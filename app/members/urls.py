from django.urls import path

from members import views

app_name = "members"

urlpatterns = [
    path("", views.MemberListView.as_view(), name="list"),
    path("new", views.MemberCreateView.as_view(), name="create"),
    path("edit/<int:pk>", views.MemberEditView.as_view(), name="edit"),
]
