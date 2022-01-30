import pygame, sys
from pygame.locals import *
pygame.init()    #파이게임을 초기화 시킨다
pygame.display.set_caption("First Program")     #게임 화면 윗부분에 뜨는 이름
screen = pygame.display.set_mode((640,480))     #게임 화면을 너비높이 640,480으로 설정
xpos = 50
ypos = 200
clock =pygame.time.Clock()  #while문이 도는 루프를 설정하는거라는데 실질적으로 disply update 속도를 조절하는거니 프레임이라고 봐도 되는건가?
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #9~10줄은 창 닫기를 의미.
            sys.exit()  #프로그램 종료
    pressed_keys = pygame.key.get_pressed() #pygame.key.get_pressed()는 키보드의 모든 키와 키눌림 여부를 리스트로 만든다
    if pressed_keys[K_RIGHT]:
        xpos += 1
    if pressed_keys[K_LEFT]:
        xpos += -1
    if pressed_keys[K_UP]:
        ypos += -1
    if pressed_keys[K_DOWN]:
        ypos += 1
    screen.fill((255,255,255))  #RGB코드
    pygame.draw.circle(screen,(0,255,0),(xpos,ypos),20)   #screen 뒤에 인자들 순서대로 circle의 색상,원의 중심위치,반지름,테두리의 두께
    pygame.display.update()   
