import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightbrown = (181, 101, 29)
brown = (128, 43, 0)
darkbrown = (51, 18, 0)

gameDisplay = pygame.display.set_mode((1200, 600))
gameDisplay.fill(brown)


def whiteorblack(color):
    if color == white:
        color = black
    else:
        color = white

    return color


def printrow(top=True):
    """prints a row depending on its position (top by default) and its starting color (white default)"""
    if top:
        color = white
        for i in range(12):
            pygame.draw.polygon(gameDisplay, color,
                                ((i * 100, 0), (i * 100 + 100, 0), (i * 100 + 50, 600 / 2.5)))
            color = whiteorblack(color)
    else:
        color = black
        for i in range(12):
            pygame.draw.polygon(gameDisplay, color,
                                ((i * 100, 600), (i * 100 + 100, 600), (i * 100 + 50, 600 / 2.5 + 125)))
            color = whiteorblack(color)


printrow()
printrow(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
