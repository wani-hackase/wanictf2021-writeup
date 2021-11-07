from app.master import views as master_views
from app.memo import views as memo_views
from app.views import CrawlView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("", memo_views.MemoListView.as_view(), name="memo-list"),
    path("memo/create", memo_views.MemoCreateView.as_view(), name="memo-create"),
    path("memo/<int:pk>", memo_views.MemoEditView.as_view(), name="memo-edit"),
    path("register", master_views.RegisterView.as_view(), name="register"),
    path("user", master_views.UserEditView.as_view(), name="user"),
    path(
        "login",
        master_views.LoginView.as_view(),
        name="login",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("crawl", CrawlView.as_view(), name="crawl"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
