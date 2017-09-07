from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in


class Todo(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, db_index=True)
    session = models.CharField(max_length=32, blank=True, null=True, db_index=True)

    title = models.CharField(max_length=75)
    # description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


# def migrate_anonymous_todos(sender, user, request, **kwargs):
#     import pdb; pdb.set_trace()
#     Todo.objects.filter(session=request.session.session_key).update(user=user)
# user_logged_in.connect(migrate_anonymous_todos)