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
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x>10:
            self.rect.x-= self.speed 
        if key_pressed[K_RIGHT] and self.rect.x<700 - 10-self.rect.width:
            self.rect.x+= self.speed
        if key_pressed[K_UP] and self.rect.y<500 - 10-self.rect.height:
            self.opora = True
            self.rect.y+= self.speed
            self.opora = False
        
    def gravity(self):
        self.opora = False
        sprite_list = sprite.spritecollide(hero,platforms,False)
        if len(sprite_list)!=0:
            self.opora = True
        if not self.opora:
            self.rect.y+=5

        
    # def Fire(self):
    #     bullet = Bullet('bullet.png',self.rect.centerx,self.rect.y,15,30,25)
    #     bullets.add(bullet)    
        
# class Enemy(Game_sprite):
#     def update(self):
#         global lost
#         self.rect.y+=self.speed
#         if  self.rect.y>500-self.rect.height:
#             self.rect.x = randint(10,700-10-self.rect.width)
#             self.rect.y = -self.rect.height
#             self.speed = randint(2,5)
#             lost+=1

# class Bullet(Game_sprite):
#     def update(self):
#         self.rect.y-=self.speed
#         if  self.rect.y<=0:
#             self.kill()

class Platform(Game_sprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__(img, x,y, w,h, speed)


#создай окно игры
win = display.set_mode((700,500))
display.set_caption('Крутой платформер(то что надо)')
background= transform.scale(image.load("fon.png"),(700,500))

platforms = sprite.Group()
pl_count = 5
for i in range(pl_count):
    x = randint(5,700-105)
    y = randint(200,400)
    plt = Platform('platform1.png', x, y, 100, 50, 0)
    platforms.add(plt)
plt = Platform('platform1.png', 0, 480, 700, 50, 0)
platforms.add(plt)



# подключение музыки
# mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()

# работа со шрифтами
font.init()
font1 = font.Font(None,36)


hero = Player('hero.png', 25,100, 51,75, 15)







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
        hero.update()
        hero.reset()
        hero.gravity()    
        # обновление окна игры
        
    display.update()
    clock.tick(FPS)