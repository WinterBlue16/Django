from django.db import models
from django.utils import timezone # 설정해둔 장소, 시간에 따라 정해짐
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24) # 로또 번호 리스트 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255,
        default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str # 없어도 됨
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

    def generate(self): # 로또 번호를 자동으로 생성함
        self.lottos=""
        origin = list(range(1,46)) # 1~46의 숫자 리스트
        # 6개 번호 set 갯수만큼 1~46 중에서 랜덤으로 6개를 골라 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess=origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n' # 로또 번호 str에 6개 번호 set 추가(??)

        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장 # save를 써주지 않을 경우 DB에 반영되지 않으므로 꼭 써 줄 것!!

    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "pk {}:{} - {}".format(self.pk, self.name, self.text) # pk 자동 생성

# 필기
# CharField == Charactor Field(열에 담기는 데이터 타입 지정 등 종류 많음)
