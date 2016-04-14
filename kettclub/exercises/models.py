import uuid as uuid

import bleach as bleach

import six
from django.contrib.auth.models import User
from django.core import mail
from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string
from django.utils import translation
from django.utils.text import slugify
from kettclub import settings


class Muscle(models.Model):
    '''
    Muscle an exercise works out
    '''

    name = models.CharField(max_length=50,
                            verbose_name=('Name'),
                            help_text=('In latin, e.g. "Pectoralis major"'))

    # Whether to use the front or the back image for background
    is_front = models.BooleanField(default=1)

    # Metaclass to set some other properties
    class Meta:
        ordering = ["name", ]

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Muscle has no owner information
        '''
        return False


class Equipment(models.Model):
    '''
    Equipment used or needed by an exercise
    '''

    name = models.CharField(max_length=50,
                            verbose_name=('Name'))

    class Meta:
        '''
        Set default ordering
        '''
        ordering = ["name", ]

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Equipment has no owner information
        '''
        return False


class ExerciseCategory(models.Model):
    '''
    Model for an exercise category
    '''
    name = models.CharField(max_length=100,
                            verbose_name=('Name'),)

    # Metaclass to set some other properties
    class Meta:
        verbose_name_plural = ("Exercise Categories")
        ordering = ["name", ]

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    def get_owner_object(self):
        '''
        Category has no owner information
        '''
        return False


