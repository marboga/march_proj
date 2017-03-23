from __future__ import unicode_literals
# from ..languages.models import Language
from django.db import models
import bcrypt

# from ..other_app.models import ClassName

# Create your models here.
# def invocation():
#     return "I was invoked"

class LocationManager(models.Manager):

    def validate_location(self, data):
        print "in models", data

        errors = []

        if len(data['name']) < 1:
            errors.append('Name must not be blank')


        #all my other validations

        if errors:
            return (False, errors)
        else:
            new_obj = Location.objects.create(
                name=data['name'],
                latitude=float(data['latitude']),
                longitude=float(data['longitude']),
            )
            return (True, new_obj)


class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # zip_code = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #activities

    objects = LocationManager()

    def __unicode__(self):
        return self.name

class ActivityManager(models.Manager):
    def validate_activity(self, data):
        print "in models", data

        errors = []

        if len(data['name']) < 1:
            errors.append('Name must not be blank')

        try:
            loc = Location.objects.get(id=data['location_id'])
            print loc
        except Location.DoesNotExist:
            errors.append('Location does not exist')

        if errors:
            return (False, errors)

        else:    #no errors
            activity = Activity.objects.create(
                name=data['name'],
                location=loc,
            )
            return (True, activity)

class Activity(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, related_name="activities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ActivityManager()

    def __unicode__(self):
        return self.name

class LockboxManager(models.Manager):
    def validate_lockbox(self, data):
        print data
        errors = []
        #validations

        if errors:
            return (False, errors)
        else:
            #create our Lockbox
            first_obj = Lockbox.objects.get(id=1)
            old_pass = first_obj.key.encode()

            hashed_key = bcrypt.hashpw(
                data['passphrase'].encode(),
                old_pass
            )
            print "\n\n", "*"*50, "\nhere is hash", hashed_key
            box = self.create(
                label=data['label'],
                key=hashed_key
            )
            return (True, box)


class Lockbox(models.Model):
    label = models.CharField(max_length=200)
    key = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LockboxManager()
