from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def get_data(request):
    header = {"Access-Control-Allow-Origin":"*"}
    data = {"slackUsername": "emperordivo", "backend": True, "age": 23, "bio": "Am an Engineering student and budding fullstack developer" }
    return JsonResponse(data, headers=header)
