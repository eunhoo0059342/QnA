from django.urls import path
# from 폴더위치 import 파일
from . import views

# account.urls 파일도 동일하게 작성
# path("url",views.연결할함수, name="url별칭")
urlpatterns = [
    # 메인페이지 -> 아무것도 안적어도 바로 접속 
    path('', views.main, name='main'),
    path('write', views.write, name='write'),
    path('a', views.create, name='create'),
]