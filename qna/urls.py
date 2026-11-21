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
    # 상세페이지url 생성하기 -> 갈때 어떤 게시글 id값(고유값)을 같이 넘겨주기/
    # qna/detail/<int:id변수이름>
    path('qna/detail/<int:q_id>', views.detail, name='detail'),
    path('delete/<int:q_id>', views.delete, name='delete'),   
    # 수정페이지로 가는 url 생성하기
    path('edit/<int:q_id>', views.edit, name='edit'),
    # DB를 수정하는 url를 생성하기
    path('update/<int:q_id>', views.update, name='update'),
    
]