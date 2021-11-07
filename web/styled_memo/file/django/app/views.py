import os

import django_rq
from app.crawler import crawler

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import View


class CrawlView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        django_rq.enqueue(
            crawler, request.user.admin_username, os.environ.get("ADMIN_PASSWORD")
        )
        messages.success(request, f"{request.user.admin_username}が確認を行います。しばらくお待ちください。")
        return HttpResponseRedirect(reverse_lazy("memo-list"))
