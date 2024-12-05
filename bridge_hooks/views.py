from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests


class AccountView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DestinationView(APIView):
    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomingDataView(APIView):
    def post(self, request):
        secret_token = request.headers.get('CL-X-TOKEN')
        if not secret_token:
            return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            account = Account.objects.get(app_secret_token=secret_token)
        except Account.DoesNotExist:
            return Response({"message": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        for destination in account.destinations.all():
            headers = destination.headers
            method = destination.http_method
            url = destination.url

            if method == 'GET':
                response = requests.get(url, params=data, headers=headers)
            else:
                response = requests.request(method, url, json=data, headers=headers)

        return Response({"message": "Data sent to destinations"}, status=status.HTTP_200_OK)
