from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class booking(models.Model):
    order_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    date_book = models.DateField()
    time = models.DateTimeField()
    people=models.IntegerField(default=1)
    message= models.CharField(max_length=5000)

    def __str__(self):
        return self.name
