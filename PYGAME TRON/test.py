import pygame
pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tron Menu')
clock = pygame.time.Clock()

Exit = False

#messageDisplay
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def text_objects(text,Font):
     textSurface = font.render(text,True,black)
     return textSurface.get_rect()

def message_display(text):
     largeText = pygame.font.Font('freesansbold.tty',155)
     TextSurf,TextRect = text_objects(text,largeText)
     TextRect.center = ((display_width/2),(display_height/2))
     gameDisplay.blit(TextSurf , TextRect)

     pygame.display.update()
     time.sleep(2)

     game_loop()
def gameOver():
     message_Display('Game Over Racers') 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def game_loop():
     while not Exit:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    Exit = True
               print(gameOver)

     pygame.display.update()

     clock.tick(60)


pygame.quit()
quit()
