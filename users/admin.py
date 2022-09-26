from django.contrib import admin

# Register your models here.
from .models import ExtendUser
from django.apps import apps

admin.site.register(ExtendUser)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
