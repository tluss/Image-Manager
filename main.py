import pygame as pg
import time
import random
  
pg.init() 
  
screen = pg.display.set_mode((400, 400)) 
  
pg.display.set_caption("❤️&💀") 
exit = False
RANAREA = 200
ZOOM = 10
POS = (0,0)
FPS = 20

def draw_cells(cl):
    lx, ly = pg.display.get_window_size()
    for pos in cl:
        x, y = pos.split(" ")
        x, y = int(x), int(y)
        pg.draw.rect(screen,(200,200,200),((x+POS[0])*ZOOM-1+lx//2,(y+POS[1])*ZOOM-1+ly//2,ZOOM+2,ZOOM+2))
        
def update_cells(cl):
    adj_list = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    new_cell_list = {}
    for pos in cl:
        new_cell_list[pos] = (True,0)
        
    for pos in cl:
        x, y = pos.split(" ")
        x, y = int(x), int(y)
        for adj in adj_list:
            key = str(x+adj[0]) + " " +str(y+adj[1])
            if key in new_cell_list:
                new_cell_list[key] = (new_cell_list[key][0],new_cell_list[key][1]+1)
            else:
                new_cell_list[key] = (False,1)
    cl = []
    for pos,val in new_cell_list.items():
        v, nei = val
        if v == True:
            if nei==2 or nei==3:
                cl.append(pos)
        else :
            if nei==3:
                cl.append(pos)
    return cl

def matrix_to_list(mat):
    cl = []
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == "1":
                cl.append(str(x) + " " +str(y))
    return cl
                
cell_list = matrix_to_list([
    "000000000000000000000000100000000000",
    "000000000000000000000010100000000000",
    "000000000000110000001100000000000011",
    "000000000001000100001100000000000011",
    "110000000010000010001100000000000000",
    "110000000010001011000010100000000000",
    "000000000010000010000000100000000000",
    "000000000001000100000000000000000000",
    "000000000000110000000000000000000000"
])

"""cell_list = matrix_to_list([
    "01111",
    "10001",
    "00001",
    "10010"
])"""
"""
cell_list = matrix_to_list([[str(random.randint(0, 1)) for x in range(RANAREA)]for y in range(RANAREA)])
"""
screen.fill((0,0,0)) 
draw_cells(cell_list)
pg.display.update()

mouse_p = False
mouse_spos = (0,0)
while not exit: 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            exit = True
        if event.type == pg.MOUSEWHEEL:
            if event.y == 1:
                lx, ly = pg.display.get_window_size()
                ZOOM = ZOOM*1.1

            elif event.y == -1:
                ZOOM = ZOOM*0.91

            
    if pg.mouse.get_pressed()[0]:
        if not(mouse_p):
            mouse_p = True
            mouse_pos = pg.mouse.get_pos()
        else: 
            new_mouse_pos = pg.mouse.get_pos()
            POS = (POS[0]+(new_mouse_pos[0]-mouse_pos[0])/ZOOM, POS[1]+(new_mouse_pos[1]-mouse_pos[1])/ZOOM)
            mouse_pos = new_mouse_pos
    else:
        mouse_p = False
        
    
    time.sleep(1/FPS)
    cell_list = update_cells(cell_list)
    screen.fill((0,0,0)) 
    draw_cells(cell_list)
    pg.display.update()
    
