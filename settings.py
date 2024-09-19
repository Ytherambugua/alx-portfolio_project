INSTALLED_APPS = [
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom apps
    'blog',  # Your blog app
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files (for images uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Templates
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],  # Custom template directory
    },
]

