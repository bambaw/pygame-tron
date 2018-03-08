import pygame
import os
os.environ["SDL_VIDEO_CENTERED"]="1"
pygame.init()

#Colors
black = (0,0,0) 
red = (255, 0, 0)
blue = (0, 128, 255)
orange = (255, 153, 0)
violet = (102, 51, 153)

display_width, display_height = 1000,700
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Menu Fonts
font = pygame.font.Font(os.path.join('OrangeKid.ttf'), 40)
smallfont = pygame.font.Font('OrangeKid.ttf',30)
medfont = pygame.font.Font('OrangeKid.ttf',50)
largefont = pygame.font.Font('OrangeKid.ttf',80)
medlargefont = pygame.font.Font('OrangeKid.ttf',120)
Tron_font = pygame.font.Font(os.path.join('OrangeKid.ttf'),120)

#Dots For choice
choice_dot = pygame.Rect(320,265,10,10)
credits_dot = pygame.Rect(675,655,10,10)
controls_dot = pygame.Rect(675,655,10,10)

clock = pygame.time.Clock()


#Credits #TESTING 
def game_credits():
    crdts = True
    while crdts:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    return 0
                elif event.key == pygame.K_RETURN:
                    if credits_dot.top == 655:
                        return True
                           
        display_width , display_height = 1000 , 700
        gameDisplay = pygame.display.set_mode((display_width,display_height))
        gameDisplay.fill(black)
        gameDisplay.blit(Tron_font.render("Credits~",False,blue), (100,15))
        gameDisplay.blit(font.render("Wikipedia (Game Description)",False,blue), (400,150))
        gameDisplay.blit(font.render("Tron Movie (Game Idea)",False,blue), (400,200))
        gameDisplay.blit(font.render("Youtube  (Music)",False,blue), (400,250))
        gameDisplay.blit(font.render("Hypodermic larable fonts  (Font)",False,blue), (400,300))
        gameDisplay.blit(font.render("YouTube University  (Coding)",False,blue), (400,350))
        gameDisplay.blit(font.render("Pygame.org/docs  (Coding)",False,blue), (400,400))
        gameDisplay.blit(font.render("Back To Menu",False,blue), (700,640))
        gameDisplay.blit(font.render("Special Thanks to:",False,blue), (50,550))
        gameDisplay.blit(font.render("Sir Jayran Labrador",False,blue), (330,550))
        gameDisplay.blit(font.render("(Who made all of these things possible)",False,blue), (70,600))
         
        pygame.draw.rect(gameDisplay,blue,credits_dot)
        pygame.display.update()
        clock.tick(25)
          
def controls():
    controls = True
    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    return 0
                elif event.key == pygame.K_RETURN:
                    if credits_dot.top == 655:
                        return 0
        display_width , display_height = 1000 , 700
        gameDisplay = pygame.display.set_mode((display_width,display_height))
        gameDisplay.fill(black)
        gameDisplay.blit(medfont.render("*Controls* ~",False,blue), (30,30))
        gameDisplay.blit(smallfont.render("Player 1 --< W-A-S-D",False,blue), (100,100))
        gameDisplay.blit(smallfont.render("Player 2 --< T-F-G-H",False,blue), (100,130))
        gameDisplay.blit(smallfont.render("Player 3 --< I-J-K-L",False,blue), (100,160))
        gameDisplay.blit(smallfont.render("Player 4 --< Arrow Keys",False,blue),(100,190))
        gameDisplay.blit(medfont.render("*Game Description* ~",False,blue),(550,30))
        gameDisplay.blit(smallfont.render("''Players are in constant motion on a playfield",False,blue), (500,100))
        gameDisplay.blit(smallfont.render("creating a wall of light behind them as they move.",False,blue), (485,130))
        gameDisplay.blit(smallfont.render("If players hit a wall, they are out of the game.",False,blue), (485,160))
        gameDisplay.blit(smallfont.render("The last man standing in the game gains a point.",False,blue),(485,190))
        gameDisplay.blit(smallfont.render("When a player gets 5 points, the player wins.",False,blue),(485,220))
        gameDisplay.blit(medfont.render("*About Us*  ~",False,blue),(30,280))
        gameDisplay.blit(smallfont.render("Julius Ivan Baron N. Narvasa and John Gabriel Catarong are certified beginners in programming,",False,blue),(30,350))
        gameDisplay.blit(smallfont.render("who both worked hard for this game to be possible and 100% functional. This game is for project ",False,blue),(30,380))
        gameDisplay.blit(smallfont.render("use only. Parts of the games' code is refactored from youtube tutorials especially in menu part.",False,blue),(30,410))
        gameDisplay.blit(smallfont.render("Copyright of the games' code is prohibited unless developers names are acknowledged.",False,blue),(30,440))
        gameDisplay.blit(font.render("Back To Menu",False,blue), (700,640))
         
        pygame.draw.rect(gameDisplay,blue,controls_dot)
         
        pygame.display.update()
        clock.tick(25)

