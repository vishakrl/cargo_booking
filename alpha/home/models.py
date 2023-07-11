from django.db import models

# Create your models here.
class booking(models.Model):
    
    s_name=models.CharField(max_length=30)
    r_name=models.CharField(max_length=30)
    dst=models.CharField(max_length=40)
    address=models.TextField()
    cargo_type=models.CharField(max_length=25)
    weight=models.IntegerField()
    
    date=models.DateField()
    ctno=models.CharField(max_length=15)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.s_name
    

class order(models.Model):
    orderno=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=30)
    r_name=models.CharField(max_length=30)
    dst=models.CharField(max_length=40)
    address=models.TextField()
    cargo_type=models.CharField(max_length=25)
    weight=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField()
    ctno=models.CharField(max_length=15)

    class Meta:
        ordering=["-date"]

    def __str__(self):
        return self.s_name






