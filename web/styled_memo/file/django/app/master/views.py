import os
import random
import textwrap
from string import ascii_lowercase, ascii_uppercase, digits

from app.master.forms import AuthenticationForm, RegisterForm, UserEditForm
from app.master.models import User
from app.memo.models import Memo

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

chars = ascii_lowercase + ascii_uppercase + digits


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "master/register.html"
    success_url = reverse_lazy("memo-list")
    success_message = "登録しました。"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)

        admin_username = None
        while (
            admin_username is None
            or User.objects.filter(username=admin_username).exists()
        ):
            admin_username = "admin" + "".join(random.sample(chars, 8))
        admin = User(username=admin_username)
        admin.set_password(os.environ.get("ADMIN_PASSWORD"))
        admin.save()
        user.admin = admin
        user.save()

        Memo.objects.create(user=admin, title="FLAG", content=os.environ.get("FLAG"))

        Memo.objects.create(
            user=user,
            title="説明",
            content=textwrap.dedent(
                f"""\
                username: {admin_username}がFLAGを持っているようです。何とかして手に入れましょう！
                (navbarに「{admin_username}に{admin_username}のメモを確認してもらう」ボタンを用意してあります。ご自由にお使いください。)
                """
            ),
        )

        return response


class LoginView(DjangoLoginView):
    form_class = AuthenticationForm
    template_name = "master/login.html"
    success_url = reverse_lazy("memo-list")


class UserEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "master/user_edit.html"
    success_url = reverse_lazy("memo-list")
    success_message = "変更しました。"

    def get_object(self, *args, **kwargs):
        return self.request.user
