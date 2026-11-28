# 가상환경 활성화
venv/Scripts/activate



# 회원 만들어서 QnA사이트를 만들기

# 프로젝트 초기 셋팅
## 1. 회원을 관리할 App생성하기
django-admin startapp account

## 2. config/settings 설정
### (1) 내가 사용할 앱 등록
```python
INSTALLED_APPS = [
    'django.contrib.admin',             # 어드민
    'django.contrib.auth',              # 회원-인증
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # '생성한 app이름', <- 쉼표 잊지말고 꼭 쓰기(나중에 안까먹어요.)
]
```

### (2) template 셋팅
1. 프로젝트 폴더/templates 폴더를 생성하기

2. settings.py에서 templates 경로 설정
```python
import os  # 맨위에
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 프로젝트의 templates 폴더를 템플릿 경로로 등록
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        ...
    },
]
```

### (3) static 셋팅
1. 프로젝트폴더/static 폴더를 생성하기

2. settings.py에서 static 경로 설정
```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR
```

### (4) UTC(국제 표준시)
 - 한국은 UTC +9
```python
TIME_ZONE = 'Asia/Seoul'
```



# Django Admin(관리자)
: 내가 직접 만든게 아니라 Django에서 admin기능을 제공한다.

(회원 권한)
- 일반 회원
- 일반 관리자
- 최고 관리자 => superuser


## 1. 장고의 user을 생성하기 => django가 이미 만들어 놨음
(원래)
python manage.py makemigrations >> 내가 만든 모델의 틀생성
python manage.py migrate

(장고기능을 사용할땐)
python manage.py migrate



## 2. 장고 최고관리자 superuser 생성하기
python manange.py createsuperuser
>> username : 아이디 정하기 보통은 admin
>> email : 이메일은 아무거나 
>> password : 1234
>> y

db.sqlite3에 auth_user에 추가되는게 보임

### 3. 장고어드민 로그인해보기
http://127.0.0.1:8000/admin/
username : admin
password : 1234

username : apro_p
password : apro1234

username : tester1
password : 코딩1234



# 로그인/로그아웃 구현하기
- account App에서 url 생성해서 하기

로그인 url : /account/login
로그아웃 url: /account/logout

## 1. config/urls.py 에서 App별 url을 만들어주기
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'))
]
```

## 2. account/urls.py에서 로그인/로그아웃 url만들기
```python
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns=[
    path("login", auth_views.LoginView.as_view(template_name="account/login.html"), name="login" )
]

```

## 3. account/login.html 생성하기
- 아이디를 입력하고 패스워드를 입력 => form태그

```html

<form action="{% url '앱이름:url별칭' %}" method="POST">
    {% csrf_token %}  <- 안넣으면 보안이슈 POST로 안넘어감 
    <div>
        <label for="username">사용자ID</label>
        <input type="text" name="username" id="username"
            value="{{ form.username.value | default_if_none:'' }}">
    </div>
    <div>
        <label for="password">비밀번호</label>
        <input type="password" name="password" id="password"
            value="{{ form.password.value | default_if_none:'' }}">
    </div>
    <button type="submit">로그인</button>

</form>

```


## 4. 로그인 후 이동할 url 정하기(config/urls.py)
```python
LOGIN_REDIRECT_URL = "/"


```


## 5. 로그인 되어있는지 체크하기
- 유저의 인증을 체크하기
```
{% if user.is_authenticated %}  
    <!-- 로그인 된 html -->

{% else %}
    <!-- 로그인 안된 html -->

{% end if %}

```



# Git으로 버전 관리하기
### 1. 로컬(내컴퓨터) 저장소 만들어야한다.
```
git init
```

### 2. .gitignore 파일 생성하기 
: git이 특정파일은 무시할수 있도록 설정하는 파일
git에 불필요한 정보는 저장하지 않도록 하기
https://gitignore.io


3. 저장할 내용을 선택하기
```
git add . 
git add 파일/디렉토리명
```

4. git 상태 확인하기
```
git status 
```

5. 저장할 내용을 선택을 해제하기
```
git add . 
```
git reset 파일/폴더

6. 진짜 저장하기 
git commit -m "한줄메세지"
추천메세지 first init
        project init

git commit
- 리눅스 파일을 작성하는 화면(마우스는 안통하고, 키보드로만 가능)
- 'i' insert모드 작성하기
- 맨첫줄은 제목  - 내가 만든 기능에 대한 제목  (기능만들때느 feat: 제목)
- 두번줄은 줄바꿈
- 세번째줄에서 본문 - 내가 만든 기능에 대한 자세한 설명 '/account/login' url 접속시 로그인하거나 로그인 되면 로그인완료됨 메세지 띄우기
- '#' 주석 : 무시
- esc키 누르고 ':wq' (w: 작성하고 q: 종료)


7. git 히스토리 보기
git log

8. github 원격저장소에 저장하기
git remote add origin ~~~
git push origin main




# question 질문 모델을 생성하기 => ORM
- 클래스명은 모든 단어의 앞에 대문자 PascalCase
- 단순객체가 아니고 db랑 연결할 객체

from django.contrib.auth.models import User

class 모델이름(models.Model):
    작성자 : 유니크한(고유한) id값으로 회원DB정보랑 연결하기 => DB를 전문적으로 공부하면 좀더 자세하기 알수가 있어요.
    # - 작성자 : 로그인한 유저로 자동으로 입력되게하기 
        #         => User모델과 연결 key(보통 id값) 
        #         => ForeignKey(모델명, related_name="User작성될 컬러명" , on_delete=삭제정책(models.CASCADE / SET_NULL))
    writer = models.ForeignKey(User, related_name='writer_questions')

