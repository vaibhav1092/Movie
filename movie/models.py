from django.db import models

# Create your models here.
class Movie(models.Model):
    Mname=models.CharField(max_length=100)
    Mrdate = models.DateField()
    Mlang = models.CharField(max_length=100)

    class Meta:
        db_table = "movie_Info"



class Actor(models.Model):
    # Aid=models.IntegerField()
    Aname=models.CharField(max_length=100)
    Aage= models.IntegerField()
    Agender=models.CharField(max_length=100)
    Movi_Act=models.ManyToManyField(Movie)

    class Meta:
        db_table = "actor_Info"


# class Movie_Actor(models.Model):
#     Movie=models.ForeignKey(Movie,on_delete=models.CASCADE,)
#     Actor=models.ForeignKey(Actor,on_delete=models.CASCADE,)
    # rdate=models.DateField()

    # class Meta:
    #     db_table = "movie_act_Info"
