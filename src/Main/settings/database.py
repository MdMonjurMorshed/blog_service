from Main.settings import DB_NAME,DB_USER,DB_PASS,DB_HOST,DB_PORT

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
      
    },

  
}