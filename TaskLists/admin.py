#admin for TaskLists
from django.contrib import admin
from TaskLists.models import *

admin.site.register(Tasks)
admin.site.register(SubTasks)
admin.site.register(Collaboration)
admin.site.register(UserList)