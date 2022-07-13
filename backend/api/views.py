from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class BoardView(APIView):

    def get(self, request):
        return Response({'message':'Hello World'})