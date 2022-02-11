# created on 22 May 2021, 10:14 AM

import random
import pygame
import sys
pygame.init()

# general setup
pygame.display.set_caption("Bouncy")
WIDTH = 600
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LIGHT_BLUE = (102, 178, 255)
pygame.mouse.set_visible(False)

class Ball:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed_x = 3
        self.speed_y = 5


    def draw_ball(self):
        self.ball_move()
        self.collision()
        pygame.draw.ellipse(SCREEN, LIGHT_BLUE, (self.x, self.y, self.width, self.height))

    def ball_move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.width >= WIDTH or self.x <= 0: # if ball hitting right/left wall, bounce ball back
            self.speed_x *= -1

        if self.y <= 0:
            self.speed_y *= -1 # if ball hitting top screen, bounce ball back

        if self.y + self.height > HEIGHT: # if player can't catch a ball, ball will start again at random position at beginning speed
            player.lives -= 1
            self.x = WIDTH/2
            self.y = HEIGHT/2
            self.speed_x = 3
            self.speed_y = 3
            self.speed_x *= random.choice((1,-1))
            self.speed_y *= random.choice((1,-1))


    def collision(self):

        # ball collide with player, make ball bounce up
        if pygame.Rect(ball.x, ball.y, ball.width, ball.height).colliderect(pygame.Rect(player.x, player.y, player.width, player.height)):

            self.speed_y *= -1
            self.speed_x *= random.choice((-1.2,1.2))

        # ball collide with red ball, ball speed will go 1.5
        if pygame.Rect(ball.x, ball.y, ball.width, ball.height).colliderect(pygame.Rect(red_ball.x, red_ball.y, red_ball.width, red_ball.height)):
            self.speed_x *= -1
            self.speed_y *= -1

        # ball collide with yellow ball, score + 1
        if pygame.Rect(ball.x, ball.y, ball.width, ball.height).colliderect(
                pygame.Rect(yellow_ball.x, yellow_ball.y, yellow_ball.width, yellow_ball.height)):
            self.speed_x *= -1
            self.speed_y *= -1
            score.player_score += 1
            if score.player_score % 5 == 0:
                score.level += 1

        # ball collide with green ball, ball speed back to normal speed
        if pygame.Rect(ball.x, ball.y, ball.width, ball.height).colliderect(
            pygame.Rect(green_ball.x, green_ball.y, green_ball.width, green_ball.height)):
            self.speed_x *= -1
            self.speed_x = 3
            self.speed_y *= -1
            self.speed_y = 3

class Player:
    def  __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 5
        self.lives = 3

    def draw_player(self):
        self.player_move()
        pygame.draw.rect(SCREEN, LIGHT_BLUE, (self.x, self.y, self.width, self.height))

    def player_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.width < WIDTH:
            self.x += self.vel

class Red: # (red ball) if ball collide with object, ball speed will be + 1
    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_speed = 3
        self.y_speed = 3

    def draw_object(self):
        red_ball.red_move()
        pygame.draw.ellipse(SCREEN, (255,0,0), (self.x, self.y, self.width, self.height))

    def red_move(self):
            if score.level == 1:
                self.x += self.x_speed
                self.y += self.y_speed
                if self.x + self.width >= WIDTH or self.x < 0:
                    self.x_speed *= -1
                if self.y + self.height >= HEIGHT or self.y < 0:
                    self.y_speed *= -1

            elif score.level == 2:
                yellow_ball.yellow_move()
                self.x += self.x_speed
                self.y += self.y_speed
                if self.x + self.width >= WIDTH or self.x < 0:
                    self.x_speed *= -1
                if self.y + self.height >= HEIGHT or self.y < 0:
                    self.y_speed *= -1


class Green: # (green ball) to slow down speed by 0.5
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.level_state = False

    def draw_green_ball(self):
        pygame.draw.ellipse(SCREEN, (0,153,76), (self.x, self.y, self.width, self.height))

class Yellow:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_speed = 3
        self.y_speed = 3

    def draw_yellow_ball(self):
        pygame.draw.ellipse(SCREEN, (204, 204, 0), (self.x, self.y, self.width, self.height))

    def yellow_move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x + self.width >= WIDTH or self.x < 0:
            self.x_speed *= -1
        if self.y + self.height >= HEIGHT or self.y < 0:
            self.y_speed *= -1

class Score:
    def __init__(self):
        self.player_score = 0
        self.level = 0


    def draw_score(self):
        score_text = pygame.font.SysFont("comicsans", 30)
        score_text = score_text.render(f"Score: {self.player_score}", True, (255,255,255))

        level_text = pygame.font.SysFont("comicsans", 30)
        level_text = level_text.render(f"Level: {self.level}", True, (255,255,255))

        lives_text = pygame.font.SysFont("comicsans", 30)
        lives_text = lives_text.render(f"Lives: {player.lives}", True, (255,255,255))

        SCREEN.blit(score_text, (10, 10))
        SCREEN.blit(level_text, (WIDTH/2 - level_text.get_width()/2, 12))
        SCREEN.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))


def display_message(message):
    SCREEN.fill((0,0,0))
    game_over_text = pygame.font.SysFont("comicsans", 50)
    game_over_text = game_over_text.render(message, True, (255,255,255))
    SCREEN.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2 - game_over_text.get_height()/2))
    pygame.display.update()


ball = Ball(280, 180, 20, 20)
player = Player(WIDTH/2 - 50, 380, 100, 10)
red_ball = Red(100, 100, 40, 40)
green_ball = Green(500, 50, 30, 30)
yellow_ball = Yellow(100, 200, 30, 30)
score = Score()

def main_intro():
    pygame.time.Clock().tick(60)

    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_game()

        if score.level >= 3:
            intro = False
            break

        display_message("Press SPACE to continue")
        pygame.display.update()


def main_game():
    run = True
    while run:
        pygame.time.Clock().tick(60)

        def draw_window():
            SCREEN.fill((0,0,0))
            ball.draw_ball()
            player.draw_player()
            red_ball.draw_object()
            green_ball.draw_green_ball()
            yellow_ball.draw_yellow_ball()
            score.draw_score()

            pygame.display.update()

        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        draw_window()

        if player.lives < 0:
            display_message("You Lost! Try Again")
            pygame.time.delay(3000)
            player.lives = 3
            score.player_score = 0
            score.level = 0
            run = False
            main_intro()

        if score.level >= 3:
            display_message("You Win!!")
            pygame.time.delay(3000)
            run = False
            break

main_intro()