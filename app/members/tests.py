from django.test import TestCase

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
        member = Member.objects.get(email=self.email)
        member.first_name = "Updated First Name"
        member.save()
        print(member.first_name)
        self.__compare_member_values(member, first_name="Updated First Name")

    def test_update_last_name(self):
        pass

    def test_update_phone(self):
        pass

    def test_update_email(self):
        pass

    def test_update_role(self):
        pass

    def __compare_member_values(self, member: Member, **kawargs) -> None:
        self.assertEqual(member.first_name, kawargs.get("first_name", self.first_name))
        self.assertEqual(member.last_name, kawargs.get("last_name", self.last_name))
        self.assertEqual(member.phone, kawargs.get("phone", self.phone))
        self.assertEqual(member.email, kawargs.get("email", self.email))
        self.assertEqual(member.role, kawargs.get("role", Member.Role.REGULAR))
