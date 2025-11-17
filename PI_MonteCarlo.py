import sys
import random, math
import pygame

pygame.init()

###################################################################

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monte Carlo Pi Estimation")

###################################################################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FONT = pygame.font.SysFont("comicsans", 64)
# FPS = 120

###################################################################
# Parameters

Outter_x, Outter_y, Outter_w, Outter_h = 100, 100, WIDTH-200, HEIGHT-200

RADIUS = min(Outter_w, Outter_h) // 2
CENTER = (WIDTH//2, HEIGHT//2)
PWC = 0
TOTAL_POINTS = []
TP = 0


###################################################################
# Main Loop
run = True
CLOCK = pygame.time.Clock()

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
    
    # Generating a random point
    x = random.randint(Outter_x, Outter_w+100)
    y = random.randint(Outter_y, Outter_h+100)
    
    # Checking if the point is within the circle
    distance = math.sqrt((x - CENTER[0])**2 + (y - CENTER[1])**2)
    if distance <= RADIUS:
        PWC += 1
        
    TOTAL_POINTS.append((x, y))
    TP += 1
    
    # Drawing the points
    WIN.fill(BLACK)
    for point in TOTAL_POINTS:
        pygame.draw.circle(WIN, WHITE, point, 2)
    pygame.draw.circle(WIN, RED, CENTER, RADIUS, width=6)
    pygame.draw.rect(WIN, WHITE, (Outter_x, Outter_y, Outter_w, Outter_h), width=6)
    
    # Displaying the current estime of Pi
    Pi_Estimate = 4 * (PWC / TP)
    Text = FONT.render(f"Pi Estimate: {Pi_Estimate:.6f}", True, WHITE)
    WIN.blit(Text, (10, 10))
    
    pygame.display.update()
    # CLOCK.tick(FPS)
