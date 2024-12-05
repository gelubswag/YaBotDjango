from django.urls import path

app_name = "api"
from .views import ExternallRequest, TestRequest

urlpatterns = [
    path("api/ExternallRequest/", ExternallRequest.as_view(), name="ExternallRequest"),
    path("api/TestRequest/", TestRequest.as_view(), name="TestRequest"),
]
