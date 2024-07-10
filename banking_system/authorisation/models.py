from django.db import models
from django.core import validators

# Create your models here.

class BaseModel(models.Model):
    is_created = models.DateTimeField(auto_now_add=True, editable=False)
    is_updated = models.DateTimeField(auto_now_add=True, editable=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserDetails(BaseModel):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    user_name = models.CharField(db_index=True, max_length=30, null=False, blank=False)
    mobile_number = models.CharField(
        max_length=10,
        db_index=True,
        null=False,
        unique=True,
        validators=[
            validators.RegexValidator(
                regex=r"^\+91[6-9]\d{9}$",
                message='Mobile number must be in the format: "+91XXXXXXXXXX", where X is a digit and the number starts with 6, 7, 8, or 9.',
            )
        ],
    )
    email_id = models.EmailField(
        max_length=50,
        null=False,
        db_index=True,
        unique=True,
        validators=[validators.EmailValidator(message="Invalid email format")],
    )
    password = models.CharField(
        max_length=50,
        db_index=True,
        null=False,
        validators=[
            validators.RegexValidator(
                regex=r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$",
                message="Password must contain at least 8 characters, including at least one digit, one lowercase letter, "
                        "and one uppercase letter.",
            )
        ],
    )
    is_mobile_verified = models.BooleanField(null=False, )
    gender = models.CharField(
        choices=(("M", "Male"), ("F", "Female")),
        null=False,
        blank=False,
        max_length=1,
    )
    date_of_birth = models.DateField(
        null=False,
        blank=False,
        validators=[
            validators.RegexValidator(
                regex=r"^\d{4}-\d{2}-\d{2}$",
                message='Date of birth must be in the format: "YYYY-MM-DD".'
            )
        ]
    )
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    profile_picture = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(auto_now_add=True, editable=True)
    unsuccessfull_attempts = models.IntegerField(default=0)
    is_blocked = models.BooleanField(default=False)
    block_expiration = models.DateTimeField(null=True, blank=True)
    recaptcha_attempts = models.IntegerField(default=False)
    