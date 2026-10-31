from django.db import models
from django.contrib.auth.models import User

# https://kin.naver.com/qna/detail.naver?d1id=1&dirId=10303&docId=495335812
# 질문
# - 작성자(로그인, 회원아이디)
# - 제목 : CharField
# - 내용 : TextField
# - 조회수 : IntegerField
# - 생성일자 created_at: 날짜시간 데이터 DateTimeField(auto_add_now=True)
# - 수정일자 

class Question(models.Model):
    # 특정 회원이 작성자다 라고 연결할수 있는 정보 = key(고유값, unique)
    # 내 질문테이블이랑 유저랑 key연결하기
    # on_delete 옵션
    # - 유저가 삭제될때 정책적으로 정해야하는것 : (1) models.CASCADE : 유저가 탈퇴하면 게시글이 사라진다. cascade
    #                                   (2) models.SET_NULL : 유저가 탈퇴하면 게시글은 남대신 유저 정보를 날리는 방향 null -> set_null (카톡 알수없음)
    # 기본적으로 컬럼은 null 허용하지 않는다. => null허용하고 싶으면 설정 null=True
    writer = models.ForeignKey(User, related_name='writer_questions', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    text = models.TextField()
    views = models.IntegerField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table: 이름 직접 정하기
        db_table = 'q'
        # 어드민에서 테이블 다룰때 쓰는 명칭을 직접 정할수 있다.
        # - 단수랑 복수를 은근히 잘 따져요.
        # - 단수명칭 정할수 있고    verbose_name
        # - 복수명치도 정할 수 있다. verbose_name_plural
        verbose_name = '질문'
        verbose_name_plural = '질문 리스트'
        