from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from myapp.permissions import IsManager, IsEmployee


# Create your views here.
class HelloAPI(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        data = {
            'message': 'HEllo django'
        }

        return Response(data)


@api_view(["GET"])
@permission_classes([IsAuthenticated, ])
def hello_drf(request):
    data = {
        "message":"hi my django"
    }
    return Response(data)


class HelloRole(APIView):
    permission_classes = [IsManager, ]

    def get(self, request):
        data = {
            'message': 'HEllo Manager'
        }

        return Response(data)


class HelloRole2(APIView):
    permission_classes = [IsEmployee, ]

    def get(self, request):
        data = {
            'message': 'HEllo Employee'
        }

        return Response(data)