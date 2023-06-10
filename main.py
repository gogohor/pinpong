from pygame import*
from time import sleep 

from button import Button
from sprite import Player,Enemy,Wall,GameSprite,Wall1


window = display.set_mode((700,500))
clock = time.Clock()
display.set_caption("небесний Лабіринт")

game = True
btn_start = Button(0,400,100,50,"pngwing.com.png")
btn_exit = Button(0,450,100,50,"xit.png")

btn_exit1 = Button(600,450,100,50,"xit.png")

btn_level1 = Button(20,20,70,70,'level1.png')
btn_level2 = Button(20,100,70,70,'level2.png')
btn_level3 = Button(20,180,70,70,'level3.png')
btn_level4 = Button(20,260,70,70,'level4.png')

player1 = Player('hero.png', 495,420,10)
player = Player('hero.png', 0, 320,10)
player2 = Player('hero.png', 30, 350,10)
player3 = Player('hero.png', 5, 230,10)

final = Player('gold.png', 630,140, 0)


final2 = Player('gold.png', 30,10, 0)
final3 = Player('button.png', 25,415, 0)

level1_pula = Enemy('pula.png',30,20,12.5)
level2_pula = Enemy('pula.png',300,180,12.5)

level3_pula1 = Enemy('pula.png',120,20,12.5)
level3_pula2 = Enemy('pula.png',30,20,2)
level3_pula3 = Enemy('pula.png',500,420,9.5)


final4 = Player('gold.png', 560,10,0)
final5 = Player('button.png', 30,20,0)
final6 = Player('button.png', 30,230,0)

button = Player("Button.png",30,330,4)
button2 = Player("Button.png",30,410,4)
button3 = Player("Button.png",30,150,4)
button4 = Player("Button.png",610,30,4)
final8 = Player('gold.png', 620,230,10)
level4_pula = Enemy('pula.png',30,30,12.5)
level4_pula2 = Enemy('pula.png',500,420,9.5)
level4_pula3 = Enemy('pula.png',120,180,9.5)
b = False
b2 = False
b3 = False
b4 = False


walls_level1 = []

wall1_level1 = Wall1((2,4,55), 10,10,680,10)
wall2_level1 = Wall1((2,4,55), 10,10,10,310)
wall3_level1 = Wall1((2,4,55), 10,480,680,10)
wall4_level1 = Wall1((2,4,55), 10,400,10,80)
wall5_level1 = Wall1((2,4,55), 680,190,10,340)
wall6_level1 = Wall1((2,4,55), 680,10,10,100)
wall7_level1 = Wall1((2,4,55), 10,100,200,10)
wall8_level1 = Wall1((2,4,55), 340,100,270,10)
wall9_level1 = Wall1((2,4,55), 200,100,10,100)
wall10_level1 = Wall1((2,4,55), 10,180,80,10)
wall11_level1 = Wall1((2,4,55), 10,310,100,10)
wall12_level1 = Wall1((2,4,55), 100,310,10,100)
wall13_level1 = Wall1((2,4,55),590,190,90,10)
wall14_level1 = Wall1((2,4,55), 100,310,10,80)
wall15_level1 = Wall1((2,4,55),550,325,100,10)
wall16_level1 = Wall1((2,4,55), 500,110,10,220)
wall17_level1 = Wall1((2,4,55),200,400,10,80)
wall18_level1 = Wall1((2,4,55), 290,310,120,10)
wall19_level1 = Wall1((2,4,55),290,210,10,100)
wall20_level1 = Wall1((2,4,55), 370,200,30,30)




walls_level1.append(wall1_level1)
walls_level1.append(wall2_level1)
walls_level1.append(wall3_level1)
walls_level1.append(wall4_level1)
walls_level1.append(wall5_level1)
walls_level1.append(wall6_level1)
walls_level1.append(wall7_level1)
walls_level1.append(wall8_level1)
walls_level1.append(wall9_level1)
walls_level1.append(wall10_level1)
walls_level1.append(wall11_level1)
walls_level1.append(wall12_level1)
walls_level1.append(wall13_level1)
walls_level1.append(wall14_level1)
walls_level1.append(wall15_level1)
walls_level1.append(wall16_level1)
walls_level1.append(wall17_level1)
walls_level1.append(wall18_level1)
walls_level1.append(wall19_level1)
walls_level1.append(wall20_level1)


