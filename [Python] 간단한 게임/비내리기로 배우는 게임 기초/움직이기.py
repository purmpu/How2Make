import pygame, sys
from pygame.locals import *
pygame.init()    #파이게임을 초기화 시킨다
screen = pygame.display.set_mode((640,480))     #게임 화면을 너비높이 640,480으로 설정
xpos = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #9~10줄은 창 닫기를 의미.
            sys.exit()  #프로그램 종료
    xpos += 1
    screen.fill((255,255,255))  #RGB코드
    pygame.draw.circle(screen,(0,255,0),(xpos,200),20)   #screen 뒤에 인자들 순서대로 circle의 색상,원의 중심위치,반지름,테두리의 두께
    pygame.display.update()   
