import pygame
import random
from datetime import datetime
from datetime import timedelta

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

RED = 255, 0, 0
GREEN = 0, 255, 0
WHITE = 255, 255, 255

TURN_INTERVAL = timedelta(seconds=0.3)


class Snake:
    """뱀 클래스"""
    color = GREEN

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]
        self.direction = 'north'

    def draw(self, screen):
        """뱀을 화면에 표시"""
        for position in self.positions:
            draw_block(screen, self.color, position)

    def crawl(self):
        """뱀이 현재 방향으로 한칸 기어간다."""
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y-1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y+1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x-1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x+1)] + self.positions[:-1]

    def turn(self, direction):
        """뱀의 방향전환"""
        self.direction = direction

    def grow(self):
        """뱀이 한칸 자라난다"""
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y-1, x))
        elif self.direction == 'south':
            self.positions.append((y+1, x))
        elif self.direction == 'west':
            self.positions.append((y, x-1))
        elif self.direction == 'east':
            self.positions.append((y, x+1))


class Apple:
    """사과 클래스"""
    color = RED

    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self, screen):
        """사과를 화면에 표시"""
        draw_block(screen, self.color, self.position)


class GameBoard:
    """게임판 클래스"""
    width = 20
    height = 20

    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def draw(self, screen):
        """화면에 게임판을 표시"""
        self.apple.draw(screen)
        self.snake.draw(screen)

    def process_turn(self):
        """게임을 진행한다"""
        self.snake.crawl()

        # 뱀의 머리위치
        head_position = self.snake.positions[0]

        # 뱀의 머리와 몸이 부딛히면
        if head_position in self.snake.positions[1:]:
            raise SnakeCollisionException()

        # 게임판 밖으로 나가면
        y, x = head_position
        # print("head position x{}, y{}".format(x, y))
        if x < 0 or x >= self.width or y < 0 or y > self.height:
            raise SnakeCollisionException()

        # 뱀의 머리와 사과가 닿으면
        if head_position == self.apple.position:
            # print("snake")
            # print(head_position)
            # print("apple")
            # print(self.apple.position)
            self.snake.grow()
            self.put_new_apple()

    def put_new_apple(self):
        """게임판에 새 사과를 놓는다"""
        self.apple = Apple((random.randint(0, 19), random.randint(0, 19)))
        for position in self.snake.positions:
            if self.apple.position == position:
                self.put_new_apple()
                break


class SnakeCollisionException(Exception):
    """뱀 충돌 예외"""
    pass


def draw_background(screen):
    """게임의 배경"""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):
    """position 위치에 color의 블록을 그린다"""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east'
}
last_turn_time = datetime.now()

game_board = GameBoard()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in DIRECTION_ON_KEY:
                game_board.snake.turn(DIRECTION_ON_KEY[event.key])

    if TURN_INTERVAL < datetime.now() - last_turn_time:
        try:
            game_board.process_turn()
        except SnakeCollisionException:
            exit()
        last_turn_time = datetime.now()

    draw_background(screen)
    game_board.draw(screen)
    pygame.display.update()
