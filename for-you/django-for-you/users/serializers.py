from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all(), message='Email sudah terdaftar')]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')


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
        instance.save()
        return instance

    def create(self, validated_data):
        pass