def game_intro():
    pygame.mixer.music.load("Menu.mp3")
    pygame.mixer.music.play(loops = 0, start = 0)
    intro = True    
    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    return 0
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        pygame.display.quit()
                        return 0
                    if event.key == pygame.K_UP:
                        if choice_dot.top == 265:
                            choice_dot.move_ip(0,200)
                        else:
                            choice_dot.move_ip(0,-50)
                    elif event.key == pygame.K_DOWN:
                        if choice_dot.top == 465:
                            choice_dot.move_ip(0,-200)
                        else:
                            choice_dot.move_ip(0,50)
                    elif event.key == pygame.K_RETURN:
                        if choice_dot.top == 265:
                            print("Play")
                            intro = False #Dare sya na part sa play
                            game_loop()
                        elif choice_dot.top == 315:
                            print("Winner") #mao nalang problema
                            display_winner()
                        elif choice_dot.top == 365:
                            controls()
                        elif choice_dot.top == 415:
                            game_credits()
                        elif choice_dot.top == 465:
                            print("Exit")
                            pygame.quit() #Exit na location
                            quit() 

        gameDisplay.fill(black)
        gameDisplay.blit(Tron_font.render("Tron Light Cycle~",False,blue), (100,15))
        gameDisplay.blit(font.render("Play",False,blue), (350,250))
        gameDisplay.blit(font.render("Who is the latest winner?",False,blue), (350,300))
        gameDisplay.blit(font.render("Controls / About Us",False,blue), (350,350))
        gameDisplay.blit(font.render("Credits",False,blue), (350,400))
        gameDisplay.blit(font.render("Exit",False,blue), (350,450))
        pygame.draw.rect(gameDisplay,blue,choice_dot)
        pygame.display.update()
        clock.tick(25)
        
