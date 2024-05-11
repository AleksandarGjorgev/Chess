from const import *
import time


run_game = True
run = True

while run:
    screen.fill("dark gray")
    choice = startup_window(800, 400, "Welcome to Blind Chess", "Pick a starting side")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if choice:
        run = False


    pygame.display.flip()


while run_game:  # Infinite loop to keep the game running
    timer.tick(fps)
    screen.fill("Dark gray")
    draw_board(choice)
    draw_pieces(choice)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    pygame.display.flip()

pygame.quit()
