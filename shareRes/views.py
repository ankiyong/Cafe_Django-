from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

def index(request):
    #기존에 입력되어 있는(혹은 새로 입력한) 카테고리 내용을 db에서 select 함
    categories = Category.objects.all() #select 진행 후 결과를 반환
    #반환된 결과를 categories에 담았음
    #rendering에 사용할 dict로 구성
    content = {'category':categories}
    #구성된 dict를 rendering에 가용하도록 전달달
    return render(request,'shareRes/index.html',content)
    #요청한 클라이언트 에게 , shareRes디렉토리 밑의 index.html을 보여준다
    #누가 이 요청을 불렀는지에 대한 클라이언트 정보(request)
    #요청에 응답하여 보여줄 html파일 shareRes/index.html
    # return HttpResponse('index')
    #요청에 의한 응답을 확인하기 위해 진행

def restaurantDetail(request):
    return render(request,'shareRes/restaurantDetail.html')
    # return HttpResponse('restaurantDetail')

def restaurantCreate(request):
    return render(request, 'shareRes/restaurantCreate.html')
    # return HttpResponse('restaurantCreate')

def categoryCreate(request):
    return render(request, 'shareRes/categoryCreate.html')
    # return HttpResponse('categoryCreate')

def create_category(request):
    # 사용자가 입력한 category data를 추출해서 db에 저장한다
    #1. 사용자가 입력한 category data를 추출(post방식으로 서버에 전송됨)
    category_name = request.POST['categoryName']
    # db저장 후 index.html파일을 재요청
    new_category = Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    #index url(기본페이지) 요청
    # return HttpResponse('create_category')