def game_loop():
    #RESOLUTION
    width, height = 1000 , 700

    score = [0,0,0,0]

    def coll(x,y):
        coll = pygame.Rect.colliderect(x,y)
        return coll
    class P1T(object):    
        def __init__(self, pos):
            p1tempt.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
    class P2T(object):    
        def __init__(self, pos):
            p2tempt.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
    class P3T(object):    
        def __init__(self, pos):
            p3tempt.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
    class P4T(object):    
        def __init__(self, pos):
            p4tempt.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

    #CLOCK, BACKGROUND, MUSIC
    clock = pygame.time.Clock()
    background_image = pygame.image.load("TronBackground.jpg").convert()
    pygame.mixer.music.load("Albedo.mp3")

    win = False
    while win == False:
        #Wall arrays
        p1t = []
        p2t = []
        p3t = []
        p4t = []
        p1temp = []
        p2temp = []
        p3temp = []
        p4temp = []
        p1tempt = []
        p2tempt = []
        p3tempt = []
        p4tempt = []
        reps = 0
        
        #PLAYER 1 COORDINATES
        x1 , y1 = 30 , 30
        p1moving = True

        #PLAYER 2 COORDINATES
        x2 , y2 = width - 40 , 30
        p2moving = True

        #PLAYER 3 COORDINATES
        x3 , y3 = 30 , height - 40
        p3moving = True

        #PLAYER 4 COORDINATES
        x4 , y4 = width - 40 , height - 40
        p4moving = True


        #MOVEMENT STR (w-up, a-left, s-down, d-right)
        p1m = "s"
        p2m = "a"
        p3m = "d"
        p4m = "w"

        #COUNTDOWN TIMER
        for x in range(4):
            bg = gameDisplay.blit(background_image, [0,0])
            #Game Borders
            w_up = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,0,width,10))
            w_left = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,0,10,height))
            w_right = pygame.draw.rect(gameDisplay, (255,255,255) , pygame.Rect(width-10,0,10,height))
            w_down = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,height-10,width,10))
            #Player Initial Drawing
            p1hb = pygame.draw.rect(gameDisplay, blue, pygame.Rect(x1, y1, 10, 10))
            p2hb = pygame.draw.rect(gameDisplay, red, pygame.Rect(x2, y2, 10, 10))
            p3hb = pygame.draw.rect(gameDisplay, orange, pygame.Rect(x3, y3, 10, 10))
            p4hb = pygame.draw.rect(gameDisplay, violet, pygame.Rect(x4, y4, 10, 10))
            if x == 0:
                gameDisplay.blit(font.render("3",False,red), (490,340))
            if x == 1:
                gameDisplay.blit(largefont.render("2",False,red), (480,320))
            if x == 2:
                gameDisplay.blit(medlargefont.render("1",False,orange), (470,300))
            if x == 3:
                paused = False
            clock.tick(1)
            pygame.display.flip()

        #REDRAW BORDERS
        if score[0] == 0 and score[1] == 0 and score[2] == 0 and score[3] == 0:
            pygame.mixer.music.play(loops = 0, start = 3.5)
        bg = gameDisplay.blit(background_image, [0,0])
        w_up = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,0,width,10))
        w_left = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,0,10,height))
        w_right = pygame.draw.rect(gameDisplay, (255,255,255) , pygame.Rect(width-10,0,10,height))
        w_down = pygame.draw.rect(gameDisplay, (255,255,255), pygame.Rect(0,height-10,width,10))
                
        while paused == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    paused = True
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    return 0
                                                    
            #DRAW PLAYERS
            P1T((x1,y1))
            p1hb = pygame.draw.rect(gameDisplay, blue, pygame.Rect(x1, y1, 10, 10))
            for trail in p1t:
                pygame.draw.rect(gameDisplay, blue, trail.rect)
                                        
            P2T((x2,y2))
            p2hb = pygame.draw.rect(gameDisplay, red, pygame.Rect(x2, y2, 10, 10))
            for trail in p2t:
                pygame.draw.rect(gameDisplay, red, trail.rect)
                                        
            P3T((x3,y3))
            p3hb = pygame.draw.rect(gameDisplay, orange, pygame.Rect(x3, y3, 10, 10))
            for trail in p3t:
                pygame.draw.rect(gameDisplay, orange, trail.rect)
                                        
            P4T((x4,y4))
            p4hb = pygame.draw.rect(gameDisplay, violet, pygame.Rect(x4, y4, 10, 10))
            for trail in p4t:
                pygame.draw.rect(gameDisplay, violet, trail.rect)

            #DISPLAY SCORES
            gameDisplay.blit(font.render(str(score[0]),False,(255,255,255)), (50,40))
            gameDisplay.blit(font.render(str(score[1]),False,(255,255,255)), (940,40))
            gameDisplay.blit(font.render(str(score[2]),False,(255,255,255)), (50,620))
            gameDisplay.blit(font.render(str(score[3]),False,(255,255,255)), (940,620))

            #GET KEYPRESSES
            pressed = pygame.key.get_pressed()

            #PLAYER CONTROLS
            if p1moving == True:
                if pressed[pygame.K_w] and p1m != "s" and p1m != "w": p1m = "w"
                if pressed[pygame.K_a] and p1m != "d" and p1m != "a": p1m = "a"
                if pressed[pygame.K_s] and p1m != "w" and p1m != "s": p1m = "s"
                if pressed[pygame.K_d] and p1m != "a" and p1m != "d": p1m = "d"
            if p2moving == True:
                if pressed[pygame.K_UP] and p2m != "s" and p2m != "w": p2m = "w"
                if pressed[pygame.K_LEFT] and p2m != "d" and p2m != "a": p2m = "a"
                if pressed[pygame.K_DOWN] and p2m != "w" and p2m != "s": p2m = "s"                        
                if pressed[pygame.K_RIGHT] and p2m != "a" and p2m != "d": p2m = "d"
            if p3moving == True:
                if pressed[pygame.K_t] and p3m != "s" and p3m != "w": p3m = "w"
                if pressed[pygame.K_f] and p3m != "d" and p3m != "a": p3m = "a"
                if pressed[pygame.K_g] and p3m != "w" and p3m != "s": p3m = "s"                        
                if pressed[pygame.K_h] and p3m != "a" and p3m != "d": p3m = "d"
            if p4moving == True:
                if pressed[pygame.K_i] and p4m != "s" and p4m != "w": p4m = "w"
                if pressed[pygame.K_j] and p4m != "d" and p4m != "a": p4m = "a"
                if pressed[pygame.K_k] and p4m != "w" and p4m != "s": p4m = "s"                        
                if pressed[pygame.K_l] and p4m != "a" and p4m != "d": p4m = "d"
                                                                         
            #PlayerMoves
            if p1moving == True:
                if p1m == "w":
                    y1 -= 4
                if p1m == "a":
                    x1 -= 4
                if p1m == "s":
                    y1 += 4
                if p1m == "d":
                    x1 += 4
            if p2moving == True:
                if p2m == "w":
                    y2 -= 4
                if p2m == "a":
                    x2 -= 4
                if p2m == "s":
                    y2 += 4
                if p2m == "d":
                    x2 += 4
            if p3moving == True:
                if p3m == "w":
                    y3 -= 4
                if p3m == "a":
                    x3 -= 4
                if p3m == "s":
                    y3 += 4
                if p3m == "d":
                    x3 += 4
            if p4moving == True:
                if p4m == "w":
                    y4 -= 4
                if p4m == "a":
                    x4 -= 4
                if p4m == "s":
                    y4 += 4
                if p4m == "d":
                    x4 += 4
                                                                                        
            #CHECK COLLISION P2P
            if coll(p1hb,p2hb):
                p1moving = False
                p2moving = False
            if coll(p1hb,p3hb):
                p1moving = False
                p2moving = False
            if coll(p1hb,p4hb):
                p1moving = False
                p2moving = False
            if coll(p2hb,p3hb):
                p1moving = False
                p2moving = False
            if coll(p2hb,p4hb):
                p1moving = False
                p2moving = False
            if coll(p3hb,p4hb):
                p1moving = False
                p2moving = False

                        
            #CHECK COLLISION P2W
            if coll(p1hb,w_up) or coll(p1hb,w_left) or coll(p1hb,w_down) or coll(p1hb,w_right):
                p1moving = False
            if coll(p2hb,w_up) or coll(p2hb,w_left) or coll(p2hb,w_down) or coll(p2hb,w_right):
                p2moving = False
            if coll(p3hb,w_up) or coll(p3hb,w_left) or coll(p3hb,w_down) or coll(p3hb,w_right):
                p3moving = False
            if coll(p4hb,w_up) or coll(p4hb,w_left) or coll(p4hb,w_down) or coll(p4hb,w_right):
                p4moving = False

            #CHECK COLLISION P2T
            for trail in p1t:
                if coll(p1hb,trail.rect):
                    p1moving = False
                if coll(p2hb,trail.rect):
                    p2moving = False
                if coll(p3hb,trail.rect):
                    p3moving = False
                if coll(p4hb,trail.rect):
                    p4moving = False
            for trail in p2t:
                if coll(p1hb,trail.rect):
                    p1moving = False
                if coll(p2hb,trail.rect):
                    p2moving = False
                if coll(p3hb,trail.rect):
                    p3moving = False
                if coll(p4hb,trail.rect):
                    p4moving = False
            for trail in p3t:
                if coll(p1hb,trail.rect):
                    p1moving = False
                if coll(p2hb,trail.rect):
                    p2moving = False
                if coll(p3hb,trail.rect):
                    p3moving = False
                if coll(p4hb,trail.rect):
                    p4moving = False
            for trail in p4t:
                if coll(p1hb,trail.rect):
                    p1moving = False
                if coll(p2hb,trail.rect):
                    p2moving = False
                if coll(p3hb,trail.rect):
                    p3moving = False
                if coll(p4hb,trail.rect):
                    p4moving = False

            #TRAIL REPEAT
            reps += 1
            if reps == 4:
                p1t.extend(p1temp)
                p1temp = []
                p2t.extend(p2temp)
                p2temp = []
                p3t.extend(p3temp)
                p3temp = []
                p4t.extend(p4temp)
                p4temp = []
                p1temp.extend(p1tempt)
                p1tempt = []
                p2temp.extend(p2tempt)
                p2tempt = []
                p3temp.extend(p3tempt)
                p3tempt = []
                p4temp.extend(p4tempt)
                p4tempt = []
                reps = 0

            #CHECK LAST MAN
            if p1moving == True and p2moving == False and p3moving == False and p4moving == False:
                p1moving = False
                score[0] += 1
                paused = True
            if p1moving == False and p2moving == True and p3moving == False and p4moving == False:
                p2moving = False
                score[1] += 1
                paused = True
            if p1moving == False and p2moving == False and p3moving == True and p4moving == False:
                p3moving = False
                score[2] += 1
                paused = True
            if p1moving == False and p2moving == False and p3moving == False and p4moving == True:
                p4moving = False
                score[3] += 1
                paused = True
                                
            pygame.display.flip()
            clock.tick(60)
                
        for x in range(4):
            if score[x] == 5:
                if x == 0:
                    winner = blue
                if x == 1:
                    winner = red
                if x == 2:
                    winner = orange
                if x == 3:
                    winner = violet
                win = True
    create_highscore(winner)
    game_intro()
    return 0

