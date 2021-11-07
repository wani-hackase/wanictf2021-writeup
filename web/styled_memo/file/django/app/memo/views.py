from app.memo.forms import MemoCreateForm, MemoForm
from app.memo.models import Memo

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView


class MemoQuerySetMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class MemoListView(LoginRequiredMixin, MemoQuerySetMixin, ListView):
    model = Memo
    context_object_name = "memos"
    template_name = "memo/list.html"


class MemoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Memo
    template_name = "memo/form.html"
    form_class = MemoCreateForm
    success_message = "登録しました。"
    success_url = reverse_lazy("memo-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class MemoEditView(
    LoginRequiredMixin,
    MemoQuerySetMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Memo
    template_name = "memo/form.html"
    form_class = MemoForm
    success_message = "変更しました。"
    success_url = reverse_lazy("memo-list")
