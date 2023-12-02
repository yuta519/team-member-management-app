from django.views import generic

from members.forms import MemberForm
from members.models import Member


class MemberListView(generic.ListView):
    model = Member
    template_name = "members/list.html"


class MemberCreateView(generic.CreateView):
    model = Member
    form_class = MemberForm
    template_name = "members/create.html"
    success_url = "/members"


class MemberEditView(generic.UpdateView):
    model = Member
    template_name = "members/edit.html"
    success_url = "/members"
    fields = ["first_name", "last_name", "phone", "email", "role"]