def create_highscore(winner):
    running = True
    background_image = pygame.image.load("TronBackground.jpg").convert()
    name = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    return 0
                elif event.key == pygame.K_RETURN:
                    if name:
                        name = name.upper()
                        running = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[0:-1]
                else:
                    if not len(name) > 12:
                        name = name + event.unicode
        bg = gameDisplay.blit(background_image, [0,0])
        gameDisplay.blit(medfont.render("Congratualtions you won!",False,winner), (180,200))
        gameDisplay.blit(medfont.render("Enter name: ",False,winner), (180,300))
        gameDisplay.blit(medfont.render(name.upper(),False,winner), (390,300))
        pygame.display.flip()
        clock.tick(25)
    file = open('Player.txt','w')
    file.write(name)
    file.close()
    running = False
    
def display_winner():
    file = open('Player.txt','r')
    temp = file.read()
    file.close()
    winner = True
    while winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.display.quit()
                    return 0
                elif event.key == pygame.K_RETURN:
                    return 0 
        gameDisplay.fill(black)
        gameDisplay.blit(medlargefont.render("The latest winner is:",False,blue), (30,30))
        gameDisplay.blit(medlargefont.render(temp,False,blue), (300,300))
        gameDisplay.blit(font.render("Press enter to return to menu",False,blue), (600,640))
        pygame.display.update()
        clock.tick(25)

game_intro()
"""
while True:
    choice = game_intro()
    if choice == 1:
        game_loop()
    if choice == 2:
        controls()
    if choice == 3:
        game_credits()
"""
