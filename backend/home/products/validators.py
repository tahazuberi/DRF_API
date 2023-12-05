
from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

def validate_title(value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} Already Exists")
        return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(),lookup='iexact')