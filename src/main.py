import pygame
import sys
from snake import Snake
from food import Food
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    game = Game(screen)  # 确保只传递 screen 参数

    while game.is_running:  # 修改为检查 game.is_running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.handle_input(event)

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(game.speed)  # 使用动态速度控制帧率
    pygame.quit()  # 游戏结束时退出
    sys.exit()

if __name__ == '__main__':
    main()