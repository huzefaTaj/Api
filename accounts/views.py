import profile
from django.shortcuts import render
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,ProfileSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from accounts.models import Profile
from rest_framework.decorators import api_view

# Register
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


#login
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

#profile
@api_view(['GET', 'POST', 'DELETE'])
def profile_list(request):
    # Get Profile 
    if request.method == 'GET':
        profile = Profile.objects.all()
        
        user = request.query_params.get('user', None)
        if user is not None:
            profile = profile.filter(user__icontains=user)
        
        profile_serializer = ProfileSerializer(profile, many=True)
        return JsonResponse(profile_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    
    #Post profile
    elif request.method == 'POST':
        profile_data = JSONParser().parse(request)
        profile_serializer = ProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse(profile_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete Profile
    elif request.method == 'DELETE':
        count = Profile.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    try: 
        profile = Profile.objects.get(pk=pk) 
    except Profile.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        profile_serializer = ProfileSerializer(profile) 
        return JsonResponse(profile_serializer.data) 
 
    elif request.method == 'PUT': 
        profile_data = JSONParser().parse(request) 
        profile_serializer = ProfileSerializer(profile, data=profile_data) 
        if profile_serializer.is_valid(): 
            profile_serializer.save() 
            return JsonResponse(profile_serializer.data) 
        return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        profile.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
