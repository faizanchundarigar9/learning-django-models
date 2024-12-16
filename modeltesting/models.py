from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return f"Musician {self.first_name} {self.last_name}"

class Album(models.Model):
    
    languages = {
        "E": "English",
        "H": "Hindi",
        "G": "Gujarati",
    }
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    release_date = models.DateField()
    rating = models.IntegerField() 
    language = models.CharField(max_length=1, choices=languages,default="E")
    # language = models.TextChoices('English','Hindi','Gujarati')


    def __str__(self):
        return f"{self.name} by {self.artist}"  
   
 

