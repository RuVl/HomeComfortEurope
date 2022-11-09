import hashlib
import random

from .models import UserProfileModel
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = UserProfileModel
#         fields = ('email', 'phone_number', 'password1', 'password1', 'CompanyName', 'is_dealer',
#                   'interested_in_stocking', 'is_consumer')
#
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             for field_name, field in self.fields.items():
#                 field.widget.attrs['class'] = 'form-control'
#                 field.help_text = ''
#
#         def save(self):
#             user = super(UserProfileModel, self).save()
#             user.username = UserRegisterForm.request['POST']['email']
#             salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
#             user.save()
#             return user
