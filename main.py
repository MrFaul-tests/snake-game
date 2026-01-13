import keyboard
import time
import os, sys
from snake import Snake, Apple
from out import Drawing
from threading import Thread


size = os.get_terminal_size()
snake = Snake(size=(size.lines, size.columns))
apple = Apple()
draw = Drawing()


def check_keys():
    while True:
        #print(keyboard.read_key())
        if keyboard.is_pressed('down'):
            if snake.direction != 'up':
                snake.direction = 'down'
        elif keyboard.is_pressed('up'):
            if snake.direction != 'down':
                snake.direction = 'up'
        elif keyboard.is_pressed('left'):
            if snake.direction != 'right':
                snake.direction = 'left'
        elif keyboard.is_pressed('right'):
            if snake.direction != 'left':
                snake.direction = 'right'


key_thread = Thread(target=check_keys)
key_thread.daemon = True
key_thread.start()


while True:
    snake.move()

    if snake.body[0] == apple.get_position():
        snake.apple_eaten()
        apple.respawn(cords=[size.lines - 1, size.columns - 1])

    draw.draw(snake.body, apple.get_position(), [size.lines, size.columns])
    if snake.check_collision():
        print("Game Over!")
        break
    #sys.stdout.write('\033[H')
    time.sleep(0.05)


