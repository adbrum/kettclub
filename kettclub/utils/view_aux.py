from datetime import date, datetime
from django.conf import settings
from django.http import HttpResponse
import json
import os

# Devolve a data e hora actual
def dateTime_actual():
    return datetime.now() 


UPLOAD_PATH = 'uploads/%Y/%m'
# Faz upload das imagens
def handle_uploaded_file_img(source):
    
    upload_dir = date.today().strftime(UPLOAD_PATH)
    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)
    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)
    for key, file in source.FILES.items():
        path = '{0}/{1}/{2}'.format(settings.MEDIA_ROOT, upload_dir, file.name)
        os.system('chmod -R 777 {0}'.format(path))
        dest = open(path, 'w')
        if file.multiple_chunks:
            for c in file.chunks():
                dest.write(c)
        else:
            dest.write(file.read())
        dest.close()

# Faz upload das imagens
def upload_imagens(request):
    nameFile = request.FILES.get('file')
    
    ##print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", nameFile 
    
    handle_uploaded_file_img(request)
    upload_dir = date.today().strftime(UPLOAD_PATH)
    #caminhoImagem = '{0}/{1}/{2}'.format(settings.MEDIA_ROOT, upload_dir, nameFile)
    #caminhoStatic = '{0}{1}/'.format("kettclub"+settings.STATIC_URL, "imagens")
    
    caminhoImagem = '{0}/{1}/{2}'.format(settings.MEDIA_ROOT, upload_dir, nameFile)
    caminhoStatic = '{0}{1}/'.format(settings.STATIC_ROOT, "imagens")
    
    os.system("mv {0} {1}".format(caminhoImagem, caminhoStatic))
    pathImage = '{0}{1}/{2}'.format(settings.STATIC_URL, "imagens", nameFile)
    
    response_data = {}
    response_data['image'] = pathImage
    return HttpResponse(json.dumps(response_data), content_type="application/json")

# Faz upload das imagens da webcam
def upload_webcam(request):
    nameFile = request.POST['file']
    participanteId = request.POST['pId']
    #print "EDITADO AGORA___________________", participanteId
    participanteNi = request.POST['pNi']
    
    #caminhoStatic = '{0}{1}/'.format("kettclub"+settings.STATIC_URL, "FotosCredenciados")
    
    caminhoStatic = '{0}{1}/'.format(settings.STATIC_ROOT, "FotosCredenciados")
    
    today = datetime.today()
    dataEmi = today.strftime('%d_%m_%Y_%M_%S')
    nomefich = str(participanteId)+ "_" + str(participanteNi)+dataEmi+".png"

    fh = open(caminhoStatic + nomefich, "wb")
    fh.write(nameFile.decode('base64'))
    fh.close()

    #handle_uploaded_file_img(request)
    #upload_dir = date.today().strftime(UPLOAD_PATH)
    #caminhoImagem = '{0}/{1}/{2}'.format(settings.MEDIA_ROOT, upload_dir, nameFile)
    
    #os.system("mv {0} {1}".format(caminhoImagem, caminhoStatic))
    pathImage = '{0}{1}/{2}'.format(settings.STATIC_URL, "FotosCredenciados", nomefich)

    #print "-------------TESTE--------------", pathImage    

    response_data = {}
    response_data['image'] = pathImage

    #Guarda a imagem na base de dados
    # Credenciados.objects.filter(id = int(participanteId)).update(
    #                                             imagem = pathImage)
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

# Comparar duas listas, 
# recebe 2 listas
# devolve lista dos elementos que sairam a lista Inicial
# devolve lista dos elementos que entraram a lista Inicial
# devolve lista dos elementos que se mantiveram na lista Inicial
def comparListas(listaInicial, listaFinal):
    listaElementEntrada = list(set(listaFinal).difference(listaInicial))
    listaElementSaida = list(set(listaInicial).difference(listaFinal))
    listaElementManteve = list(set(listaInicial).intersection(listaFinal))
    
    return listaElementEntrada, listaElementSaida, listaElementManteve
    
    
    
# logotipo
def uploadImagemLogotipo(request):
    nameFile = request.FILES.get('file')
    handle_uploaded_file_img(request)
    upload_dir = date.today().strftime(UPLOAD_PATH)
    caminhoImagem = '{0}/{1}/{2}'.format(settings.MEDIA_ROOT, upload_dir, nameFile)
    caminhoStatic = '{0}{1}/'.format("kettclub"+settings.STATIC_URL, "imagens")
    os.system("mv {0} {1}".format(caminhoImagem, caminhoStatic))
    #print "mv {0} {1}".format(caminhoImagem, caminhoStatic)
    pathImage = '{0}{1}/{2}'.format(settings.STATIC_URL, "imagens", nameFile)
    # try:
    #     Logotipo.objects.get(id = 2)
    #     Logotipo.objects.filter(id = 2).update(imagem = pathImage)
    # except:
    #     logo = Logotipo(id = 2, imagem = pathImage)
    #     logo.save()
    
    response_data = {}
    response_data['image'] = pathImage
    return HttpResponse(json.dumps(response_data), content_type="application/json")
