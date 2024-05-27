from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
from .models import CustomUser
from .serializers import LoginSerializer, UserSerializer, TutorRegisterSerializer, StudentRegisterSerializer

class TutorRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TutorRegisterSerializer
    permission_classes = (permissions.AllowAny,)

class StudentRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = StudentRegisterSerializer
    permission_classes = (permissions.AllowAny,)

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            user_data = UserSerializer(user).data
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data  # Include user data in the response
            })
        return Response(serializer.errors, status=400)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return redirect('/')
        except Exception as e:
            return Response(status=400)

class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
