# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
    )
    search_fields = ( 'titre' , 'date_add' ,)


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
        'categorie_id',
        'image',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'categorie_id',
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
        'categorie_id',
        'image',
    )
    search_fields = ( 'titre',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Post, PostAdmin)
