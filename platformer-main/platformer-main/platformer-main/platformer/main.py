from pygame import *
from random import randint
from random import choice, randint

class Game_sprite(sprite.Sprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Player(Game_sprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__(img, x,y, w,h, speed)
        self.opora = False
    def update(self):
        global x_pos
        key_pressed = key.get_pressed()
        if self.rect.x<x_start or self.rect.x>x_max-x_start: #что то тут не так
            if key_pressed[K_a] and self.rect.x>10:
                self.rect.x-= self.speed 
            if key_pressed[K_d] and self.rect.x<700 - 10-self.rect.width:
                self.rect.x+= self.speed
        else:
            if key_pressed[K_a] and x_pos<0:
                x_pos+= self.speed 
            if key_pressed[K_d]and x_pos<x_max-x_start*2 :
                x_pos-= self.speed
                
        if key_pressed[K_SPACE] and self.opora == True:
            self.rect.y-= 100
        
    def gravity(self):
        self.opora = False
        sprite_list = sprite.spritecollide(hero,platforms,False)
        if len(sprite_list)!=0:
            self.opora = True
            # self.rect.y-=5
        if not self.opora:
            self.rect.y+=5

        
    # def Fire(self):
    #     bullet = Bullet('bullet.png',self.rect.centerx,self.rect.y,15,30,25)
    #     bullets.add(bullet)    
        
class Enemy(Game_sprite):
    def __init__(self, img, x,y, w,h, speed,fly=0):
        super().__init__(img, x,y, w,h, speed)
        self.fly = fly
    def start(self, z1,z2):
        self.z1 = z1
        self.z2 = z2
    
    def update(self):
        global x_pos
        if  self.fly == 1:
            if self.rect.y <= min(self.z1, self.z2):
                self.direct = 1 
            elif self.rect.y >= max(self.z1, self.z2):
                self.direct = -1
            self.rect.y+=self.speed*self.direct
            self.rect.x+=x_pos
        else:
            if self.rect.x <= min(self.z1, self.z2):
                self.direct = 1 
            elif self.rect.x >= max(self.z1, self.z2):
                self.direct = -1
            self.rect.x+=self.speed*self.direct+x_pos








# class Bullet(Game_sprite):
#     def update(self):
#         self.rect.y-=self.speed
#         if  self.rect.y<=0:
#             self.kill()

class Platform(Game_sprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__(img, x,y, w,h, speed)
        self.x_start = x

    def update(self):
        self.rect.x = self.x_start+x_pos


x_start = 350-75/2
x_pos = 0
x_max = 1400





#создай окно игры
win = display.set_mode((700,500))
display.set_caption('Крутой платформер(то что надо)')
background= transform.scale(image.load("fon.png"),(700,500))

platforms = sprite.Group()
# plt_coord = [[x,y], [x,y], [x,y]]
pl_count = 25
for i in range(pl_count):
    x = randint(5,10*x_max-105)
    y = randint(100,200)
# for x,y in plt_coord:
    plt = Platform('platform1.png', x, y, 100, 50, 0)
    platforms.add(plt)
plt = Platform('platform1.png', 0, 480, 20*x_max, 50, 0)
platforms.add(plt)



# подключение музыки
# mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()










# работа со шрифтами
font.init()
font1 = font.Font(None,36)


hero = Player('hero.png', 25,100, 51,75, 15)

enemys=sprite.Group()
enemy1 = Enemy('enemy.jpg',200,300,51,75,5,0)
enemy1.start(200,300)
enemys.add(enemy1)
enemy2 = Enemy('enemy.jpg',400,200,51,75,5,1)
enemy2.start(200,300)
enemys.add(enemy2)



clock = time.Clock()
FPS = 40
 
game = True
fin = False
lost = 0
score = 0

menu = True


while game:
    # проверка нажатия на кнопку выход
    for e in event.get():
        if e.type == QUIT:
            game = False
        # if e.type == KEYDOWN:
        #     if e.key == K_SPACE:
        #         hero.Fire()
        
    # if menu:
    #     win.blit(background,(0,0))
    #     knopa.reset()
    #     pressed = mouse.get_pressed()
    #     pos = mouse.get_pos()
    #     if pressed[0]:
    #         if knopa.collidepoint(pos[0],pos[1]):
    #             menu = False
    #             fin = False       
                
    if not fin:
        
        win.blit(background,(0,0))
        platforms.draw(win)
        platforms.update() 
        hero.update()
        hero.reset()
        hero.gravity()
        enemys.update()
        enemys.draw(win)
        # обновление окна игры
        
    display.update()
    clock.tick(FPS)