from django.db import models

class Passive(models.Model):
    type=models.CharField(max_length=20,unique=True)
    heading = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='Passive/')
    para1 = models.TextField()
    image1 = models.ImageField(upload_to='Passive/')
    para2 = models.TextField()
    h2 = models.CharField(max_length=50)
    para3 = models.TextField()
    image2 = models.ImageField(upload_to='Passive/')

    def __str__(self):
        return self.type

