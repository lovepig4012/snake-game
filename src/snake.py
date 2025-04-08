class Snake:
    def __init__(self):
        # 初始位置设置为5的倍数，以实现更平滑的移动
        self.positions = [(0, 0)]
        self.direction = (1, 0)  # Start moving to the right
        self.grow_flag = False
        self.move_distance = 5  # 每次移动5个像素，使移动更平滑

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        # 使用较小的移动单位，使移动更平滑
        new_head = (head_x + dir_x * self.move_distance, head_y + dir_y * self.move_distance)
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