from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/',views.ProductDetailApiView.as_view(),name='product_detail'),
    path('<int:pk>/update/',views.ProductUpdateApiView.as_view(),name='product_edit'),
    path('<int:pk>/delete/',views.ProductDeleteApiView.as_view()),
    # path('',views.ProductCreateApiView.as_view()),
    path('list/',views.ProductListCreateApiView.as_view(),name='product_list')

]