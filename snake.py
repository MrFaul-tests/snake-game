import random


class Apple:
    
    def __init__(self, position=None):
        if position is None:
            position = [10, 10]
        self.position = position

    def respawn(self, cords=[1, 20]):
        self.position = [random.randint(1, cords[0]), random.randint(1, cords[1])]

    
    def get_position(self):
        return self.position
    

    

class Snake:

    def __init__(self, body=None, direction='right', size=(200, 200)):
        if body is None:
            body = [[5, 5], [5, 4], [5, 3], [5, 2], [5, 1]]
        self.body = body
        self.direction = direction
        self.size = size


    def move(self):
        if self.direction == 'right':
            new_head = [self.body[0][0], self.body[0][1] + 1]
        elif self.direction == 'left':
            new_head = [self.body[0][0], self.body[0][1] - 1]
        elif self.direction == 'up':
            new_head = [self.body[0][0] - 1, self.body[0][1]]
        elif self.direction == 'down':
            new_head = [self.body[0][0] + 1, self.body[0][1]]
        
        if new_head[0] < 0:
            new_head[0] = self.size[0] - 1
        elif new_head[0] >= self.size[0]:
            new_head[0] = 0
        if new_head[1] < 0:
            new_head[1] = self.size[1] - 1
        elif new_head[1] >= self.size[1]:
            new_head[1] = 0
        
        
        self.body.insert(0, new_head)
        self.body.pop()  # удаляем последний сегмент змейки


    def apple_eaten(self):
        tail = self.body[-1]
        self.body.append(tail)  # добавляем новый сегмент в конец змейки


    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        return False
    
