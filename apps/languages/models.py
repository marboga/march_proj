from __future__ import unicode_literals

from django.db import models

from ..theme_app.models import Location
# Create your models here.

class LanguageManager(models.Manager):

    def create_lang(self, data):
        new_lang = self.create( name=data['language'] )
        print new_lang

    def add_location_to_language(self, data):
        loc = Location.objects.get(id=data['location'])
        print loc, type(loc)
        lang = Language.objects.get(id=data['language'])
        print "#$%^"*35
        print loc.spoken_languages.all()
        print lang, type(lang)

        lang.locations_spoken.add(loc)

        lang.save()

        return lang


class Language(models.Model):
    name = models.TextField(max_length=255)
    locations_spoken = models.ForeignKey(Location, related_name="spoken_languages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LanguageManager()