class Exercise(models.Model):
    '''
    Model for an exercise
    '''
    license_author = models.CharField(max_length=200)

    category = models.ForeignKey(ExerciseCategory,
                                 verbose_name=('Category'))
    description = models.TextField(max_length=2000,
                                   verbose_name=('Description'))
    '''Description on how to perform the exercise'''

    name = models.CharField(max_length=200,
                            verbose_name=('Name'))

    muscles = models.ManyToManyField(Muscle,
                                     blank=True,
                                     verbose_name=('Primary muscles'))
    '''Main muscles trained by the exercise'''

    muscles_secondary = models.ManyToManyField(Muscle,
                                               verbose_name=('Secondary muscles'),
                                               related_name='secondary_muscles',
                                               blank=True)
    '''Secondary muscles trained by the exercise'''

    equipment = models.ManyToManyField(Equipment,
                                       verbose_name=('Equipment'),
                                       blank=True)
    '''Equipment needed by this exercise'''

    creation_date = models.DateField(('Date'),
                                     auto_now_add=True,
                                     null=True,
                                     blank=True)
    '''The submission date'''

    language = models.IntegerField(1)
    '''The exercise's language'''

    license = models.IntegerField(1)
    '''The exercise's language'''

    uuid = models.CharField(verbose_name='UUID',
                            max_length=36,
                            editable=False,
                            default=uuid.uuid4)
    '''
    Globally unique ID, to identify the exercise across installations
    '''

    status = models.IntegerField(1)
    '''The exercise's language'''

    #
    # Django methods
    #
    class Meta:
        ordering = ["name", ]

    def get_absolute_url(self):
        '''
        Returns the canonical URL to view an exercise
        '''
        return reverse('exercise:exercise:view', kwargs={'id': self.id, 'slug': slugify(self.name)})

    def save(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''

        super(Exercise, self).save(*args, **kwargs)

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.name

    #
    # Own methods
    #

    @property
    def main_image(self):
        '''
        Return the main image for the exercise or None if nothing is found
        '''
        return self.exerciseimage_set.filter(is_main=True).first()

    @property
    def description_clean(self):
        '''
        Return the exercise description with all markup removed
        '''
        return bleach.clean(self.description, strip=True)

    def get_owner_object(self):
        '''
        Exercise has no owner information
        '''
        return False

    def send_email(self, request):
        '''
        Sends an email after being successfully added to the database (for user
        submitted exercises only)
        '''
        try:
            user = User.objects.get(username=self.license_author)
        except User.DoesNotExist:
            return
        if self.license_author and user.email:
            translation.activate(user.userprofile.notification_language.short_name)
            url = request.build_absolute_uri(self.get_absolute_url())
            subject = ('Exercise was successfully added to the general database')
            context = {
                'exercise': self.name,
                'url': url
            }
            message = render_to_string('exercise/email_new.html', context)
            mail.send_mail(subject,
                           message,
                           settings.WGER_SETTINGS['EMAIL_FROM'],
                           [user.email],
                           fail_silently=True)

    def set_author(self, request):
        '''
        Set author and status
        This is only used when creating exercises (via web or API)
        '''
        if request.user.has_perm('exercises.add_exercise'):
            self.status = self.STATUS_ACCEPTED
            if not self.license_author:
                self.license_author = request.get_host().split(':')[0]
        else:
            if not self.license_author:
                self.license_author = request.user.username

            subject = ('New user submitted exercise')
            message = (u'The user {0} submitted a new exercise "{1}".').format(
                request.user.username, self.name)
            mail.mail_admins(six.text_type(subject),
                             six.text_type(message),
                             fail_silently=True)


def exercise_image_upload_dir(instance, filename):
    '''
    Returns the upload target for exercise images
    '''
    return "exercise-images/{0}/{1}".format(instance.exercise.id, filename)


class ExerciseImage(models.Model):
    '''
    Model for an exercise image
    '''

    exercise = models.ForeignKey(Exercise,
                                 verbose_name=('Exercise'))
    '''The exercise the image belongs to'''

    image = models.ImageField(verbose_name=('Image'),
                              help_text=('Only PNG and JPEG formats are supported'),
                              upload_to=exercise_image_upload_dir)
    '''Uploaded image'''

    is_main = models.BooleanField(verbose_name=('Main picture'),
                                  default=False,
                                  help_text=("Tick the box if you want to set this image as the "
                                              "main one for the exercise (will be shown e.g. in "
                                              "the search). The first image is automatically "
                                              "marked by the system."))
    '''A flag indicating whether the image is the exercise's main image'''

    class Meta:
        '''
        Set default ordering
        '''
        ordering = ['-is_main', 'id']

    def save(self, *args, **kwargs):
        '''
        Only one image can be marked as main picture at a time
        '''
        if self.is_main:
            ExerciseImage.objects.filter(exercise=self.exercise).update(is_main=False)
            self.is_main = True
        else:
            if ExerciseImage.objects.accepted().filter(exercise=self.exercise).count() == 0 \
               or not ExerciseImage.objects.accepted() \
                            .filter(exercise=self.exercise, is_main=True)\
                            .count():
                self.is_main = True

    def delete(self, *args, **kwargs):
        '''
        Reset all cached infos
        '''
        super(ExerciseImage, self).delete(*args, **kwargs)

        # Make sure there is always a main image
        if not ExerciseImage.objects.accepted() \
                .filter(exercise=self.exercise, is_main=True).count() \
           and ExerciseImage.objects.accepted() \
                .filter(exercise=self.exercise) \
                .filter(is_main=False) \
                .count():

                image = ExerciseImage.objects.accepted() \
                    .filter(exercise=self.exercise, is_main=False)[0]
                image.is_main = True
                image.save()

    def get_owner_object(self):
        '''
        Image has no owner information
        '''
        return False

    def set_author(self, request):
        '''
        Set author and status
        This is only used when creating images (via web or API)
        '''
        if request.user.has_perm('exercises.add_exerciseimage'):
            self.status = self.STATUS_ACCEPTED
            if not self.license_author:
                self.license_author = 'wger.de'

        else:
            if not self.license_author:
                self.license_author = request.user.username

            subject = ('New user submitted image')
            message = (u'The user {0} submitted a new image "{1}" for exercise {2}.').format(
                request.user.username,
                self.name,
                self.exercise)
            mail.mail_admins(six.text_type(subject),
                             six.text_type(message),
                             fail_silently=True)


class ExerciseComment(models.Model):
    '''
    Model for an exercise comment
    '''
    exercise = models.ForeignKey(Exercise,
                                 verbose_name=('Exercise'),
                                 editable=False)
    comment = models.CharField(max_length=200,
                               verbose_name=('Comment'),
                               help_text=('A comment about how to correctly do this exercise.'))

    def __str__(self):
        '''
        Return a more human-readable representation
        '''
        return self.comment

    def get_owner_object(self):
        '''
        Comment has no owner information
        '''
        return False