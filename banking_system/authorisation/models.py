from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(BaseModel) :
    user_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=13)
    frist_name = models.CharField(max_length=13)
    username = models.CharField(unique=True,db_index=True,max_length=36)
    gender = models.CharField(
        max_length=1, choices=(("m", "Male"), ("f", "Female")), null=False
    )
    date_of_birth = models.DateField()
    email_id = models.EmailField(
            max_length=10,
            unique=True
    )
    mobile_number = models.CharField(
        max_length=10
    )
    password = models.CharField(
        max_length=100
    )
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    block_expiration = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    unsuccessful_attempts = models.IntegerField(default=0)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