walls_level2 = []

wall1_level2 = Wall1((2,4,55), 100,10,580,10)
wall2_level2 = Wall1((2,4,55), 10,10,10,470)
wall3_level2 = Wall1((2,4,55), 680,10,10,480)
wall4_level2 = Wall1((2,4,55), 10,480,480,10)
wall5_level2 = Wall1((2,4,55), 480,10,100,10)
wall6_level2 = Wall1((2,4,55), 100,250,10,230)
wall7_level2 = Wall1((2,4,55), 580,480,100,10)
wall8_level2 = Wall1((2,4,55), 100,250,250,10)
wall9_level2 = Wall1((2,4,55), 350,250,10,100)
wall10_level2 = Wall1((2,4,55), 200,350,350,10)
wall11_level2 = Wall1((2,4,55), 540,250,10,100)
wall12_level2 = Wall1((2,4,55), 10,170,450,10)
wall13_level2 = Wall1((2,4,55), 590,170,100,10)
wall14_level2 = Wall1((2,4,55), 450,110,10,70)
wall15_level2 = Wall1((2,4,55), 590,10,10,70)
wall16_level2 = Wall1((2,4,55), 350,10,10,70)
wall17_level2 = Wall1((2,4,55), 250,110,10,70)

wall18_level2 = Wall1((2,4,55),250,10,10,100)

walls_level2.append(wall1_level2)
walls_level2.append(wall2_level2)
walls_level2.append(wall3_level2)
walls_level2.append(wall4_level2)
walls_level2.append(wall5_level2)
walls_level2.append(wall6_level2)
walls_level2.append(wall7_level2)
walls_level2.append(wall8_level2)
walls_level2.append(wall9_level2)
walls_level2.append(wall10_level2)
walls_level2.append(wall11_level2)
walls_level2.append(wall12_level2)
walls_level2.append(wall13_level2)
walls_level2.append(wall14_level2)
walls_level2.append(wall15_level2)
walls_level2.append(wall16_level2)
walls_level2.append(wall17_level2)

walls_level3 = []

wall1_level3 = Wall1((2,4,55), 10,10,540,10)
wall2_level3 = Wall1((2,4,55), 10,10,10,470)
wall3_level3 = Wall1((2,4,55), 150,480,500,10)
wall4_level3 = Wall1((2,4,55), 10,480,150,10)
wall5_level3 = Wall1((2,4,55), 630,10,50,10)
wall6_level3 = Wall1((2,4,55), 680,10,10,470)
wall7_level3 = Wall1((2,4,55), 10,300,90,10)
wall8_level3 = Wall1((2,4,55), 680,10,10,470)
wall9_level3 = Wall1((2,4,55), 100,200,10,200)
wall10_level3 = Wall1((2,4,55), 100,400,370,10)
wall11_level3 = Wall1((2,4,55), 550,400,60,10)
wall12_level3 = Wall1((2,4,55), 600,200,10,200)
wall13_level3 = Wall1((2,4,55), 440,100,240,10)
wall14_level3 = Wall1((2,4,55), 100,10,10,100)
wall15_level3 = Wall1((2,4,55), 200,320,330,10)
wall16_level3 = Wall1((2,4,55), 520,100,10,80)
wall17_level3 = Wall1((2,4,55), 280,180,130,10)
wall18_level3 = Wall1((2,4,55), 280,180,10,150)
wall19_level3 = Wall1((2,4,55), 100,100,190,10)
wall20_level3 = Wall1((2,4,55), 480,10,10,100)
wall21_level3 = Wall1((2,4,55), 290,100,190,10)

