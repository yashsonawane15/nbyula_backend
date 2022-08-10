from django.views import View
from django.http import JsonResponse
from .db import applicant
from .forms import ApplicantSignupForm, ApplicantLoginForm
from.validation import validate_payload
from django.views.decorators.csrf import csrf_exempt


class ApplicantSignup(View):
    forms = {
        'POST': ApplicantSignupForm
    }

    @csrf_exempt
    @validate_payload
    def post(self, request, *args, **kwargs):
        applicant.signup()


class ApplicantLogin(View):
    forms = {
        'POST': ApplicantLoginForm
    }

    @validate_payload
    def post(self, request, *args, **kwargs):
        applicant.login()


class JobApplicantView(View):

    def get(self, request, *args, **kwargs):
        applicant.get_job_applicant()


class JobApplicantsView(View):
    forms = {
        # 'POST':
    }

    def get(self, request,  *args, **kwargs):
        poster_id = kwargs['id']

        response = applicant.get_applicant(id)

        return JsonResponse(response['data'], status=response['code'])

    @validate_payload
    def post(self, request, *args, **kwargs):
        pass


