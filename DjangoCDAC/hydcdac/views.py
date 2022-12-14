from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import rest_framework
from .dbrelateddata import package_name_extract

class GetDatabase(APIView):
    def get(self, *args, **kwargs):
        get_resp={"status":200}
        get_pack=self.kwargs.get("packagename")
        get_resp["data" ]= package_name_extract(get_pack)
        print(get_resp["data"])
        return Response(get_resp, status=status.HTTP_200_OK)


