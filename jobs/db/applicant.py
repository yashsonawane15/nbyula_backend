import jwt
from django.contrib.auth import hashers
from jobs import settings
from jobs.models import ApplicantUser, JobApplication, JobListing
from datetime import datetime


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
    user = ApplicantUser.objects(username=data['username']).first()
    if not hashers.check_password(data['password'], user.password):
        return {
            "code": 401,
            "msg": "The username or password is incorrect"
        }

    payload = {"role": "applicant", "id": str(user.id)}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return {
        "code": 200,
        "data": {
            "token": token,
            "id": str(user.id)
        }
    }


def get_job_applicant(id):
    app = ApplicantUser.objects(id=id).first()

    return {
        "code": 200,
        "data": {
            "name": app.first_name + " " + app.last_name,
            "email": app.email,
            "username": app.username
        }
    }


def get_listings():

    job_listings = JobListing.objects(status="Active")
    listings = []

    for listing in job_listings:
        job = listing.job

        listings.append({
            "id": listing.id,
            "title": job.title,
            "description": job.description,
            "lastDate": job.deadline
        })

    return {
        "code": 200,
        "data": {
            "listings": listings
        }
    }


def extract_applied_jobs(applicant):
    jobapps_cursor = JobApplication.objects(applicant=applicant).order_by('-applied_date')
    jobs = []

    for job_application in jobapps_cursor:
        job_listing = job_application.job
        job = job_listing.job

        jobs.append({
            "id": job_application.id,
            "title": job.title,
            "description": job.description,
            "status": job_listing.status
        })

    return jobs


def get_applied_jobs(userid):
    applicant = ApplicantUser.objects(id=userid).first()

    if not applicant:
        return {
            "code": 400,
            "data": {
                "msg": "User not found"
            }
        }

    applied_jobs = extract_applied_jobs(applicant)

    return {
        "code": 200,
        "data": {
            "applications": applied_jobs
        }
    }


def apply_job(app_id, data):
    job_listing = JobListing.objects(id=data['jobid']).first()
    applicant = ApplicantUser.objects(app_id).first()

    if not applicant:
        return {
            "code": 400,
            "data": {
                "msg": "Your profile was not found"
            }
        }

    if not job_listing:
        return {
            "code": 400,
            "data": {
                "msg": "Job listing not found!"
            }
        }

    application = JobApplication()
    application.applicant = applicant
    application.job = job_listing.job
    application.applied_date = datetime.now()

    application.save()

    return {
        "code": 200,
        "data": {
            "msg": "You have successfully applied."
        }
    }






