from django.db import models

# Create your models here.

class Categorie(models.Model):
    titre = models.CharField(max_length = 255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_upd = models.DateTimeField(auto_now = True)
    statut = models.BooleanField(default = True)

class Post(models.Model):
    titre = models.CharField(max_length = 255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_upd = models.DateTimeField(auto_now = True)
    statut = models.BooleanField(default = True)
    categorie_id = models.ForeignKey('Categorie', on_delete = models.CASCADE, related_name = 'categorie_post')
    image = models.ImageField(upload_to='image/', blank=True)
    #post = models.ForeignKey (Post, on_delete = models.CASCADE, nom_relatif = " article_article " , null = true)