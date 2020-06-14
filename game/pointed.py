import sys, pygame, math
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WHITE = (255,255,255)
BLACK = (0,0,0)
BGCOLOR = (255,255,255)

pygame.init()
displaywin = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

#이미지 만들기
tankimg = pygame.image.load("myimage.jpg")

#각도구하기
def catchAngle(x1,y1,x2,y2):
    y = y1-y2
    x = x1-x2
    angle = math.atan2(x,y)
    angle = angle * (180/math.pi) #라디안값을 각도로 변경
    angle = (angle + 90) %360 #이미지의 각도 조정
    return angle

#메인루프
while True:
    #이벤트 핸들링
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    #배경색 칠하기
    displaywin.fill(BGCOLOR)

    #마우스 위치
    mousex, mousey = pygame.mouse.get_pos()

    #탱크 위치
    for tankx, tanky in ((200,150), (50,300), (50,50), (200,400)):
        degrees = catchAngle(tankx,tanky,mousex,mousey)
        #탱크 회전
        rotatedtank = pygame.transform.rotate(tankimg, degrees)
        rotateRect = rotatedtank.get_rect()
        rotateRect.center = (tankx,tanky)

        #이미지를 화면에 그려준다.
        displaywin.blit(rotatedtank, rotateRect)

    #마우스 화살표 그려주기
    pygame.draw.line(displaywin, BLACK, (mousex-10, mousey), (mousex+10, mousey))
    pygame.draw.line(displaywin, BLACK, (mousex, mousey-10), (mousex, mousey+10))

    pygame.display.update()
