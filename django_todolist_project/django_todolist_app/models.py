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
      
    def to_json(self):
        return {
            "_id": str(self.id),  # Convert ObjectId to string
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }