from django.urls import path,include
from rest_framework import routers
from . import views

app_name='shop'

router=routers.DefaultRouter()
router.register('categories',views.CategoryViewSet)
router.register('products', views.ProductViewSet)

urlpatterns=[
    #path('categories/', views.CategoryListView.as_view(), name='category_list'),
    #path('categories/<pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('', include(router.urls)),
]


