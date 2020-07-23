import os
import pygame

# 기본초기화
pygame.init()

# 화면크기설정
screen_width = 640
screen_height = 480
screeen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀설정
pygame.display.set_caption("pang pang")

# FPS
clock = pygame.time.Clock()

# 1.게임초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "image")

# 배경화면
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터이동방향
character_to_x = 0

# 캐릭터이동속도
character_speed = 5

# 무기만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기발사
weapons = []
weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2.이벤트처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    # 3. 게임캐릭터위치정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # print("character_x_pos:{} , character_y_pos:{}".format(character_x_pos, character_y_pos))

    # 무기위치
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 4. 충돌처리

    # 5. 화면그리기
    screeen.blit(background, (0,0))
    screeen.blit(stage, (0, screen_height - stage_height))
    screeen.blit(character, (character_x_pos, character_y_pos))

    for weapon_x_pos, weapon_y_pos in weapons:
        screeen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    pygame.display.update()

pygame.quit()
