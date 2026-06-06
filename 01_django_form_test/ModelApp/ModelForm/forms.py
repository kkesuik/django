from django.forms import ModelForm,formset_factory
from .models import Classes,students

class UserForm(ModelForm):
    class Meta:
        model = students
        fields = ['name','grade','class_id','picture']
        
UserFormSet = formset_factory(UserForm,extra=3)
        

    

    
    
        
    # class_id = forms.
    # name = forms.CharField(max_length=50,)
    # grade = forms.IntegerField()
    # picture = forms.FileField()