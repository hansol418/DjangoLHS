from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger
from lunchMenu.models import LunchMenu


# views - controller 역할.

# 터미널에서, 단위 테스트 연습해보기.
# python
# 입력 후, 모양이 >>>
# from burgers.models import Burger
# 오류 발생하면,
# 다시 터미널에서, ctrl + z
# python manage.py shell
# from burgers.models import Burger
# Burger
# 해당 모델 객체의 목록 모두 가져오기.
# Burger.object.all()

def main(request):
    # 단순 문자열만 리턴,
    # return HttpResponse("Hello, world.")
    # 화면을 연결해서 응답하기.
    return render(request, 'main.html')


def main2(request):
    # return HttpResponse("오늘 점심 뭐 먹지? 듣고 있나요? 듣고만 있나요? ")
    return render(request, 'main2.html')


def burger_list(request):
    # 디비로부터 데이터 가져오기.
    burgers = Burger.objects.all()
    # 1차 확인, 콘솔 확인
    # print(f"전체 햄버거 목록: {burgers}")
    # 데이터를 화면에 전달시, 각각 전달 가능하지만, 하나의 객체에 모두 담아서 보내기
    context = {'burgers': burgers}
    # 화면에 그려주면서, 동시에 데이터도 같이 전달.
    # 주의사항,
    # 화면에서, 타임리프 기억나요? , 해당 데이터 가져올 때,
    # 변수 사용시 기본 문법
    # {{변수명 }} ,
    # 태그 사용시,
    # {% 시작     %}  끝나는 태그
    return render(request, 'burger_list.html',context)


def lunchMenu(request):
    # 디비로부터 데이터 가져오기.
    lunchMenu = LunchMenu.objects.all()
    # 1차 확인, 콘솔 확인
    # print(f"전체 햄버거 목록: {burgers}")
    # 데이터를 화면에 전달시, 각각 전달 가능하지만, 하나의 객체에 모두 담아서 보내기
    context = {'lunchMenu': lunchMenu}
    # 화면에 그려주면서, 동시에 데이터도 같이 전달.
    # 주의사항,
    # 화면에서, 타임리프 기억나요? , 해당 데이터 가져올 때,
    # 변수 사용시 기본 문법
    # {{변수명 }} ,
    # 태그 사용시,
    # {% 시작     %}  끝나는 태그
    return render(request, 'lunchMenu.html',context)