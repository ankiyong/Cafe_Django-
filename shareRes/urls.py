from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #http://127.0.0.1:8000/ 요청 처리 -> views파일 내의 index 함수를 통해 요청 처리
    #name은 http://127.0.0.1:8000/을 부르기 위한 별명임
    path('restaurantDetail/',views.restaurantDetail, name='resDetailPage'),
    #http://127.0.0.1:8000/restaurantDetail/ 요청 처리
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    #http://127.0.0.1:8000/restaurantCreate/ 요청 처리
    path('restaurantCreate/create', views.Create_restaurant, name='resCreate'),
    #http://127.0.0.1:8000/restaurantCreate/ 요청 처리
    path('categoryCreate/',views.categoryCreate, name='cateCreatePage'),
    #http://127.0.0.1:8000/categoryCreate/ 요청 처리
    path('categoryCreate/create',views.create_category,name='cateCreate'),
    #http://127.0.0.1:8000/categoryCreate/create/ 요청 처리
    path('categoryCreate/delete',views.Delete_category,name='cateDelete'),
    #http://127.0.0.1:8000/categoryCreate/delete/ 요청 처리

]