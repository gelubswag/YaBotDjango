from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from rest_framework import status, response, request
from requests import request as external_request
from .data_handler import *
from json import loads as json_loads


class ExternallRequest(APIView):
    def post(self, request: request.Request):
        if not request.data:
            data = {"message": yandex_data_handler("null_msg")}
        else:
            data = {"message": yandex_data_handler(request.data)}

        resp = external_request(
            settings.EXTERNAL_API_METHOD, settings.EXTERNAL_API_URL, data=data
        )

        return response.Response(resp.json(), status=status.HTTP_200_OK)


class TestRequest(APIView):
    def post(self, request: request.Request):

        data = yandex_response_handler(request.data)

        return response.Response(data=data, status=status.HTTP_200_OK)


# Create your views here.
