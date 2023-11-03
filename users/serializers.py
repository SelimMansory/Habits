from rest_framework import serializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user