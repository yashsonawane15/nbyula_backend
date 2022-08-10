from django.views import View
from django.http import JsonResponse
from .db import applicant

class JobApplicant(View):

    def get(self, request,  *args, **kwargs):
        poster_id = kwargs['id']

        response = applicant.get_applicant(id)

        return JsonResponse(response['data'], status=response['code'])


    def post(self, request, *args, **kwargs):
        pass


