from django.contrib import admin
from django.urls import path, include
from . import views


applicant_urls = [
    path('applicant', views.JobApplicantsView.as_view()),
    path('applicant/signup', views.ApplicantSignup.as_view()),
    path('applicant/login',views.ApplicantLogin.as_view()),
    path('applicant/{id}', views.JobApplicantView.as_view()),

]

poster_urls = [

]

all_urls = applicant_urls + poster_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('v1/', include(all_urls))
]


