import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelApp.settings')
from django import setup
setup()

from ModelForm.models import Classes

class_names = ['class' + c for c in 'BCDEFGH']

for class_name in class_names:
 class_inserted = Classes(
    name= class_name
)
 class_inserted.save()