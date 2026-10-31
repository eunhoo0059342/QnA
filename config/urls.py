"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 전체적인 프로젝트에서 관리하는 url
# 우리의 정책 - 앱별로 urls.py를 따로 관리하기로 했다.

urlpatterns = [
    #장고에서 제공하는 기능
    path('admin/', admin.site.urls),
    # account앱(회원,로그인)에서 url를 관리 => include
    path('account/', include('account.urls')),
    # qna앱(질문게시판 - 메인)에서 url를 관리 => include
    # 메인페이지는 도메인까지만 입력해도 바로 화면 떠야한다. => Url를 ""로 만들기
    path('', include('qna.urls'))

]
