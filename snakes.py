# i_path = ipath[count]
import pygame
import random
pygame.mixer.pre_init(44100, -16, 3, 4096)
pygame.init()
screen_width=1200
screen_height=600
font=pygame.font.SysFont(pygame.font.get_fonts()[0],40,False,True)
font2=pygame.font.SysFont(pygame.font.get_fonts()[0],60,True,False)
font3=pygame.font.SysFont( pygame.font.get_fonts()[0],40,True,True)
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snakes game")
pygame.display.update()
main_menu=True
pygame.mixer.music.load("awesomeness.wav")
pygame.mixer.music.play(-1)
image2=pygame.image.load("snakes-in-nature-scene-vector-26599598.jpg")
def drawsnake(screen,snk_list,snake_size):
    for i in snk_list:
        pygame.draw.rect(screen,(255,0,0),(i[0],i[1],snake_size,snake_size))
def gameloop(main_menu):
    game_over=False
    exit_game=False
    snake_x=45
    snake_y=55
    velocity_x,velocity_y=0,0
    snake_size=10
    food_x,food_y=random.randint(50,screen_width-30),random.randint(50,screen_height-30)
    fps=30
    appleimage=pygame.image.load("unnamed.png")
    resizeapple=pygame.transform.scale(appleimage,(15,15))
    score=0
    highscore=100
    snk_list=[]
    snk_length=1
    clock=pygame.time.Clock()
    while not(exit_game):
        clock.tick(fps)
        sf=font.render(f"SCORE:{score}",1,(123,24,145))
        if main_menu:
            title=font2.render("SNAKES",1,(56,67,56))
            text=font3.render("Press enter to start game",1,(218,114,45))
            screen.fill((255,255,255))
            image1=pygame.image.load("84-848297_movies-jungle-book-snake-kaa-mowgli-wallpapers-desktop.jpg")
            resize1=pygame.transform.scale(image1,(1200,600))
            screen.blit(resize1,(0,0))
            screen.blit(title,(500,3))
            screen.blit(text,(400,200))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                elif event.type==pygame.KEYDOWN:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Keyboard_Button_1-fesliyanstudios.com.wav"))
                    if event.key==pygame.K_RETURN:
                        main_menu=False
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("game-over-sound-effect.wav"))
                        gameloop(main_menu)
        elif game_over:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("game-over-sound-effect.wav"))
            screen.fill((255,255,255))
            resize2=pygame.transform.scale(image2,(1200,600))
            screen.blit(resize2,(0,0))
            fail=font.render("Game Over",1,(125,0,0))
            result=font.render(f"your score:{score}",1,(125,0,0))
            best=font.render(f"highscore:{highscore}",1,(125,0,0))
            screen.blit(fail,(screen_width/2,6))
            screen.blit(result,(screen_width/2,screen_height/6+25))
            screen.blit(best,(screen_width/2,screen_height/6+50))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                elif event.type==pygame.KEYDOWN:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Keyboard_Button_1-fesliyanstudios.com.wav"))
                    if event.key==pygame.K_RETURN:
                        gameloop(main_menu)
        else:
#             appleimg=pygame.image.load("unnamed.png")
            pygame.mixer.music.stop()
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("windows_error.wav"))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                elif event.type==pygame.KEYDOWN:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Keyboard_Button_1-fesliyanstudios.com.wav"))
                    if event.key==pygame.K_RIGHT:
                        velocity_x=4
                        velocity_y=0
                    elif event.key==pygame.K_LEFT:
                        velocity_x=-4
                        velocity_y=0
                    elif event.key==pygame.K_UP:
                        velocity_y=-4
                        velocity_x=0
                    elif event.key==pygame.K_DOWN:
                        velocity_y=4
                        velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("Apple_Bite-Simon_Craggs-1683647397.wav"))
                snk_length+=5
                food_x,food_y=random.randint(0,screen_width-30),random.randint(0,screen_height-30)
                if score>100:
                    highscore=score
            screen.fill((74,218,184))
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
            if (snake_x<0 or snake_x>screen_width) or (snake_y<0 or snake_y>screen_height):
                game_over=True
#             pygame.draw.rect(screen,(0,0,0),(food_x,food_y,snake_size,snake_size))
            screen.blit(resizeapple,(food_x,food_y))
            drawsnake(screen,snk_list,snake_size)
            screen.blit(sf,(4,20))
        pygame.display.update()
    pygame.quit()
    quit()
gameloop(main_menu)    
