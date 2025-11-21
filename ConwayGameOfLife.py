import sys
import random as rd
import pygame as pg

pg.init()

############################################################

TILE_SIZE = 20
WIDTH = HEIGHT = 800
GRID_SIZE = WIDTH // TILE_SIZE
FPS = 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (60, 60, 60)

screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

############################################################

foo = set()

def init_vars():
    global foo
    foo = set()

def get_neighbors(poo):
    x, y = poo
    n_poo = []
    
    for dx in [-1, 0, 1]:
        if (x + dx < 0) or (x + dx >= GRID_SIZE):
            continue
        
        for dy in [-1, 0, 1]:
            if (y + dy < 0) or (y + dy >= GRID_SIZE) or (dx == dy == 0):
                continue
            
            n_poo.append((x+dx, y+dy))
    
    return n_poo


def handle_foo():
    all_foo = set()
    new_foo = set()
    
    for poo in foo:
        n_poo = get_neighbors(poo)
        all_foo.update(n_poo)
        
        n_poo = list(filter(lambda x: x in foo, n_poo))
        
        if len(n_poo) in [2, 3]:
            new_foo.add(poo)
    
    for poo in all_foo:
        n_poo = get_neighbors(poo)
        n_poo = list(filter(lambda x: x in foo, n_poo))
        
        if len(n_poo) == 3:
            new_foo.add(poo)
    
    return new_foo


def draw():
    global foo
    screen.fill(GREY)
    
    for poo in foo:
        x, y = poo
        pg.draw.rect(screen, WHITE, pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    for g in range(1,GRID_SIZE):
        pg.draw.line(screen, BLACK, (0, g*TILE_SIZE), (WIDTH, g*TILE_SIZE), width=2)
        pg.draw.line(screen, BLACK, (g*TILE_SIZE, 0), (g*TILE_SIZE, HEIGHT), width=2)
    
    pg.display.flip()

############################################################

def main():
    global foo
    init_vars()
    
    running = True
    playing = False
    while running:
        # Event Handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            
            if (not playing) and (event.type == pg.MOUSEBUTTONDOWN):
                if pg.mouse.get_pressed()[0]:
                    poo = pg.mouse.get_pos()
                    foo.add((poo[0]//TILE_SIZE, poo[1]//TILE_SIZE))

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    playing = not playing
                
                if event.key == pg.K_r:
                    init_vars()
                    playing = False
                
                if event.key == pg.K_g:
                    foo = set([(rd.randint(0, GRID_SIZE), rd.randint(0, GRID_SIZE)) for _ in range(rd.randint(3, 7)*GRID_SIZE)])
        
        if playing:
            pg.display.set_caption("Playing    { Space to Pause }    { G to Generate }    { R to Reset }")
            foo = handle_foo()
        else:
            pg.display.set_caption("Paused    { Space to Play }    { G to Generate }    { R to Reset }")
        
        draw()
        clock.tick(FPS)
    
############################################################

if __name__ == "__main__":
    main()
