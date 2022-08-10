from mongoengine import Document
from mongoengine import StringField, EmailField, DateTimeField, BooleanField, ReferenceField, ListField


class User(Document):
    username = StringField()
    password = StringField()
    email = EmailField()
    first_name = StringField()
    last_name = StringField()


class Job(Document):
    title = StringField()
    description = StringField(max=300)
    location = StringField()
    deadline = DateTimeField()
    poster = ReferenceField(User)
    contact_phone = StringField()
    contact_email = EmailField()
    is_archived = BooleanField()


class JobApplicant(User):
    applied_jobs = ListField(ReferenceField(Job))


class JobPoster(User):
    posted_jobs = ListField(ReferenceField(Job))











