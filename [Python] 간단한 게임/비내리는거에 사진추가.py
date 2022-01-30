import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
raindrop_spawn_time = 0
mike_umbrella_image = pygame.image.load("사진위치 c:/블라블라").convert() #image.load는 이미지를 가져오고 
                                                                                #convert가 그 이미지를 그래픽카드가 읽을수 있는 포맷으로 바꿔줌


class Raindrop:     #class이름은 대문자로 시작함
    def __init__(self):     #class의 첫 함수는 반드시 __init__으로 시작해야함, self는 더 알아보기
        self.x = random.randint(0,1000)
        self.y = -5
        self.speed = random.randint(5,18) #떨어지는 속도를 5~18 사이 랜덤으로

    def move(self):
        self.y += self.speed #랜덤속도로 떨어짐, 13줄참고

    def off_screen(self): #self.y가 800을 넘어갔는지 true false를 알려줌
        return self.y > 800

    def draw(self):     #보통 draw함수같은걸 가장 마지막에 쓴다는데 이유가ㅏ 있겠지?
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+5),1)

    
class Mike:
    def __init__(self):
        self.x = 300
        self.y = 400
    def draw(self):
        screen.blit(mike_umbrella_image,(self.x,self.y)) #screen.blit은 전송될 개체와 좌표를 갖는다 개체는 이미지,좌표는 xy

raindrops = []  #raindrop들로 이 리스트가 채워진다함(27줄) 보통 리스트는 class이름에 s를 붙여 복수형으로 이름지음
mike = Mike() #마이크를 부르는 인스턴스 마이크 나와!!!
while True:
    clock.tick(60)  #이거 안쓰면 비가 엄청 빨리 떨어짐
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    raindrops.append(Raindrop())    #비를 두배로 오게하고 싶으면 이 줄을 복붙
    screen.fill((255,255,255))
    mike.draw() #마이크 소환!!!
    #for raindrop in raindrops:  #class의 단수형에 소문자로
        #raindrop.move()
        #raindrop.draw()    밑에 while문이 이 역할을 대신함
    
    i = 0
    while i < len(raindrops):             #아 이해했다 제일큰 while true루프를 돌고 다시 내려와서 raindrops 리스트 안에 있는 숫자만큼 다시 i가 올라가는거임 아 드디어
        raindrops[i].move()
        raindrops[i].draw()
        if raindrops[i].off_screen():
            del raindrops[i]
            i -= 1
        i += 1

    pygame.display.update()
