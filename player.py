import pygame
import random

class Player:
    def __init__(self, snake, color, dir):
        self.snake = snake  #cordinates [(x,y),...] x = row y = column
        self.dir = dir # moving direction "U", "D", "L", "R"
        self.color = color
        self.points = len(snake)
        self.winner = False
        self.ready = False

    def draw(self, win):
        for square in self.snake:
            pygame.draw.rect(win, self.color, (square[0] * 20, square[1] * 20 + 50, 20, 20)) # 10 one square height and width

    def move(self, eaten):
        if self.dir == "R":
            self.snake.append((self.snake[-1][0]+1,self.snake[-1][1]))
            if eaten == False:
                self.snake.pop(0)
        if self.dir == "L":
            self.snake.append((self.snake[-1][0]-1,self.snake[-1][1]))
            if eaten == False:
                self.snake.pop(0)
        if self.dir == "U":
            self.snake.append((self.snake[-1][0],self.snake[-1][1]-1))
            if eaten == False:
                self.snake.pop(0)
        if self.dir == "D":
            self.snake.append((self.snake[-1][0],self.snake[-1][1] + 1))
            if eaten == False:
                self.snake.pop(0)

    def get_points(self):
        points = len(self.snake)
        return points

class Food:
    def __init__(self, food):
        self.food = food #cordinates [(x,y),...] x = row y = column
        self.color = (238,162,30)

    def draw(self, win):
        for square in self.food:
            pygame.draw.rect(win, self.color, (square[0] * 20, square[1] * 20 + 50, 20, 20))

    def spawn_food(self, p1_snake, p2_snake):
        while True: 
            f_p = (random.randint(0,29), random.randint(0,29))

            if (f_p not in p1_snake) and (f_p not in p2_snake):
                self.food.append(f_p)
                break
    
    def check_if_empty(self, p1_snake, p2_snake):
        if not self.food:
            while True: 
                f_p = (random.randint(0,29), random.randint(0,29))

                if (f_p not in p1_snake) and (f_p not in p2_snake):
                    self.food.append(f_p)
                    break
