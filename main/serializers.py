from rest_framework import serializers
from . import models


class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password1')
        user = models.CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Revenue
        fields = '__all__'


class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expenditure
        fields = '__all__'
