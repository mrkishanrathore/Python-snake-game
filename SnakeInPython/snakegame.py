import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

exit_game = False
game_over = False
snake_x = 45
snake_y = 55
init_velocity = 5
velocity_x = init_velocity
velocity_y = 0
snake_size = 20
snake_length = 1
snake_list = []
score = 0
food_radius = 10
fps = 30


def plot_snake(window, color, snk_list, size_snake):
    for i in range(0, len(snk_list)):
        pygame.draw.rect(window, color, [snk_list[i][0], snk_list[i][1], size_snake, size_snake])


def show_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


food_x = random.randint(50, screen_width - 20)
food_y = random.randint(20, screen_height - 20)
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if not velocity_x == -init_velocity:
                    velocity_x = init_velocity
                    velocity_y = 0
            if event.key == pygame.K_LEFT:
                if not velocity_x == init_velocity:
                    velocity_x = -init_velocity
                    velocity_y = 0
            if event.key == pygame.K_UP:
                if not velocity_y == init_velocity:
                    velocity_x = 0
                    velocity_y = -init_velocity
            if event.key == pygame.K_DOWN:
                if not velocity_y == -init_velocity:
                    velocity_x = 0
                    velocity_y = init_velocity

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        food_x = random.randint(50, screen_width - 20)
        food_y = random.randint(20, screen_height - 20)
        score = score + 1
        snake_length = snake_length + 5
        if score % 5 == 0:
            init_velocity = init_velocity + 1
        print("Score : ", score * 10)

    gameWindow.fill(white)
    show_text("Score :- " + str(score * 10), black, 10, 10)

    head = [snake_x, snake_y]
    snake_list.append(head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    plot_snake(gameWindow, green, snake_list, snake_size)
    pygame.draw.circle(gameWindow, red, [food_x, food_y], food_radius)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
