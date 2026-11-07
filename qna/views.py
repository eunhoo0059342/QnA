from django.shortcuts import render, redirect
# from 파일 위치
from .models import Question


# Create your views here.

# view 열결할 함수 만들기
# def 함수이름(request):
#   return render(request, "파일경로")  -> html 그리기!

def main(request):
    # 질문게시글을 전체를 불러오기 -> DB
    # 모델이름.objects.all() 
    db = Question.objects.all()
    
    # 데이터를 html에다가 응답 Response를 하고 싶다. => 딕셔너리(JS에서는 json)형태로 전달
    # 딕셔너리 = {
    #  '전달할 데이터이름': 전달할 데이터
    # }
    dict = {
        'data':db
    }

    # 찐 전달하기
    # retrun render(request, "처리할 Html경로", 응답할 딕셔너리)

    return render(request, 'qna/index.html', dict)







def write(request):
    return render(request, "qna/write.html")

# 우리만든 POST받았다면 Question 모델에 데이터를 생성하기
# - 새로 만들기 => render
# - 다 만든 후에는 메인페이지로 이동하자. => redirect('url별칭')
def create(request):
    if request.method == 'POST':
        # 인스턴트(객체) 생성하기
        # 인스턴스명.속성명 = 저장할 데이터
        
        # form태그에서 전달받은 데이터(request.POST)는 딕셔너리형태로 전달받는다.
        # request.POST <-딕셔너리

        # d={"one":"일","two":"이","three":"삼"}
        # d에서 one값을 꺼내기
        # d['one']
        # d.get("one")

        new_q = Question()

        new_q.title = request.POST['title']
        new_q.writer = request.user         # 사용자를 개발자도구에서 마음대로 수정하면 안되니깐
        new_q.text = request.POST['text']
        new_q.views=0

        # DB에 저장하기 Save
        new_q.save()
        return redirect('write')