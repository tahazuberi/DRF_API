from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product_edit',
        lookup_field='pk'
        )
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
                
                'url',
                'edit_url',
                'email',
                'pk',
                'title',
                'content',
                'price',
                'sale_price',  
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