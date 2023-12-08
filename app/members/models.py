from django.db import models


class Member(models.Model):
    class Role(models.TextChoices):
        REGULAR = 'regular', 'Regular'
        ADMIN = 'admin', 'Admin'

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    # The longest international phone number is 15 digits.
    # https://en.wikipedia.org/wiki/E.164
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=False, blank=False)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.REGULAR)

    def concat_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_admin(self):
        return self.role == self.Role.ADMIN

    class Meta:
        db_table = "members"
