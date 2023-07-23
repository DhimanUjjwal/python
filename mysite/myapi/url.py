from django.urls import path
from myapi.views import StudentView


urlpatterns = [
    path('', StudentView.as_view())
]