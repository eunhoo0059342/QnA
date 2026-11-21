from django.contrib import admin
from .models import Question, Answer

# Register your models here.
# qna 앱에서 설정하고 싶은 admin 설저을 여기다가 하기
# admin에 questions 모델을 볼수 있도록 등록하기
# admin.site.register(모델이름)
admin.site.register(Question)
admin.site.register(Answer)