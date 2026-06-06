from django.db import models

# Create your models here.
class Classes(models.Model):
    name = models.CharField()
    
    class Meta:
        db_table = 'classes'
        
    def __str__(self):
        return self.name
        
class students(models.Model):
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE, )
    name = models.CharField(max_length= 50)
    grade = models.IntegerField()
    picture = models.FileField(blank=True,null=True)