from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=50)
    roll_no= models.CharField(max_length=9)
    year= models.CharField(max_length=4)
    picture= models.ImageField(upload_to='images/', blank=True, null=True)
    parentId= models.CharField(max_length=400,  default=None, blank=True, null=True)
    linkedIn= models.URLField(max_length=200)
    def __str__(self):
        return self.roll_no


# class TreeNode(models.Model):
#     name= models.CharField(max_length=50)
#     roll_no= models.CharField(max_length=9)
#     parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.roll_no