import pygame
from network import Network
from player import Food
import os
pygame.font.init()


WIDTH,HEIGHT = 600,650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
R,C = 30, 30 # rows and columns

# Uploading an image
LOGO_SNAKE = pygame.image.load(os.path.join("static/images", "snake.png"))
pygame.display.set_icon(LOGO_SNAKE)
c = 0

def main():
    run = True
    clock = pygame.time.Clock()
    eaten = False
    n = Network()


    p1 = n.getP()
    food = n.getF()

    def eat_food(food_list, snake):
        for food in food_list:
            if food == snake[-1]:
                food_list.remove(food)
                return True
        return False
    
    def collision(players_snake, opponents_snake):
        winner = None
        if players_snake[-1] in opponents_snake:
            winner = "p2"
        if opponents_snake[-1] in players_snake:
            winner = "p1"

        for square in players_snake:
            if players_snake.count(square) > 1:
                winner = "p2"
            if square[0] > 29 or square[0] < 0 or square[1] > 29 or square[1] < 0:
                winner = "p2"
        for square in opponents_snake:
            if opponents_snake.count(square) > 1:
                winner = "p1"
            if square[0] > 29 or square[0] < 0 or square[1] > 29 or square[1] < 0:
                winner = "p1"

        

        return winner

    def draw_points(win, p1_points, p2_points):
        font = pygame.font.SysFont("comicsans", 30)
        text_1 = font.render(f"Your points: {p1_points}", True, (255,0,0))
        text_2 = font.render(f"Opponents points: {p2_points}", True, (255,0,0))
        win.blit(text_1, (20,(50 - text_1.get_height())/2))
        win.blit(text_2, (WIDTH - text_2.get_width() - 20,(50 - text_1.get_height())/2))





    def redrawWindow(win, p1, p2):
        global c
        win.fill((255,255,255))

        for i in range(R):
            pygame.draw.line(win,(75,74,71), (0 + 20*i,50), (20*i, HEIGHT + 50))
            pygame.draw.line(win,(75,74,71), (0,50 + 20*i), (WIDTH, 50 + 20*i)) 
        
        draw_points(win, p1.get_points(), p2.get_points())
        
        c += 1
        if c == 30:
            food.spawn_food(p1.snake, p2.snake)
            c = 0
        
        food.check_if_empty(p1.snake, p2.snake)
        food.draw(win)

        
        
        p1.move(eaten)

        p1.draw(win)
        p2.draw(win)


    

        pygame.display.update()


    while run:
        clock.tick(10)
        p2 = n.send(p1)
        p1.ready = True
        print(p2.ready, p1.ready)

        if p1.ready and p2.ready:


            if p2.winner or p1.winner:
                break

            redrawWindow(WIN,p1,p2)

            if collision(p1.snake, p2.snake):
                winner = collision(p1.snake, p2.snake)
                if winner == "p2":
                    p2.winner = True
                else:
                    p1.winner = True
                break
                    

            eaten = eat_food(food.food, p1.snake)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and p1.dir != "D":
                p1.dir = "U"
            if keys[pygame.K_s] and p1.dir != "U":
                p1.dir = "D"
            if keys[pygame.K_a] and p1.dir != "R":
                p1.dir = "L"
            if keys[pygame.K_d] and p1.dir != "L":
                p1.dir = "R"
        else:
            WIN.fill((255,255,255))
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Waiting for opponent!",True, (0,0,0))
            WIN.blit(text, ((WIDTH - text.get_width())/2, (HEIGHT - text.get_height())/2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            pygame.display.update()

    run = True
    while run:
        clock.tick(60)
        WIN.fill((255,255,255))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play again!", True, (51,0,0))

        if p1.winner == True:
            text1 = font.render("You Won!", True, (51,0,0))
        else:
            text1 = font.render("You Lost!", True, (51,0,0))

        WIN.blit(text, ((WIDTH - text.get_width())/2, 220))
        WIN.blit(text1, ((WIDTH - text1.get_width())/2, 150))
        pygame.display.update()

        p1.winner = False
        p2.winner = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

def game():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill((255,255,255))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", True, (51,0,0))
        WIN.blit(text, ((WIDTH - text.get_width())/2, (HEIGHT - text.get_height())/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()
        

while True:
    game()