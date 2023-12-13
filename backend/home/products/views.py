from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissions] #give certain permissions to the person who can access the records
    # authentication_classes = [authentication.SessionAuthentication,TokenAuthentication] #allow who can access the records

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user=request.user)
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffEditorPermission]

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # def perform_update(self,serializer):
    #     instance = serializer.save()
    #     if not instance.content:
    #         instance.content = instance.title

class ProductDeleteApiView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductListMixinView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request):
        return self.list(request)