from decimal import Decimal


# Navigation
WORKOUT_TAB = 'workout'
EXERCISE_TAB = 'exercises'
WEIGHT_TAB = 'weight'
NUTRITION_TAB = 'nutrition'
SOFTWARE_TAB = 'software'
USER_TAB = 'user'

# Default quantization
TWOPLACES = Decimal('0.01')
FOURPLACES = Decimal('0.0001')

# Valid date formats
DATE_FORMATS = ['%d.%m.%Y',  # '25.10.2012'
                '%d.%m.%y',  # '25.10.12'

                '%m/%d/%Y',  # '10/25/2012'
                '%m/%d/%y',  # '10/25/12'

                '%Y-%m-%d',  # '2012-10-25'
                ]

# Allowed tags, attributes and styles allowed in textareas edited with a JS
# editor. Everything not in these whitelists is stripped.
HTML_TAG_WHITELIST = ('strong',
                      'em',
                      'ul',
                      'ol',
                      'li',
                      'p')

HTML_ATTRIBUTES_WHITELIST = {
    '*': 'style'
}

HTML_STYLES_WHITELIST = ('text-decoration',)


# Pagination
PAGINATION_OBJECTS_PER_PAGE = 25
PAGINATION_MAX_TOTAL_PAGES = 10
PAGINATION_PAGES_AROUND_CURRENT = 5
