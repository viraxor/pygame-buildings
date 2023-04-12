import pygame
import random

pygame.init()

# window init
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Buildings")

running = True

# colors
midnight_blue = pygame.Color((25, 25, 112))
black = pygame.Color((0, 0, 0))

# 60fps demo!
clock = pygame.time.Clock()

buildings = [None, None, None, None, None]

class Building(pygame.sprite.Sprite):
    def __init__(self, x1, y1, width, color):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.color = color
        
    def draw(self):
        pygame.draw.rect(window, self.color, (self.x1, self.y1, self.width, 600))

def draw_building(x1, y1, width=150):
    gray_shade = random.randint(0, 45)
    return Building(x1, y1, width, pygame.Color((gray_shade, gray_shade, gray_shade)))

while running:
    pygame.display.flip()
    
    # sky
    window.fill(midnight_blue)
    
    # drawing buildings
    if buildings == [None, None, None, None, None]:
        buildings[0] = draw_building(0, random.randint(50, 300), 150)
        buildings[1] = draw_building(150, random.randint(50, 300), 150)
        buildings[2] = draw_building(300, random.randint(50, 300), 150)
        buildings[3] = draw_building(450, random.randint(50, 300), 150)
    elif buildings[4] == None:
        buildings[0].width -= 1
        buildings[1].x1 -= 1
        buildings[2].x1 -= 1
        buildings[3].x1 -= 1
        buildings[4] = draw_building(599, random.randint(50, 300), 1)
    elif buildings[0].width == 0:
        buildings[0] = buildings[1]
        buildings[1] = buildings[2]
        buildings[2] = buildings[3]
        buildings[3] = buildings[4]
        buildings[0].width -= 1
        buildings[1].x1 -= 1
        buildings[2].x1 -= 1
        buildings[3].x1 -= 1
        buildings[4] = draw_building(599, random.randint(50, 300), 1)
    else:
        buildings[0].width -= 1
        buildings[1].x1 -= 1
        buildings[2].x1 -= 1
        buildings[3].x1 -= 1
        buildings[4].x1 -= 1
        buildings[4].width += 1
    
    for building in buildings:
        if building != None:
            building.draw()
            
    # black ground
    ground = pygame.draw.rect(window, black, (0, 575, 600, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            
    clock.tick(60)
