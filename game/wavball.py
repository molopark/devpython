import sys, pygame, math
from pygame.locals import *

BRIGHTBLUE = (0,50,255)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BGCOLOR = (255,255,255)

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WIN_CENTERX = int(WINDOWWIDTH/2)
WIN_CENTERY = int(WINDOWHEIGHT/2)
#초당프레임수
FPS = 60
AMPLITUDE = 100

pygame.init()
FPSCLOCK = pygame.time.Clock()
displaywin = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

#메인루프
step = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    #배경을 칠한다.
    displaywin.fill(BGCOLOR)

    #푸른색 공을 그려준다.
    #움직이는 공 그리기 math.sin()
    yPos = -1 * math.sin(step) * AMPLITUDE
    pygame.draw.circle(displaywin, BRIGHTBLUE, (int(WINDOWWIDTH*0.333),int(yPos)+WIN_CENTERY), 40)

    #붉은색 공을 그려준다.
    yPos = -1 * abs(math.sin(step)) * AMPLITUDE
    pygame.draw.circle(displaywin, RED, (int(WINDOWWIDTH*0.666),int(yPos)+WIN_CENTERY), 40)

    #디스플레이 업데이트를 한다.
    pygame.display.flip()
    step += 0.02

    FPSCLOCK.tick(FPS)
