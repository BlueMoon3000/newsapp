import app.settings as settings

from django.utils.encoding import smart_unicode
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from core.managers import AppUserManager

# Create your models here.

# FIXME: Move this somewhere else(?) and rewrite code and names
class SerializeMixin:
    def serializable_dict(self, version=None, **kwargs):
        rv = {'pk': self.pk, 'model': smart_unicode(self._meta)}
        # skip = ['id']
        skip = []
        options = self.serialize_options(version)

        if settings.SERIALIZE_FLATTEN_MODELS:
            field_obj = rv
        else:
            rv['fields'] = {}
            field_obj = rv['fields']

        for field in self._meta.fields:
            if 'excludes' in options and field.name in options['excludes'] or field.name in skip:
                continue
            elif 'relations' in options and field.name in options['relations']:
                if getattr(self, field.name):
                    field_obj[field.name] = getattr(self, field.name).serializable_dict(version)
                else:
                    field_obj[field.name] = getattr(self, field.name)
                if settings.SERIALIZE_INCLUDE_ID_REF:
                    field_obj['%s_id' % field.name] = getattr(self, '%s_id' % field.name)
            else:
                if isinstance(field, models.ForeignKey):
                    field_obj[field.name] = getattr(self, '%s_id' % field.name)
                    if settings.SERIALIZE_INCLUDE_ID_REF:
                        field_obj['%s_id' % field.name] = getattr(self, '%s_id' % field.name)
                else:
                    field_obj[field.name] = getattr(self, field.name, None)

        if 'extras' in options:
            for field in options['extras']:
                res = getattr(self, field)(version)
                if field.startswith('ser_'):
                    field = field.replace('ser_', '', 1)
                field_obj[field] = res

        if 'flatten' in options:
            for field in options['flatten']:
                for k, v in getattr(self, field)(version).iteritems():
                    field_obj[k] = v

        # Allow for some serialize options to only be triggered when required.
        if 'extensions' in kwargs:
            for field in kwargs['extensions']:
                if field in options['extensions']:
                    res = getattr(self, field)(version)
                    if field.startswith('flatten_'):
                        for k,v in res.iteritems():
                            field_obj[k] = v
                        break

                    if field.startswith('ser_'):
                        field = field.replace('ser_', '', 1)
                    field_obj[field] = res

        return rv

    def serialize_options(self, version=None):
        '''
        Passes serialization options to the serializable_dict method above:
            - excludes: fields to be removed from the serializable_dict
            - extras: arbitrary extra fields to add based on a function response. 
                *if 'ser_' prefix is included that will be stripped from the key in the serializable_dict.
            - flatten: flattens a dictionary into the serializable_dict
            - relations: fields to be populated from a foreign key reference
            - extensions: fields to be optionally serialized depending on context

        Note that there is no error handling in the case that you don't follow the format specified above. So shit will break. Horribly.
        '''
        return {}

class AppUser(AbstractBaseUser, SerializeMixin):
    # required
    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    full_name = models.CharField(max_length=140)

    # fb
    fb_user_id = models.CharField(max_length=20)
    fb_access_token = models.CharField(max_length=255, null=True) # FIXME: access_tokens can now be > 255 chars ?

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    last_updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name'] # only relevant to ./manage.py createsuperuser

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __unicode__(self):
        return self.email

    def serialize_options(self, version=None):
        return {
            'excludes': ('password', 'is_admin')
        }

class Topic(models.Model, SerializeMixin):
    title = models.CharField(max_length=100, unique=True)

    last_updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

# This is how we will channel similar search terms to a certain topic.
# Not very scaleable; because topics are created manually, we will also manually crate relevant search items
# Ex. Edward Snowden -> Global Surveillance Disclosures 2013...
class SearchTopic(models.Model, SerializeMixin):
    title = models.CharField(max_length=100, unique=True)
    topic = models.ForeignKey(Topic)

    # is this the same as the actual topic?
    is_master = models.BooleanField(default=False)

    last_updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Article(models.Model, SerializeMixin):
    url = models.CharField(max_length=500, unique=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField()

    last_updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

