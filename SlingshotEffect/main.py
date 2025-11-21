import sys
import math
import pygame as pg

pg.init()

############################################################

WIDTH, HEIGHT = 1000, 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Gravitational Slingshot Effect")

SPACE = pg.transform.scale(pg.image.load("background.jpg"), (WIDTH, HEIGHT))
EARTH = pg.transform.scale(pg.image.load("earth.png"), (200, 200))
CRASH = pg.mixer.Sound("explosion.wav")

clock = pg.time.Clock()

############################################################

planet_mass, planet_size, ship_mass, ship_size, vel_scale, G = 0, 0, 0, 0, 0, 0
ex, ey = WIDTH//2, HEIGHT//2

def init_vars():
    global planet_mass, planet_size, ship_mass, ship_size
    global vel_scale, G
    
    planet_mass, planet_size, ship_mass, ship_size = 100, 50, 10, 10
    vel_scale, G = 100, 5

class Ship:
    def __init__(self, x, y, x_vel, y_vel, mass):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.mass = mass
    
    def move(self):
        distance = math.sqrt((self.x - ex)**2 + (self.y - ey)**2)
        force = (G * self.mass * planet_mass) / (distance**2)
        
        acceleration = force / self.mass
        angle = math.atan2(ey - self.y, ex - self.x)
        
        x_acceleration = acceleration * math.cos(angle)
        y_acceleration = acceleration * math.sin(angle)
        
        self.x_vel += x_acceleration
        self.y_vel += y_acceleration
        
        self.x += self.x_vel
        self.y += self.y_vel
    
    def draw(self):
        pg.draw.circle(screen, RED, (int(self.x), int(self.y)), ship_size)

############################################################

def main():
    init_vars()
    foo, tempo = [], None
    
    running = True
    while running:
        # Event handling
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    if tempo:
                        tx, ty, mx, my = tempo[0], tempo[1], mouse_pos[0], mouse_pos[1]
                        vx, vy = (mx - tx) / vel_scale, (my - ty) / vel_scale
                        
                        poo = Ship(tx, ty, vx, vy, ship_mass)
                        foo.append(poo)
                        tempo = None
                    else:
                        tempo = mouse_pos
                else:
                    tempo = None
        
        # Drawing     
        screen.blit(SPACE, (0, 0))
        screen.blit(EARTH, ((WIDTH-200)//2, (HEIGHT-200)//2))
         
        if tempo:
            pg.draw.line(screen, WHITE, tempo, mouse_pos, 2)
            pg.draw.circle(screen, RED, tempo, ship_size)
            
        for poo in foo[:]:
            poo.draw()
            poo.move() 
            if poo.x < 0 or poo.x > WIDTH or poo.y < 0 or poo.y > HEIGHT:
                foo.remove(poo)
            if math.sqrt((ex - poo.x)**2 + (ey - poo.y)**2) <= 105:
                CRASH.play()
                pg.draw.circle(screen, WHITE, (poo.x, poo.y), 3*ship_size)
                foo.remove(poo)
        
        pg.display.flip()
        clock.tick(FPS)

############################################################

if __name__ == "__main__":
    main()
