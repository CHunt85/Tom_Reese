from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
      
    def __repr__(self):
        return "<Book: {}|{} {}>".format(self.id, self.name, self.desc)

      
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(Book, related_name="has_books")
    notes = models.TextField(max_length=1000)

    def __repr__(self):
        return "<Author: {}|{} {} {}>".format(self.id, self.first_name, self.last_name, self.email)

