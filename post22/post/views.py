from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer,UserLoginSerializer,PostSerializer,IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login,logout
from django.http import JsonResponse


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def logoutAPI(request):
    logout(request)
    response_data = {'message': 'Logged out successfully.'}
    return JsonResponse(response_data)


class AllPostAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer
    permission_classes = [IsAuthenticated]


class CreatePostAPI(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class UpdateAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
