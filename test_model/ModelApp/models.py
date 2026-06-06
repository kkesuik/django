from django.db import models

class Tests(models.Model):

    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 50)
    
    class Meta:
        db_table = 'tests'
    
class Test_Results(models.Model):
    
    id = models.AutoField(primary_key= True)
    student_id = models.ForeignKey('students', on_delete= models.CASCADE)
    test_id = models.ForeignKey('tests',  on_delete= models.CASCADE)
    score = models.IntegerField()
    
    class Meta:
        db_table = 'test_results'
    
class Students(models.Model):
    
    id = models.AutoField(primary_key= True)
    class_id = models.ForeignKey('classes', on_delete= models.CASCADE)
    name = models.CharField(max_length= 50)
    grade = models.IntegerField()
    
    class Meta:
        db_table = 'students'
    
class Classes(models.Model):
    
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 50)
    
    class Meta:
        db_table = 'classes'
    
    