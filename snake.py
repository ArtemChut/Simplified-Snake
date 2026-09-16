import pygame
from pygame.locals import *
import sys
import random
import time



""" --------------------------
    | USE ARROW KEYS TO MOVE |
    --------------------------
"""


def main(mode):
    pygame.init()
    screen = pygame.display.set_mode((920,640))

    font = pygame.font.SysFont("couriernew", 28)


    class Snake:
        snake_pieces = []
        def __init__(self, colour, x, y):
            self.x = x
            self.y = y
            self.size = 40
            self.colour = colour
            Snake.snake_pieces.append(self)

        def draw(self):
            pygame.draw.rect(screen, self.colour, (self.x,self.y, self.size,self.size))

        def collision(self):
            snake = pygame.Rect(self.x,self.y, self.size,self.size)

            for prize_ in Prize.prizes:
                prize = pygame.Rect(prize_.x,prize_.y, prize_.size,prize_.size)
                if snake.colliderect(prize):
                    Snake("yellow", before_movement[-1][0], before_movement[-1][1])
                    Prize.prizes.remove(prize_)
                    
                    if len(Snake.snake_pieces) == screen.get_height()//40*screen.get_width()//40:
                        won_text = font.render("You won!!", False, "green") # displying u won message
                        screen.blit(won_text, (920//2-60,640//2-20))
                        pygame.display.update()
                        time.sleep(3)

                        import snake
                        snake.main()
                        return # exit
                    else:
                        Prize().spawn()
                    break

            for i,snake_piece in enumerate(Snake.snake_pieces):
                if i != 0: # if not the head
                    if snake.x == snake_piece.x and snake.y == snake_piece.y:
                        display_lost_message()
        
        def move(self):
            if direction == "up":
                Snake.snake_pieces[0].y -= 40
            elif direction == "down":
                Snake.snake_pieces[0].y += 40
            elif direction == "right":
                Snake.snake_pieces[0].x += 40
            else:
                Snake.snake_pieces[0].x -= 40

            if mode == "hard":
                if Snake.snake_pieces[0].x <= -40:
                    display_lost_message()
                elif Snake.snake_pieces[0].x >= screen.get_width():
                    display_lost_message()
                elif Snake.snake_pieces[0].y <= -40:
                    display_lost_message()
                elif Snake.snake_pieces[0].y >= screen.get_height():
                    display_lost_message()
            else:
                if Snake.snake_pieces[0].x <= -40:
                    Snake.snake_pieces[0].x = screen.get_width()-40
                elif Snake.snake_pieces[0].x >= screen.get_width():
                    Snake.snake_pieces[0].x = 0
                elif Snake.snake_pieces[0].y <= -40:
                    Snake.snake_pieces[0].y = screen.get_height()-40
                elif Snake.snake_pieces[0].y >= screen.get_height():
                    Snake.snake_pieces[0].y = 0

    Snake("blue", 120, 200) # head of the snake
    Snake("yellow", 80, 200) # piece of a tail


    def display_lost_message():
        lost_text = font.render("You lost", False, "red") # displying u lost message
        screen.blit(lost_text, (920//2-60,640//2-20))
        pygame.display.update()
        time.sleep(3)

        import snake_menu
        snake_menu.main()
        return #exit


    class Prize:
        prizes = []
        def __init__(self):
            self.x = random.randint(0, int((screen.get_width()-40)/40))*40
            self.y = random.randint(0, int((screen.get_height()-40)/40))*40
            self.colour = "green"
            self.size = 40

        def spawn(self):
            prize = pygame.Rect(self.x,self.y, self.size,self.size)

            collides = True
            while collides:
                collides = False
                for snake_piece_ in Snake.snake_pieces:
                    snake_piece = pygame.Rect(snake_piece_.x,snake_piece_.y, snake_piece_.size,snake_piece_.size)
                    if prize.colliderect(snake_piece):
                        prize.x = random.randint(0, int((screen.get_width()-40)/40))*40
                        prize.y = random.randint(0, int((screen.get_height()-40)/40))*40
                        collides = True
            self.x = prize.x
            self.y = prize.y
            Prize.prizes.append(self)
        def draw(self):
            pygame.draw.rect(screen, self.colour, (self.x,self.y, self.size,self.size))

    Prize().spawn()


    direction = "right"
    last_time = pygame.time.get_ticks()
    while True:
        screen.fill("black")

        current_time = pygame.time.get_ticks()
        # move only every 0.15 seconds
        if current_time - last_time >= 150:
            before_movement = []
            for snake_piece in Snake.snake_pieces:
                before_movement.append([snake_piece.x,snake_piece.y])

            Snake.snake_pieces[0].move()

            # moving the tail
            for i,snake_piece in enumerate(Snake.snake_pieces):
                if i != 0: # if not the head
                    snake_piece.x = before_movement[i-1][0]
                    snake_piece.y = before_movement[i-1][1]

            last_time = current_time


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    import snake_menu
                    snake_menu.main()
                    return # exit
                
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left": # making sure that ther player can't just turn around 180 degrees
                    direction = "right"
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                    direction = "left"
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                    direction = "up"
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                    direction = "down"

        # CHECKING IF SNAKE ATE ANY FRUITS OR ATE ANY FRUITS
        Snake.snake_pieces[0].collision()
            

        for snake_piece in Snake.snake_pieces:
            snake_piece.draw()
        for prize in Prize.prizes:
            prize.draw()


        pygame.display.update()
        pygame.time.Clock().tick(60)



    pygame.display.update()
    pygame.time.Clock().tick(60)
