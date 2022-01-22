#일단 책을 따라하기. 따라하다 보면 내가 찾아보거나 ㅐㅎ서 알게되겠지

import pygame, sys
from pygame.locals import *
pygame.init()    #파이게임을 초기화 시킨다
screen = pygame.display.set_mode((640,480))     #게임 화면을 너비높이 640,480으로 설정
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #9~10줄은 창 닫기를 의미. 창 우측상단의 x아이콘이 pygame 에서 QUIT이라는 이름이라는듯
            sys.exit()  #프로그램 종료
    screen.fill((255,255,255))  #RGB코드
    pygame.draw.circle(screen,(0,255,0),(100,200),20,5)   #screen 뒤에 인자들 순서대로 circle의 색상,원의 중심위치,반지름,테두리의 두께
    pygame.display.update()     #while루프를 도는동안 일어나는 변화들일 display에 표시함. 말그대로 update


#pygame.draw.rect(screen,(0,255,0),(100,100,40,30) 원이 아닌 직사각형일때는 100,100이 왼쪽 위 꼭짓점의 위치, 가로세로의 길이.
