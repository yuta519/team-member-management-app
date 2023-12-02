from django.db import models


class Member(models.Model):
    class Role(models.TextChoices):
        REGULAR = 'regular', 'Regular'
        ADMIN = 'admin', 'Admin'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # The longest international phone number is 15 digits from the below link.
    # https://en.wikipedia.org/wiki/E.164
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.REGULAR,
    )

    class Meta:
        db_table = "members"
