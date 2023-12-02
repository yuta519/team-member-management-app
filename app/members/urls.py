from django.urls import path

from members import views

app_name = "members"

urlpatterns = [
    path("", views.MemberListView.as_view(), name="members")
]
