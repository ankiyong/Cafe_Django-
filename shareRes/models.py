from django.db import models

# Create your models here.

class Category(models.Model):
    #create table 까지는 진행된 상태
    category_name = models.CharField(max_length=100)
    #varCaar(100)인 category_name 컬럼을 생성하게 된다
    #기본키 필드 명시가 없으면 기본키는 자동으로 생성된다
