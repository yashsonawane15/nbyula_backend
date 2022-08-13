from django.forms import Form
from django.forms import CharField, EmailField
from .models import ApplicantUser


class ApplicantSignupForm(Form):
    username = CharField()
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    password = CharField()

    def is_valid(self):
        super().is_valid()

        data = self.cleaned_data

        if ApplicantUser.objects(username=data['username']):
            self.add_error('username', 'This username is already in use')

        if ApplicantUser.objects(email=data['email']):
            self.add_error('email', 'This email is already in use')

        return data


class ApplicantLoginForm(Form):
    username = CharField()
    password = CharField()


class ApplyJobForm(Form):
    jobid = CharField()


