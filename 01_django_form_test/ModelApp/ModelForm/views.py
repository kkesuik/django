from django.shortcuts import render
from .forms import UserForm,UserFormSet
from .models import students
from django.shortcuts import render, get_object_or_404
# Create your views here.

form = UserForm()
Students =students.objects.all()

def ModelListView(request):
    
    return render(request,'list.html',context={
        'students':Students,
    })

def ModelFormView(request):
    if request.method == 'POST':
        form_post = UserForm(request.POST)
        if form_post.is_valid():
            form_post.save()
            print('save completed')
    return render(request,'template.html',context={'form':form})


def ModelFormEditView(request, pk):
    student = get_object_or_404(students, pk=pk)
    form_edit = UserForm(request.POST or None,request.FILES or None, instance=student)
    if form_edit.is_valid():
            form_edit.save()
            print('save completed')
    return render(request,'template2.html',context={'form':form_edit,'student':student})

def form_set_post(request):
    formset = UserFormSet(request.POST or None)
    if formset.is_valid():
     formset.save()
    return render(request,'form_set_post.html',context={
        'formset':formset,
    })