import pygame

# initialising window

x = pygame.init()  # it return a tuple which tell how many module are initializes and how many are left not initialized
# print(x)  // their is no need to initialise it with name we can directly initialise it as well

# creating window

gameWindow = pygame.display.set_mode((1200, 500))  # this will provide us with a display and here are length and
# breath are provide of window
pygame.display.set_caption("My First Game")  # it will write a given string to the display title or name of game

# Game Specific variables :- we have made them so if someone exits the game or game over the use this variables
exit_game = False
game_over = False

# Creating a game loop :- it will help us to keep our window open

while not exit_game:
    for event in pygame.event.get():  # it can take any possible event like key press mouse position etc
        # print(event)  # will print all event done by user

        if event.type == pygame.QUIT:  # Check if we have tried to close the window by pressing [x] from the top bar
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")

            if event.key == pygame.K_LEFT:
                print("You have pressed left arrow key")


pygame.quit()  # when while loop is stop then to quit the game
quit()
