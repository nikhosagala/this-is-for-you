from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message='Email sudah terdaftar')]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    def get_email(self, obj):
        return obj.email

    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        return instance

    def create(self, validated_data):
        pass
