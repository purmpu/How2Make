import pygame, sys, random, time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("rain")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
raindrop_spawn_time = 0
last_hit_time = 0 #이미지가 마지막으로 비맞은 횟수

mike_umbrella_image = pygame.image.load("C:/Users/sehwa/Desktop/picturer/Mike_umbrella.png").convert() #image.load는 이미지를 가져오고 
                                                                                #convert가 그 이미지를 그래픽카드가 읽을수 있는 포맷으로 바꿔줌
cloud_image = pygame.image.load("C:/Users/sehwa/Desktop/picturer/cloud.png").convert()
mike_image = pygame.image.load("C:/Users/sehwa/Desktop/picturer/Mike.png").convert()

class Raindrop:     #class이름은 대문자로 시작함
    def __init__(self,x,y):     #class의 첫 함수는 반드시 __init__으로 시작해야함, self는 더 알아보기
        self.x = x
        self.y = y
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
        if time.time() > last_hit_time + 1:
            screen.blit(mike_image,(self.x,self.y))
        else:
            screen.blit(mike_umbrella_image,(self.x,self.y)) #screen.blit은 전송될 개체와 좌표를 갖는다 개체는 이미지,좌표는 xy
    def hit_by(self,raindrop): #빗방울이 이미지에 부딛혔을때 삭제하는건데 잘 몰?루겠음
        return pygame.Rect(self.x,self.y,170,192).collidepoint((raindrop.x,raindrop.y))

class Cloud:
    def __init__(self):
        self.x = 300
        self.y = 50

    def draw(self):
        screen.blit(cloud_image,(self.x,self.y))

    def rain(self):   #for i in range(원하는수)로 빗방울을 늘릴수잇음
        raindrops.append(Raindrop(random.randint(self.x,self.x+300),self.y+100))  #300이랑 100 더하는거는 구름의 x길이y길이가 300,100임
    
    def move(self):
        if pressed_keys[K_RIGHT]:
            self.x += 1
        if pressed_keys[K_LEFT]:
            self.x -= 1


raindrops = []  #raindrop들로 이 리스트가 채워진다함(27줄) 보통 리스트는 class이름에 s를 붙여 복수형으로 이름지음
mike = Mike() #마이크를 부르는 인스턴스 마이크 나와!!!
cloud = Cloud() #구름 인스턴스
while True:
    clock.tick(60)  #이거 안쓰면 비가 엄청 빨리 떨어짐
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed() #키로 구름 움직이게하려고
    #raindrops.append(Raindrop())    구름에서 내리게 할거라 비활성화
    screen.fill((255,255,255))
    mike.draw() #마이크 소환!!!
    cloud.draw() #구름 소환!!
    cloud.rain() #구름에서 비내림
    cloud.move()

    i = 0
    while i < len(raindrops):             #아 이해했다 제일큰 while true루프를 돌고 다시 내려와서 raindrops 리스트 안에 있는 숫자만큼 다시 i가 올라가는거임 아 드디어
        raindrops[i].move()
        raindrops[i].draw()
        flag = False
        if raindrops[i].off_screen():
            del raindrops[i]
            i -= 1
            flag = True
        if mike.hit_by(raindrops[i]): #마이크가 빗방울 맞았을때 삭제&마지막으로 맞은시간 기록
            del raindrops[i]
            i -= 1
            flag = True
            last_hit_time = time.time()
        if flag:
            del raindrops[i]
            i -= 1
        i += 1

    pygame.display.update()
