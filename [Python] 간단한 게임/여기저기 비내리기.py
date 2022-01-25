import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
rain_y = 0
rain_x = random.randint(0,1000)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    rain_y += 4     #직선은 밑으로 계속 떨어져야 하니깐
    pygame.draw.line(screen,(0,0,0),(rain_x,rain_y),(rain_x,rain_y+5),1)    #screen은 line이 그려질 장소, 0,0,0은 색상(rgb), 1은 직선두께
                                                                            #rain_x rain_y는 직선 시작장소, rain_y+5는 직선 끝나는 장소

    pygame.display.update()
    
 
여기까지는 이해가 되는데 다음장인 빗방울지우기 코드 추가하기에서 부터 아무것도 이해가 안됨 흑흑
