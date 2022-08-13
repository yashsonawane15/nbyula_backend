from django.views import View
from django.http import JsonResponse
from .db import applicant
from .forms import ApplicantSignupForm, ApplicantLoginForm, ApplyJobForm
from.validation import validate_payload, authenticate
from django.views.decorators.csrf import csrf_exempt


class ApplicantSignup(View):
    forms = {
        'POST': ApplicantSignupForm
    }

    @validate_payload
    def post(self, request, *args, **kwargs):
        applicant.signup(self.payload)


class ApplicantLogin(View):
    forms = {
        'POST': ApplicantLoginForm
    }

    @validate_payload
    def post(self, request, *args, **kwargs):
        response = applicant.login(self.payload)

        return JsonResponse(response['data'], status=response['code'])


class JobApplicantView(View):

    @authenticate
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        response = applicant.get_job_applicant(id)

        return JsonResponse(response['data'], status=200)


class JobApplicantsView(View):
    forms = {
        # 'POST':
    }

    @authenticate
    def get(self, request,  *args, **kwargs):
        poster_id = kwargs['id']

        response = applicant.get_applicant(id)

        return JsonResponse(response['data'], status=response['code'])

    @authenticate
    @validate_payload
    def post(self, request, *args, **kwargs):
        pass


class AppliedJobsView(View):

    @authenticate
    def get(self, request, *args, **kwargs):
        userid = kwargs['id']
        response = applicant.get_applied_jobs(userid)

        return JsonResponse(response['data'], status=response['code'])


class ApplyJob(View):
    forms = {
        'POST': ApplyJobForm
    }

    @authenticate
    @validate_payload
    def post(self, request, *args, **kwargs):
        app_id = kwargs['id']

        response = applicant.apply_job(app_id, self.payload)

        return JsonResponse(response['data'], status=response['code'])


class ApplicantListings(View):


    @authenticate
    def get(self, request, *args, **kwargs):
        response = applicant.get_listings()

        return JsonResponse(response['data'], status=response['code'])