walls_level3.append(wall1_level3)
walls_level3.append(wall2_level3)
walls_level3.append(wall3_level3)
walls_level3.append(wall4_level3)
walls_level3.append(wall5_level3)
walls_level3.append(wall6_level3)
walls_level3.append(wall7_level3)
walls_level3.append(wall8_level3)
walls_level3.append(wall9_level3)
walls_level3.append(wall10_level3)
walls_level3.append(wall11_level3)
walls_level3.append(wall12_level3)
walls_level3.append(wall13_level3)
walls_level3.append(wall14_level3)
walls_level3.append(wall15_level3)
walls_level3.append(wall16_level3)
walls_level3.append(wall17_level3)
walls_level3.append(wall18_level3)
walls_level3.append(wall19_level3)

walls_level4 = []


wall1_level4 = Wall1((2,4,55), 10,10,680,10)
wall2_level4 = Wall1((2,4,55), 10,10,10,200)
wall3_level4 = Wall1((2,4,55), 10,300,10,190)
wall4_level4 = Wall1((2,4,55), 10,10,10,220)
wall5_level4 = Wall1((2,4,55), 10,480,680,10)
wall6_level4 = Wall1((2,4,55), 680,10,10,220)
wall7_level4 = Wall1((2,4,55), 680,300,10,190)
wall8_level4 = Wall1((2,4,55), 10,300,100,10)
wall9_level4 = Wall1((2,4,55), 10,220,100,10)
wall10_level4 = Wall1((2,4,55), 100,120,10,100)
wall11_level4 = Wall1((2,4,55), 190,120,100,10)
wall12_level4 = Wall1((2,4,55), 190,120,10,190)
wall13_level4 = Wall1((2,4,55), 280,120,10,100)
wall14_level4 = Wall1((2,4,55), 190,300,100,10)
wall15_level4 = Wall1((2,4,55), 290,300,10,100)
wall16_level4 = Wall1((2,4,55), 280,220,100,10)
wall17_level4 = Wall1((2,4,55), 380,10,10,120)
wall18_level4 = Wall1((2,4,55), 480,100,200,10)
wall19_level4 = Wall1((2,4,55), 10,400,290,10)
wall20_level4 = Wall1((2,4,55), 600,180,10,50)
wall21_level4 = Wall1((2,4,55), 600,300,80,10)
wall22_level4 = Wall1((2,4,55), 600,220,80,10)
wall23_level4 = Wall1((2,4,55), 480,100,10,220)
wall24_level4 = Wall1((2,4,55), 410,320,80,10)
wall25_level4 = Wall1((2,4,55), 400,320,10,90)
wall26_level4 = Wall1((2,4,55), 410,320,80,10)
wall27_level4 = Wall1((2,4,55), 400,400,170,10)


wall28_level4 = Wall1((2,4,55), 600,220,10,90)
wall29_level4 = Wall1((2,4,55), 510,400,170,10)





walls_level4.append(wall1_level4)
walls_level4.append(wall2_level4)
walls_level4.append(wall3_level4)
walls_level4.append(wall4_level4)
walls_level4.append(wall5_level4)
walls_level4.append(wall6_level4)
walls_level4.append(wall7_level4)
walls_level4.append(wall8_level4)
walls_level4.append(wall9_level4)
walls_level4.append(wall10_level4)
walls_level4.append(wall11_level4)
walls_level4.append(wall12_level4)
walls_level4.append(wall13_level4)
walls_level4.append(wall14_level4)
walls_level4.append(wall15_level4)
walls_level4.append(wall16_level4)
walls_level4.append(wall17_level4)
walls_level4.append(wall18_level4)
walls_level4.append(wall19_level4)
walls_level4.append(wall20_level4)
walls_level4.append(wall21_level4)
walls_level4.append(wall22_level4)
walls_level4.append(wall23_level4)
walls_level4.append(wall24_level4)
walls_level4.append(wall25_level4)
walls_level4.append(wall26_level4)
walls_level4.append(wall27_level4)



font.init()
font = font.Font(None,70)
win = font.render('YOU WIN',True,(255,255,255))
lose = font.render('YOU LOSE',True,(255,255,255))




level4 = False
level3 = False
level2 = False

run = "payza"

level1 = "payza"


