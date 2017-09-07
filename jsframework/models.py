from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, db_index=True)
    session = models.CharField(max_length=32, blank=True, null=True, db_index=True)

    title = models.CharField(max_length=75)
    # description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
