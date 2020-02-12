from django import forms
from lotto.models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 사용자로부터 form을 통해 입력받을 데이터
