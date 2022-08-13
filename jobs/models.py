from mongoengine import Document
from mongoengine import StringField, EmailField, DateTimeField, BooleanField, ReferenceField, ListField


class ApplicantUser(Document):
    username = StringField()
    password = StringField()
    email = EmailField()
    first_name = StringField()
    last_name = StringField()


class PosterUser(Document):
    username = StringField()
    password = StringField()
    email = EmailField()
    first_name = StringField()
    last_name = StringField()


class Job(Document):
    title = StringField()
    description = StringField(max=300)
    location = StringField()
    poster = ReferenceField(PosterUser)
    contact_phone = StringField()
    contact_email = EmailField()


class JobListing(Document):
    job = ReferenceField(Job)
    deadline = DateTimeField()
    status = StringField()


class JobApplication(Document):
    applicant = ReferenceField(ApplicantUser)
    job_listing = ReferenceField(JobListing)
    applied_date = DateTimeField()

    meta = {'indexes': [('applicant', 'job')]}









