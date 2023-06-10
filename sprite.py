from pygame import*
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,image_name,x,y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name),(65,65))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = x
        self.rect.y = y
        self.dir2 = "right"
    
    def draw(self,window):
        window.blit(self.image,(self.rect.x,self.rect.y))



class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.dir2 = "left"
            self.speed = 10
            self.rect.x -= self.speed
            self.image = transform.scale(image.load("hero1.png"),(65,65))

        if keys[K_d] and self.rect.x < 640:
            self.dir2 = "right"
            self.speed = 10
            self.rect.x += self.speed
            self.image = transform.scale(image.load("hero.png"),(65,65))

        if keys[K_w] and self.rect.y > 5:
            self.dir2 = "up"
            self.speed = 10
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y <  430:
            self.dir2 = "down"
            self.speed = 10
            self.rect.y += self.speed
            
class Enemy(GameSprite):
    direction = 'left'
    def move_left_right(self,rect_x,rect_x1):
        if self.rect.x < rect_x:
            self.direction = 'right'
        if self.rect.x > rect_x1:
            self.direction = 'left'

        if self.direction == 'left':
            
            self.rect.x -= self.speed
        else:
            
            self.rect.x += self.speed

    def move_up_down(self,rect_y,rect_y1):
        direction2 = 'up'
        if self.rect.y < rect_y:
            self.direction = 'down'
        if self.rect.y > rect_y1:
            self.direction = 'up'
        if self.direction == 'up':    
            self.rect.y-= self.speed
        else:           
            self.rect.y += self.speed


class Wall1(sprite.Sprite):
    def __init__(self, rgb, x,y,w,h):
        super().__init__()
        self.rgb = rgb
        self.width = w
        self.height = h
        self.wall = Surface((w,h))
        self.wall.fill(rgb)

        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,window):
        window.blit(self.wall, (self.rect.x, self.rect.y))



class Wall(sprite.Sprite):
    def __init__(self,width,height,x,y,color=(200,56,89),transperncy=255):
        super().__init__()
        self.wall = Surface((width,height))
        self.wall.set_alpha(transperncy)
        self.wall.fill(color)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,window):
        self.rect.x -= 5
        if self.rect.x <0:
            self.rect.x = 700
            self.rect.y = randint(50,300)

        window.blit(self.wall,(self.rect.x,self.rect.y))

    def draw_wall(self,window):
        window.blit(self.wall,(self.rect.x,self.rect.y))
    

    