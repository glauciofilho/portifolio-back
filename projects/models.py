from django.db import models
from mongoengine import Document, fields

class Project(Document):
    title = fields.StringField(max_length=200)
    description = fields.StringField()
    meta = {'collection': 'projects'}