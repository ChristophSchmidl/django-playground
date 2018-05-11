from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """
    Test API View.
    """

    def get(self, request, format=None):
        """
        Returns a list of APIView features.
        :param request:
        :param format:
        :return:
        """

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        # Takes a dictionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})