while game:
    background = transform.scale(image.load('background.com.png'),(700,500))
    
    window.blit(background,(0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
   
    if run == "level":
        window.blit(background,(0,0))

        if btn_level1.draw(window):
                level1 = "go"

        if btn_level2.draw(window):
            level2 = True

        if btn_exit1.draw(window):
            run = "payza"

        if btn_level3.draw(window):
            level3 = True

        if btn_level4.draw(window):
            level4 = True


        if level1 == "go":
            player2.rect.x = 30
            player2.rect.y = 350
            player1.rect.x = 420
            player1.rect.y = 495
            
            window.blit(background,(0,0))
            player.draw(window)
            player.move()
            level1_pula.draw(window)
            level1_pula.move_left_right(20,600)
            final.draw(window)
            
            
            
            for wall in walls_level1:
                wall.draw(window)


            if btn_exit1.draw(window):
                run = "payza"
                player.rect.x = 10
                player.rect.y = 320

            
            if player.rect.y <= 0 or player.rect.y >= 480:
                player.rect.x = 10
                player.rect.y = 320

           

            for wall in walls_level1:

                if player.rect.colliderect(wall.rect):
                    if player.dir2 == "left":
                        player.rect.left = wall.rect.right
                    if player.dir2 == "right":
                        player.rect.right = wall.rect.left
                    if player.dir2 == "up":
                        player.rect.top = wall.rect.bottom
                    if player.dir2 == "down":
                        player.rect.bottom = wall.rect.top


                if sprite.collide_rect(player,level1_pula):
                    window.blit(lose,(200,200))
                    player.rect.y = 320
                    player.rect.x = 10
                    
                if sprite.collide_rect(player,final):
                    window.blit(win,(200,200))

                  
        if level2:  
            player.rect.x = 10
            player.rect.y = 320
            player2.rect.x = 30
            player2.rect.y = 350
            window.blit(background,(0,0))
            final2.draw(window)
            final3.draw(window)
            player1.draw(window)
            player1.move()
            level2_pula.draw(window)   
            level2_pula.move_left_right(20,600)
            wall18_level2.draw(window)  


            if player1.rect.y < 0 or player1.rect.y >= 480:
                player1.rect.x = 495
                player1.rect.y = 420
            
            for wall in walls_level2:
                wall.draw(window)

            if sprite.collide_rect(player1,level2_pula):
                player1.rect.y = 420
                player1.rect.x = 495
                final3.rect.x = 25
                wall18_level2.rect.x = 250
                window.blit(lose,(200,200))


            if sprite.collide_rect(player1,final3):
                wall18_level2.rect.x = 800
                final3.rect.x = 800

            if sprite.collide_rect(player1,final2):
                    window.blit(win,(200,200))
                
            for wall in walls_level2:

                if player1.rect.colliderect(wall.rect):
                    if player1.dir2 == "left":
                        player1.rect.left = wall.rect.right
                    if player1.dir2 == "right":
                        player1.rect.right = wall.rect.left
                    if player1.dir2 == "up":
                        player1.rect.top = wall.rect.bottom
                    if player1.dir2 == "down":
                        player1.rect.bottom = wall.rect.top

            if btn_exit1.draw(window):
                run = "payza"
                level2 = False
                player1.rect.x = 420
                player1.rect.y = 495

        if level3:
            player.rect.x = 10
            player.rect.y = 320
            player1.rect.x = 420
            player1.rect.y = 495
            window.blit(background,(0,0))
            final5.draw(window)
            final6.draw(window)
            final4.draw(window)           
            player2.draw(window)
            player2.move()
            level3_pula1.draw(window)   
            level3_pula1.move_left_right(120,600)
            level3_pula2.draw(window)   
            level3_pula2.move_up_down(30,230)
            level3_pula3.draw(window)   
            level3_pula3.move_left_right(30,600)
            wall20_level3.draw(window)
            wall21_level3.draw(window)

            for wall in walls_level3:
                wall.draw(window)

            for wall in walls_level3:

                if player2.rect.colliderect(wall.rect):
                    if player2.dir2 == "left":
                        player2.rect.left = wall.rect.right
                    if player2.dir2 == "right":
                        player2.rect.right = wall.rect.left
                    if player2.dir2 == "up":
                        player2.rect.top = wall.rect.bottom
                    if player2.dir2 == "down":
                        player2.rect.bottom = wall.rect.top

            if player2.rect.y <= 0 or player2.rect.y >= 480:
                player2.rect.x = 30 
                player2.rect.y = 350

            if btn_exit1.draw(window):
                run = "payza"
                level3 = False
                player2.rect.x = 80
                player2.rect.y = 440

            if sprite.collide_rect(player2,level3_pula1) or sprite.collide_rect(player2,level3_pula2) or sprite.collide_rect(player2,level3_pula3):
                player2.rect.y = 350
                player2.rect.x = 30
                wall20_level3.rect.x = 480
                wall21_level3.rect.x = 290
                window.blit(lose,(200,200))
                wall7_level3.rect.x = 10
                final5.rect.x = 30
                final6.rect.x = 30


            if sprite.collide_rect(player2,final5):
                wall20_level3.rect.x = 800
                wall7_level3.rect.x = 800
                final5.rect.x = 800

            if sprite.collide_rect(player2,final6):
                wall21_level3.rect.x = 800
                final6.rect.x = 800

            if sprite.collide_rect(player2,final4):
                window.blit(win,(200,200))
            
            
        if level4:
            player.rect.x = 10
            player.rect.y = 320
            player1.rect.x = 420
            player1.rect.y = 495
            player2.rect.y = 350
            player2.rect.x = 30
            window.blit(background,(0,0))
            button.draw(window)
            button2.draw(window)
            button3.draw(window)
            button4.draw(window)
            player3.draw(window)
            player3.move()
            wall29_level4.draw(window)
            wall28_level4.draw(window)
            final8.draw(window)
            level4_pula.draw(window)  
            level4_pula2.draw(window)  
            level4_pula3.draw(window) 
            level4_pula.move_left_right(30, 310) 
            level4_pula2.move_left_right(30, 680) 
            level4_pula3.move_up_down(20,330)

            for wall in walls_level4:

                if player3.rect.colliderect(wall.rect):
                    if player3.dir2 == "left":
                        player3.rect.left = wall.rect.right
                    if player3.dir2 == "right":
                        player3.rect.right = wall.rect.left
                    if player3.dir2 == "up":
                        player3.rect.top = wall.rect.bottom
                    if player3.dir2 == "down":
                        player3.rect.bottom = wall.rect.top


            for wall in walls_level4:
                wall.draw(window)


            if player3.rect.y <= 0 or player3.rect.y >= 480:
                player3.rect.x = 5 
                player3.rect.y = 230

            if btn_exit1.draw(window):
                level4 = False
                run = "payza"
                player3.rect.x = 5
                player3.rect.y = 230

            if sprite.collide_rect(player3,button):
                b = True
                button.rect.x = 800
            
            if sprite.collide_rect(player3,button2):
                b2 = True
                button2.rect.x = 800

            if sprite.collide_rect(player3,button3):
                b3 = True
                button3.rect.x = 800
                
            if sprite.collide_rect(player3,button4):
                wall29_level4.rect.x = 800
                button4.rect.x = 800
                b4 = True

            if b == True and b2 == True and b3 == True and b4 == True:
                wall28_level4.rect.x = 800

            if sprite.collide_rect(player3,final8):
                window.blit(win,(200,200))
            
            if sprite.collide_rect(player3,level4_pula) or sprite.collide_rect(player3,level4_pula2) or sprite.collide_rect(player3,level4_pula3):
                window.blit(lose,(200,200))
                player.rect.x = 5
                player.rect.y = 230

                wall29_level4.rect.x = 510
                button4.rect.x = 610
                wall28_level4.rect.x = 600
                button3.rect.x = 30
                button2.rect.x = 30
                button.rect.x = 30

                b = False
                b2 = False
                b3 = False
                b4 = False

                

    if run == "payza":
        if btn_start.draw(window):
            run = "level"
            level1 = "payza"
            
        if btn_exit.draw(window):
            game = False
        
    display.update()
    clock.tick(60)