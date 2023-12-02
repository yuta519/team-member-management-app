from django.views import generic

from members.models import Member


class MemberListView(generic.ListView):
    model = Member
    template_name = "members/member_list.html"
