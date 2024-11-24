from accounts.models import User
from core.constants import RoleCode
from core.models import get_or_404
from core.views import BaseAPIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer


class ItemCreateListView(BaseAPIView):
    # Create
    def post(self, request):
        # スタッフユーザーのみ商品を作成できる
        user: User = request.user
        if user.role.code != RoleCode.STAFF:
            raise PermissionDenied

        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"item": serializer.data})

    # List
    def get(self, request):
        qs = Item.objects.all()
        serializer = ItemSerializer(qs, many=True)
        return Response({"items": serializer.data})


class ItemDetailUpdateDeleteView(BaseAPIView):
    # Detail
    def get(self, request, id):
        item = get_or_404(Item, id=id)
        serializer = ItemSerializer(item)
        return Response({"item": serializer.data})

    # Update
    def patch(self, request, id):
        item = get_or_404(Item, id=id)
        serializer = ItemSerializer(instance=item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"item": serializer.data})

    # Delete
    def delete(self, request, id):
        item = get_or_404(Item, id=id)
        item.delete()
        return Response()
