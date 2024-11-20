from django import forms

from users.models import User


class UserCreationForm(forms.ModelForm):
    # 비밀번호 입력 필드 정의
    # widget = forms.PasswordInput : 입력 시 문자가 가려지는 비밀번호 입력 위젯 사용
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)


    class Meta:
        # 이 폼이 사용할 Django 모델 지정
        model = User
        # 폼에서 편집 가능한 필드 명시
        fields = ("user_name", "email")


    def clean_password2(self):
        # cleaned_date : 폼 유효성 검사 후 정제된 데이터를 담은 딕셔너리
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        # 두 비밀번호가 모두 입력되었고 서로 다를 경우 예외 발생
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        # 검증 통과 시 password2 반환
        return password2

    def save(self, commit=True):
        # super().save(commit=False) : 데이터베이스에 즉시 저장하지 않고 객체만 생성
        user = super().save(commit=False)
        # set_password : 비밀번호를 안전하게 해시화하여 저장
        user.set_password(self.cleaned_data["password1"])
        if commit:
            # 데이터베이스에 최종 저장
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        # 이 폼이 사용할 Django 모델 지정
        model = User
        # 사용자가 수정 가능할 필드 명시
        fields = ("user_name", "email")
