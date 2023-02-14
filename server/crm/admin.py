from django.contrib import admin
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()

admin.site.register(User)
admin.site.register(models.Project)
admin.site.register(models.Position)
admin.site.register(models.PositionMark)
admin.site.register(models.PositionAdditionalMark)
