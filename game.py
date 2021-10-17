import pygame


class Game:
    def __init__(self):

        # création de la fenêtre
        sc_width = 800
        sc_length = 1400
        sc_size = sc_length, sc_width
        self.screen = pygame.display.set_mode(sc_size)
        pygame.display.set_caption("Tawla Game")

        # chargement du board
        self.background = pygame.image.load('images/board.png')
        self.background = pygame.transform.scale(self.background, sc_size)
        self.background.convert()
        self.rect = self.background.get_rect()

    def run(self):
        # boucle de maintien en vie
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.background, self.rect)
            pygame.display.flip()

        pygame.quit()
