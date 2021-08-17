from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

def index(request):
    #기존에 입력되어 있는(혹은 새로 입력한) 카테고리 내용을 db에서 select 함
    categories = Category.objects.all() #select 진행 후 결과를 반환
    restaurants = Restaurant.objects.all()
    #반환된 결과를 categories에 담았음
    #rendering에 사용할 dict로 구성
    content = {'categories':categories,
               'restaurants':restaurants}
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
    # restaurantCreate.html 파일을 rendering 할 때 카테고리 선택을 위한 데이터는 동적으로 추가되도록 코딩
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request, 'shareRes/restaurantCreate.html',content)
    # return HttpResponse('restaurantCreate')

def Create_restaurant(request):
    # 외래키로 연결된 카테고리컬럼은 저장을 일반 값이 아닌 해당 카데고리 레코드의 인스턴스를 넘겨줘야 함
    # 카테고리 id 추출
    category_id = request.POST['resCategory']
    #카테고리 테이블의 레코드 인스턴스 반환
    category = Category.objects.get(id=category_id) # 현 코드에서 생성되는 인스턴스를 db로 전달해야 함
    name = request.POST['resTitle']
    link = request.POST['resLink']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    #맛집 입력 테이블인 Restaurant의 인스턴스를 생성
    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link=link,
                         restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    #저장된 결과를출력하기 위해 index.html파일 요청
    return HttpResponseRedirect(reverse('index'))

def categoryCreate(request):
    categories = Category.objects.all()
    #categories 변수에는 Category 테이블의 모든 레코드를 반환받아서 저장
    #Category 테이블 컬럼 : id, category_name
    content = {'categories':categories}
    return render(request, 'shareRes/categoryCreate.html',content)
    # return HttpResponse('categoryCreate')

def create_category(request):
    # 사용자가 입력한 category data를 추출해서 db에 저장한다
    #1. 사용자가 입력한 category data를 추출(post방식으로 서버에 전송됨)
    category_name = request.POST['categoryName']
    # db저장 후 index.html파일을 재요청
    new_category = Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index')) #index url(기본페이지) 요청
    # return HttpResponse('create_category')

def Delete_category(request):
    category_id=request.POST['categoryId'] #각 카테고리의 id롤 보여주는 hidden 태그
    #레코드 삭제
    #해당 레코드 가져오기
    delete_category = Category.objects.get(id=category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

