from urllib import request
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from uploader_app.models import UploadedFile
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UploadedFileSerializer(serializers.HyperlinkedModelSerializer):
    # Create a custom method field
    class Meta:
        model = UploadedFile
        fields = ['id', 'file_name', 'file_size', 'file_type', 'file']

        