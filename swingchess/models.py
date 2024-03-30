import psycopg2
from django.db import models
from django.contrib.auth.models import User
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from rest_framework_jwt.settings import api_settings


class members(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        app_label = 'swingchess'


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()


class SingleTonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingleTonModel, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        pass

    #############


@csrf_exempt
@require_http_methods(["GET"])
def check_id(request):
    byte_data = request.body
    string_data = byte_data.decode('utf-8')
    data = json.loads(string_data)
    username = data['username']
    try:
        User.objects.get(username=username)
        return HttpResponse("User already exists", status=409)
    except User.DoesNotExist:
        return HttpResponse("You can use that id", status=200)


@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    byte_data = request.body
    string_data = byte_data.decode('utf-8')
    data = json.loads(string_data)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    print(username, password, email)
    try:
        User.objects.get(username=username)
        return HttpResponse("User already exists", status=400)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password=password, email=email)
        members(user=user, username=username, email=email)
        return HttpResponse("Registered successfully.", status=201)


@csrf_exempt
@require_http_methods(["GET"])
def login(request):
    print(request)
    print(request.body)
    byte_data = request.body
    string_data = byte_data.decode('utf-8')
    data = json.loads(string_data)
    username = data.get('username')
    password = data.get('password')

    try:
        user = authenticate(username=username, password=password)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = JsonResponse({'message': 'Logged in successfully'}, status=200)
        response['Authorization'] = f'Bearer {token}'
        return response
    except User.DoesNotExist:
        return HttpResponse("You are not authorized", status=401)
