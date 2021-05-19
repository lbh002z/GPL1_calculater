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

#오차율
def ROE() :
    t_value, r_value = input("이론값 실험값 :").split()
    t_value = float(t_value); r_value = float(r_value)
    roe = abs(t_value - r_value) / t_value * 100
    print("오차율 =",roe)
    
#실험3(벡터합 + phi)
def ex3() :
    a, b, theta = input("벡터A 벡터B 사이각(도) 입력 :").split()
    a = float(a); b = float(b); theta = float(theta) * pi / 180
    r = sqrt(a ** 2 + b ** 2 + 2*a*b*cos(theta))
    phi = atan((b * sin(theta))/(a + b * cos(theta))) / pi * 180
    print("|r| = %.2f" %r) 
    print("phi = %.2f" %phi)
       
#실험6(구슬 롤러코스터 실험)
def ex6() :
    y = float(input("트랙 끝점의 높이 y(m) :"))
    h = float(input("출발점의 높이 h(m) :"))
    y0 = float(input("트랙 끝점의 높이 y0(m) :"))
    H = float(input("트랙 끝점과 실험대의 거리 H(m) :"))
    th0 = float(input("트랙의 경사각 theta0(도) :")) * pi / 180
    h0 = float(input("출발점의 높이 h0(m) :"))
    R = float(input("원형 트랙의 반경 R(m) :"))
    m = float(input("질량 m :"))
    x = float(input("평균 수평거리 x(m) :"))
    xf = float(input("평균 수평거리 xf(m) :"))
    g = 9.8

    print("\n그림1\n")
    
    vc12 = sqrt(g*x*x/(2*y))
    print('vc실험값 :',vc12)

    vc11 = sqrt(27/7*g*R * 2 - 10/7 * g * h)
    print('vc이론값 :',vc11)

    roe1 = abs(vc12 - vc11) / vc11 * 100
    print('오차율(%) :', roe1)

    E = 1/2*m*(vc11**2 - vc12**2)
    print('에너지 손실 :',E)

    print('h/R 실험값 :',h/R)

    vb12 = sqrt(vc12**2 + 10/7 * g * H)
    print('vb 실험값 :',vb12)

    vb11 = sqrt(27/7 * g * R)
    print('vb 이론값 :',vb11)

    print('\n그림2\n')

    vc22 = sqrt(g*xf*xf/(2*(y + xf*tan(th0))*cos(th0)*cos(th0)))
    print('vc실험값 :',vc22)

    vc21 = sqrt(27/7*g*R * 2 - 10/7 * g * h0)
    print('vc이론값 :',vc21)

    roe2 = abs(vc22 - vc21) / vc21 * 100
    print('오차율(%) :', roe2)

    E = 1/2*m*(vc21**2 - vc22**2)
    print('에너지 손실 :',E)

    print('h0/R 실험값 :',h0/R)

    vb22 = sqrt(vc22**2 + 10/7 * g * H)
    print('vb 실험값 :',vb22)

    vb21 = sqrt(27/7 * g * R)
    print('vb 이론값 :',vb21)

#실험7(물리진자)
def ex7() :
    L = float(input("전체 길이 입력(m) : "))
    h = float(input("중심으로부터의 길이 입력(m) : "))
    g = 9.8

    Tth = 2 * pi * sqrt((L**2 + 12 * h**2)/(12 * g * h))
    print('주기(이론값) :',Tth)
    Tex = float(input("주기(실험값) : "))
    roeT = abs(Tth - Tex) / Tth * 100
    print('오차율(주기) :',roeT)
    g = pi**2 * (L**2 + 12 * h**2)/(3 * Tex**2 * h)
    print('중력가속도(실험값) :',g)
    roeg = abs(g - 9.8) / 9.8 * 100
    print('오차율(g) :',roeg)


#메인
print("종료 : exit")    
while 1:
    func = input("\n기능 선택(평균, 오차율, 실험3, 실험6, 실험7) :")
    if func == 'exit' :
        break
    elif func == "평균" :
        avr()
    elif func == "오차율" :
        ROE()
    elif func == "실험3" :
        ex3()
    elif func == '실험6' :
        ex6()
    elif func == '실험7' :
        ex7()
    else :
        print("없는 기능입니다.")



    
