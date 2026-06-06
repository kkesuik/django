from django.urls import path
from .views import ModelFormView, ModelFormEditView, ModelListView, form_set_post

app_name='app'

urlpatterns = [
    path('form/',ModelFormView, name= 'form'),
    path('list/',ModelListView, name= 'list'),
    path('form_edit/<int:pk>/',ModelFormEditView, name= 'edit'),
    path('formset/',form_set_post, name= 'formset'),
]