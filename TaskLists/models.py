from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# TaskLists

class Tasks(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	task_date = models.DateTimeField('date published')


class SubTasks(models.Model):
	task = models.ForeignKey(Tasks)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	subtask_date = models.DateTimeField('date published')

class Collaboration(models.Model):
	userowener = models.ForeignKey(User)
	task = models.ForeignKey(Tasks)

class UserList(models.Model):
	Collaboration = models.ForeignKey(Collaboration)
	user = models.ForeignKey(User)
