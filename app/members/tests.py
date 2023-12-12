from django.test import Client, TestCase
from django.urls import reverse

from members.models import Member


class MemberModelTests(TestCase):
    first_name="First Name"
    last_name="Last Name"
    email="member@localhost"
    phone="0000000000"

    def setUp(self) -> None:
        member = Member(
           first_name=self.first_name,
           last_name=self.last_name,
           email=self.email,
           phone=self.phone
        )
        member.save()
        return super().setUp()

    def tearDown(self) -> None:
        member = Member.objects.get(email=self.email)
        member.delete()
        return super().tearDown()

    def test_filter_by_first_name(self) -> None:
        member = Member.objects.get(first_name=self.first_name)
        self.__compare_member_values(member)

    def test_filter_by_last_name(self) -> None:
        member = Member.objects.get(last_name=self.last_name)
        self.__compare_member_values(member)

    def test_filter_by_phone(self) -> None:
        member = Member.objects.get(phone=self.phone)
        self.__compare_member_values(member)

    def test_filter_by_email(self) -> None:
        member = Member.objects.get(email=self.email)
        self.__compare_member_values(member)

    def test_filter_by_role(self) -> None:
        member = Member.objects.get(role=Member.Role.REGULAR)
        self.__compare_member_values(member)

    def test_member_doesnot_exist(self) -> None:
        with self.assertRaises(Member.DoesNotExist):
            Member.objects.get(email="non_exist@example.com")

    def test_update_first_name(self):
        updated_value = "Updated First Name"
        member = Member.objects.get(email=self.email)
        member.first_name = updated_value
        member.save()
        self.__compare_member_values(member, first_name=updated_value)

    def test_update_last_name(self):
        updated_value = "Updated Last Name"
        member = Member.objects.get(email=self.email)
        member.last_name = updated_value
        member.save()
        self.__compare_member_values(member, last_name=updated_value)

    def test_update_phone(self):
        updated_value = "Updated phone"
        member = Member.objects.get(email=self.email)
        member.phone = updated_value
        member.save()
        self.__compare_member_values(member, phone=updated_value)

    def test_update_email(self):
        updated_value = "Updated email"
        member = Member.objects.get(email=self.email)
        member.email = updated_value
        member.save()
        self.__compare_member_values(member, email=updated_value)

        # For tearDown, change the email value to original one
        member.email = self.email
        member.save()

    def test_update_role(self):
        member = Member.objects.get(email=self.email)
        member.role = Member.Role.ADMIN
        member.save()
        self.__compare_member_values(member, role=Member.Role.ADMIN)

    def test_is_admin__reqular_user(self):
        member = Member.objects.get(email=self.email)
        self.assertEqual(member.is_admin(), False)

    def test_is_admin_with_admin_user(self):
        member = Member.objects.get(email=self.email)
        member.role = Member.Role.ADMIN
        member.save()
        self.assertEqual(member.is_admin(), True)

    def test_concat_name(self):
        member = Member.objects.get(email=self.email)
        self.assertEqual(member.concat_name(), f'{self.first_name} {self.last_name}')

    def __compare_member_values(self, member: Member, **kawargs) -> None:
        self.assertEqual(member.first_name, kawargs.get("first_name", self.first_name))
        self.assertEqual(member.last_name, kawargs.get("last_name", self.last_name))
        self.assertEqual(member.phone, kawargs.get("phone", self.phone))
        self.assertEqual(member.email, kawargs.get("email", self.email))
        self.assertEqual(member.role, kawargs.get("role", Member.Role.REGULAR))


class MemberListViewTests(TestCase):
    # On fixtures, there are 5 members.
    fixtures = ["members.json"]
    client = Client()

    def test_title_and_header(self):
        response = self.client.get(reverse("members:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Team Member Management App")
        self.assertContains(response, "Team members")

    def test_amount_of_members(self):
        response = self.client.get(reverse("members:list"))
        self.assertContains(response, "You have 5 team members.")

    def test_amout_of_members_when_add_new_member(self):
        member = Member.objects.create()
        member.save()

        response = self.client.get(reverse("members:list"))
        self.assertContains(response, "You have 6 team members.")

    def test_amout_of_members_when_delete_a_member(self):
        member = Member.objects.get(pk=1)
        member.delete()

        response = self.client.get(reverse("members:list"))
        self.assertContains(response, "You have 4 team members.")
