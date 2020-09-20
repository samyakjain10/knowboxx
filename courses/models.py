from django.db import models

# Create your models here.
class Courses(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class1 = models.IntegerField()
    board = models.CharField(max_length=20)
    content = models.TextField()
    duration = models.CharField(max_length=20)
    featuredImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}  ,  {self.class1}  ,  {self.board}"
