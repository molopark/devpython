import pygame
pygame.init()
display_width = 800
display_height = 600

ourScreen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("파이게임")

#music
#pygame.mixer.music.load('xxx.mp3')
#pygame.mixer.music.play(loops=0)

#IMAGE
myimg = pygame.image.load('myimage.jpg')
def myImg(x,y):
    ourScreen.blit(myimg,(x,y))

x = (display_width * 0.5)
y = (display_height * 0.5)

#RECT
#colorBlue = True
#x = 30
#y = 30

finish = False
#clock = pygame.time.Clock()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

#RECT
#        ourScreen.fill((0,0,0))
#        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#            colorBlue = not colorBlue
#        pressed = pygame.key.get_pressed()
#        if pressed[pygame.K_UP]: y -= 3
#        if pressed[pygame.K_DOWN]: y += 3
#        if pressed[pygame.K_LEFT]: x -= 3
#        if pressed[pygame.K_RIGHT]: x += 3
#        ourScreen.fill((0,0,0))
#        if colorBlue: color = (0,128,255)
#        else: color = (255,255,255)
#        pygame.draw.rect(ourScreen, color, pygame.Rect(x,y,60,60))

#IMAGE
    ourScreen.fill((0,0,0))
    myImg(x,y)

    pygame.display.flip()
#    clock.tick(60)
pygame.quit()
quit()
