from pathlib import Path
import os

from pathlib import Path

# Navegación correcta de directorios:
# /home/thor/my-staklab/backend/config/settings/dev.py → ../../.. → /home/thor/my-staklab/backend/
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # 3 niveles arriba
DEBUG = True
ALLOWED_HOSTS = ['*']
# Configuración de base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Se creará en /home/thor/my-staklab/backend/
    }
}

ROOT_URLCONF = 'config.urls'
#print(Path(__file__).resolve())  # Agrega esto temporalmente en dev.py para ver la ruta
#print(f"BASE_DIR: {BASE_DIR}")  # Debe mostrar: /home/thor/my-staklab/backend
#print(f"Ruta de DB: {BASE_DIR / 'db.sqlite3'}")  # Debe mostrar: /home/thor/my-staklab/backend/db.sqlite3

