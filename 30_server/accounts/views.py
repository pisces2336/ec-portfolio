from uuid import UUID

from core.models import get_or_404
from core.views import BaseAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Role, User
from .serializers import RoleSerializer, UserSerializer


class RoleCreateListView(BaseAPIView):
    # Create
    def post(self, request: Request):
        seliarizer = RoleSerializer(data=request.data)
        seliarizer.is_valid(raise_exception=True)
        seliarizer.save()
        return Response({"role": seliarizer.data})

    # List
    def get(self, request: Request):
        qs = Role.objects.all()
        seliarizer = RoleSerializer(qs, many=True)
        return Response({"roles": seliarizer.data})


class RoleDetailUpdateDeleteView(BaseAPIView):
    # Detail
    def get(self, request: Request, id: UUID):
        role = get_or_404(Role, id=id)
        seliarizer = RoleSerializer(role)
        return Response({"role": seliarizer.data})

    # Update
    def patch(self, request: Request, id: UUID):
        role = get_or_404(Role, id=id)
        seliarizer = RoleSerializer(instance=role, data=request.data, partial=True)
        seliarizer.is_valid(raise_exception=True)
        seliarizer.save()
        return Response({"role": seliarizer.data})

    # Delete
    def delete(self, request: Request, id: UUID):
        role = get_or_404(Role, id=id)
        role.delete()
        return Response()


class UserCreateListView(BaseAPIView):
    # Create
    def post(self, request):
        role_code = request.data.pop("role_code")
        role = get_or_404(Role, code=role_code)
        request.data["role"] = role.id

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})

    # List
    def get(self, request):
        user_qs = User.objects.select_related("role").all()
        serializer = UserSerializer(user_qs, many=True)
        return Response({"users": serializer.data})


class UserDetailUpdateDeleteView(BaseAPIView):
    # Detail
    def get(self, request, id):
        user = get_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response({"user": serializer.data})

    # Update
    def patch(self, request, id):
        user = get_or_404(User, id=id)

        if role_code := request.data.pop("role_code", None):
            role = get_or_404(Role, code=role_code)
            request.data["role"] = role.id

        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})

    # Delete
    def delete(self, request, id):
        user = get_or_404(User, id=id)
        user.delete()
        return Response()
