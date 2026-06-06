import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Tests, Test_Results, Classes, Students

T = Tests(
    name= 'Taro'
)
T.save()