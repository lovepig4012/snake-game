class Snake:
    def __init__(self):
        # 初始位置设置为10的倍数
        self.positions = [(0, 0)]
        self.direction = (1, 0)  # Start moving to the right
        self.grow_flag = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        # 确保蛇的移动是按10像素为单位的
        new_head = (head_x + dir_x * 10, head_y + dir_y * 10)
        self.positions.insert(0, new_head)
        if not self.grow_flag:
            self.positions.pop()
        else:
            self.grow_flag = False

    def grow(self):
        self.grow_flag = True

    def get_positions(self):
        return self.positions

    def set_direction(self, new_direction):
        # Prevent the snake from reversing
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction