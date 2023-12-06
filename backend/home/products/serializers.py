from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from . import validators 

class InLineProductSerializer(serializers.Serializer):
        other_product_url = serializers.HyperlinkedIdentityField(
        view_name='product_detail',
        lookup_field='pk'
        ) 
        title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    # related_products = InLineProductSerializer(source='user.product_set.all',read_only=True,many=True)
    owner = UserPublicSerializer(source='user',read_only=True);
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product_edit',
        lookup_field='pk'
        )
    email = serializers.EmailField(write_only=True)
    title  = serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    class Meta:
        model = Product
        fields = [
                'owner',
                # 'user', #represents user id
                'url',
                'edit_url',
                'email',
                'pk',
                'title',
                'content',
                'price',
                'sale_price',  
                # 'related_products'
                  ]
    



    def create(self,validated_data):
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        print(email)
        return obj

    def get_url(self,obj):
      request= self.context.get('request')
      if request is None:
          return None
      return reverse('product_detail',kwargs={"pk":obj.pk},request=request)