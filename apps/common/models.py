from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, blank=True )

    def __str__(self):
        return self.name
    

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField('Country', on_deleye=models.CASCADE, related_name='citties' )

    def __str__(self):
        return self.name
