from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Post,Category
from accounts.models import User,Profile
import random
from django.utils import timezone

category_list=['it','fun','backend']

class Command(BaseCommand):

    def __init__(self,*args,**kwargs):
        super(BaseCommand,self).__init__(*args,**kwargs)
        self.fake=Faker()

    def handle(self,*args,**options):
        user=User.objects.create_user(email=self.fake.email(),password='mxgyuirt22ali')
        profile=Profile.objects.get(user=user)
        profile.first_name=self.fake.first_name()
        profile.last_name=self.fake.last_name()
        profile.description=self.fake.paragraph(nb_sentences=5)
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)
    
        for _ in range(5):
            Post.objects.create(
                author=profile,
                title=self.fake.paragraph(nb_sentences=1),
                content=self.fake.paragraph(nb_sentences=5),
                status=random.choice([True,False]),
                category=Category.objects.get(name=random.choice(category_list)),
                published_date=timezone.now()
            )
