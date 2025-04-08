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

    # 添加键盘状态检测，提高输入响应性
    last_key_state = None
    
    while game.is_running:  # 修改为检查 game.is_running
        # 处理所有事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 仍然保留事件处理，用于ESC键等特殊按键
            game.handle_input(event)
        
        # 获取当前键盘状态，实现更快的响应
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            game.snake.set_direction((0, -1))
        elif keys[pygame.K_DOWN]:
            game.snake.set_direction((0, 1))
        elif keys[pygame.K_LEFT]:
            game.snake.set_direction((-1, 0))
        elif keys[pygame.K_RIGHT]:
            game.snake.set_direction((1, 0))
            
        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(game.speed)  # 使用动态速度控制帧率
    pygame.quit()  # 游戏结束时退出
    sys.exit()

if __name__ == '__main__':
    main()