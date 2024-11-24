from rest_framework import serializers

from .models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    role_code = serializers.SerializerMethodField()

    def get_role_code(self, instance: User):
        return instance.role.code

    def create(self, validated_data):
        instance = User(**validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

    def update(self, instance: User, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        if password := validated_data.pop("password", None):
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = "__all__"
