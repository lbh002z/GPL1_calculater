#일반물리실험 계산기

from math import *

#평균
def avr() :
    sum = 0
    list1 = input("수를 입력 :").split()
    for i in list1 :
        i = float(i)
        sum += i
    avr = sum / len(list1)
    print("평균 =",avr)
    
#벡터합
def vector() :
    a, b, theta = input("벡터A 벡터B 사이각(도) 입력 :").split()
    a = float(a); b = float(b); theta = float(theta) * pi / 180
    r = sqrt(a ** 2 + b ** 2 + 2*a*b*cos(theta))
    print("|r| =",r)
    
#phi(A와 R사이의 각)
def phi() :
    str1 = input("벡터A 벡터B 사이각(도) 입력 :")
    A, B, theta = str1.split()
    A = float(A); B = float(B); theta = float(theta) * pi / 180

    phi = atan((B * sin(theta))/(A + B * cos(theta))) / pi * 180
    print("phi =",phi)

#오차율
def ROE() :
    t_value, r_value = input("이론값 실험값 :").split()
    t_value = float(t_value); r_value = float(r_value)
    roe = abs(t_value - r_value) / t_value * 100
    print("오차율 =",roe)

#메인
print("매주 기능을 늘릴 예정입니다. ui도 만들 예정입니다")    
func = input("기능 선택(평균, 벡터합, phi, 오차율) :")
if func == "평균" :
    avr()
elif func == "벡터합" :
    vector()
elif func == "phi" :
    phi()
elif func == "오차율" :
    ROE()
else :
    print("없는 기능입니다.")


    
