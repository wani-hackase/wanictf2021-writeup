from app.forms import FormControlMixin
from app.memo.models import Memo

from django import forms


class MemoForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Memo
        fields = ("title", "content")


class MemoCreateForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Memo
        fields = ("title", "content")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        memo = super().save(commit=False)
        memo.user = self.request.user
        if commit:
            memo.save()
        return memo
