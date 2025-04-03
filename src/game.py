import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.snake = Snake()
        self.food = Food(self.width, self.height)
        self.score = 0
        self.is_running = True
        self.speed = 10  # 初始速度

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
        if self.snake.get_positions()[0] == self.food.get_position():
            self.snake.grow()  # 确保蛇变长
            self.food.respawn()
            self.score += 1  # 确保分数增加
            self.speed += 1  # 每次吃到食物后加快速度
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
        # Draw the food
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food.get_position(), 10, 10))
        # Draw the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))