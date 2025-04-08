import pygame
import logging
from snake import Snake
from food import Food

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.snake = Snake()
        # 确保食物生成在有效的网格位置上
        self.food = [Food(self.width, self.height) for _ in range(3)]  # Spawn 3 food items
        self.score = 0
        self.is_running = True
        self.speed = 4  # 降低初始速度

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.snake.set_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                self.snake.set_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                self.snake.set_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                self.snake.set_direction((1, 0))
            elif event.key == pygame.K_ESCAPE:  # 添加 ESC 键退出功能
                self.is_running = False

    def update(self):
        self.snake.move()
        # Check for collisions with food
        head_pos = self.snake.get_positions()[0]
        for i, food_item in enumerate(self.food):
            food_pos = food_item.get_position()
            # 改进碰撞检测，确保坐标完全匹配
            if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
                # 碰撞检测成功，蛇吃到食物
                self.snake.grow()  # 确保蛇变长
                food_item.respawn()
                self.score += 1  # 确保分数增加
                # 每5分时速度+1，最大速度15
                if self.score % 5 == 0 and self.speed < 15:
                    self.speed += 1
        # Check for collisions with walls or itself
        head_x, head_y = self.snake.get_positions()[0]
        if (
            head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height or
            len(self.snake.get_positions()) != len(set(self.snake.get_positions()))
        ):
            self.is_running = False

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        # Draw the snake
        for segment in self.snake.get_positions():
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, 10, 10))
        # Draw all food items
        for food_item in self.food:
            pygame.draw.rect(self.screen, (255, 0, 0), (*food_item.get_position(), 10, 10))
        # Draw the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))