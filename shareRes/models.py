from django.db import models

# Create your models here.

class Category(models.Model):
    #create table 까지는 진행된 상태
    category_name = models.CharField(max_length=100)
    #varCaar(100)인 category_name 컬럼을 생성하게 된다
    #기본키 필드 명시가 없으면 기본키는 자동으로 생성된다
class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=8)
    #foreignkey 설정(카테고리를 삭제하면 기본 카테고리로 설정)
    restaurant_name = models.CharField(max_length = 100) #맛집 이름
    restaurant_link = models.CharField(max_length = 500) #맛집 URL
    restaurant_content = models.TextField() # 맛집 설명
    restaurant_keyword = models.CharField(max_length = 50) #키워드
