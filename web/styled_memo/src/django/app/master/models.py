import os

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


def get_upload_to(user, filename):
    return "css/{0}/{1}".format(user.username, filename)


def get_css_default():
    return File(open("app/static/example.css", "r"), "example.css")


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, *args, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer."),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    css = models.FileField(
        "メモ用CSS",
        default=get_css_default,
        blank=True,
        upload_to=get_upload_to,
        storage=OverwriteStorage(),
    )
    admin = models.ForeignKey("User", null=True, on_delete=models.PROTECT)

    @cached_property
    def admin_username(self):
        if self.admin is not None:
            return self.admin.username
        return ""
