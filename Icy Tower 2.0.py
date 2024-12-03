import pygame

pygame.init()

screen = pygame.display.set_mode((500, 700))
screen.fill("white")
pygame.display.set_caption("Blocky Tower")
clock = pygame.time.Clock()
score_font = pygame.font.Font(None, 50)
background = pygame.image.load("imgs/Background.jpg")
player = pygame.Surface((50,50))
player.fill("Black")
player_x_pos = 250
score = score_font.render("0", False, "Black")


while True:
    # Wyjscie z gry
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(background, (0,0))
    # Sterowanie graczem
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x_pos -= 10
                if player_x_pos < 0:
                    player_x_pos = 500
    screen.blit(player, (player_x_pos,650))
    screen.blit(score, (250, 0))


    pygame.display.update()
    clock.tick(60)