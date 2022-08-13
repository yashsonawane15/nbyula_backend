from django.contrib import admin
from django.urls import path, include
from . import views


applicant_urls = [
    path('applicant', views.JobApplicantsView.as_view()),
    path('applicant/signup', views.ApplicantSignup.as_view()),
    path('applicant/login',views.ApplicantLogin.as_view()),
    path('applicant/listings', views.ApplicantListings.as_view()),
    path('applicant/apply', views.ApplyJob.as_view()),
    path('applicant/applied', views.ApplicantJobs.as_view()),
    path('applicant/<id>', views.JobApplicantView.as_view()),
    path('applicant/applied/<userid>', views.AppliedJobsView.as_view())

]

poster_urls = [

]

all_urls = applicant_urls + poster_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('v1/', include(all_urls))
]


