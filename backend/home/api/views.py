from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST"]) ##drf api view
def api_view(request):
        # instance = Product.objects.all().order_by("?").first()
        # data = {}
    serializer  = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # data['id'] = model_data.id        models instance into py dict(long method)
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        # data = model_to_dict(model_data,fields=['title','content','price','sale_price'])    #short method
        # data = ProductSerializer(instance).data  

        # data = serializer.save()
        # print(data)
        print(serializer.data)
    return Response(serializer.data)

 # print(request.GET) # url query parameters
    # body = request.body
    # data = {}

    # try:
    #     data = json.loads(body) ##json data into py dict
    # except:
    #     pass
    # print(data)


    # data['params'] = dict(request.GET) 
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type