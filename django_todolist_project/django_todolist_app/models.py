from django.db import models
import mongoengine as me
class Todos(me.Document):
    title = me.StringField()
    description = me.StringField()
    completed = me.BooleanField(default=False)
    created_at = me.DateTimeField(auto_now_add=True)
    updated_at = me.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title