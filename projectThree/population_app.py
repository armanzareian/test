import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","projectThree.settings")

import django
django.setup()

from first_app.models import User
from faker import Faker

fakegen=Faker()

def create_user(num=5):
    for i in range(num):
        fake_name=fakegen.first_name_male()
        fake_last=fakegen.last_name()
        fake_email=fake_name+fake_last+"@gmail.com"

        User.objects.get_or_create(First_name=fake_name,Last_name=fake_last,Email=fake_email)

if __name__=='__main__':
    print ("populating")
    create_user(20)
    print("populate complete")
