from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from uploader_app.serializers import UserSerializer, GroupSerializer, UploadedFileSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from uploader_app.serializers import UploadedFileSerializer
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from uploader_app.models import UploadedFile
from minio import Minio


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST'])
def UploadedFile_list(request):
    if request.method == 'GET':
        user = request.user
        uploadedfiles = UploadedFile.objects.filter(current_user=user)
        serializer = UploadedFileSerializer(uploadedfiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def UploadedFile_detail(request, pk):
    user = request.user
    try:
        uploadedfile = UploadedFile.objects.filter(user=user).get(pk=pk)
    except uploadedfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UploadedFileSerializer(uploadedfile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UploadedFileSerializer(uploadedfile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user = request.user
        uploadedfile = UploadedFile.objects.filter(user=user).get(pk=pk)
        serializer = UploadedFileSerializer(uploadedfile, data=request.data)
        client = Minio(
            "192.168.1.3:9000",
            access_key="ZymyA122eYprF67X",
            secret_key="BU8xsQjEF90wItAGA4YJS0ETSV0gpft1",
            secure=False,
        )
        # Remove object.
        client.remove_object("uploadedfiles", uploadedfile[0].file_name)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


for user in User.objects.all():
    Token.objects.get_or_create(user=user)
