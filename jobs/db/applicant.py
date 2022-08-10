import jwt as jwt
from django.contrib.auth import hashers
from jobs import settings
from jobs.models import ApplicantUser


def signup(data):
    user = ApplicantUser()

    user.username = data['username']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.email = data['email']
    user.password = hashers.make_password(data['password'])
    user.save()

    return {
        "code": 201,
        "data": {
            "msg": "You are ready to go!"
        }
    }


def login(data):
    user = ApplicantUser.objects(username=data['username'])
    if not hashers.check_password(data['password'], user.password):
        return {
            "code": 401,
            "msg": "The username or password is incorrect"
        }

    payload = {"role": "applicant", "id": str(user.id)}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=['HS256'])

    return {
        "code": 200,
        "data": {
            "token": token.decode()
        }
    }


def get_applicant(id):

    return None


def get_job_applicant():
    pass










