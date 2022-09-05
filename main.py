import pygame


pygame.init()

blockSize = 50



nx = 5
ny = 5

ax = nx+1
ay = ny+1

x = 100*nx
y = 100*ny

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
win_w = 1000

widht = 100
height = 100

win = pygame.display.set_mode((win_w, 1000))

pygame.display.set_caption("Conway's Game of Life")

alive = [(9,10), (10,10), (11,10), (8,11)]

vizinhos = []


#--------// Functions //------------------------------------------------------------------

def drawGrid():
    for x in range(0, win_w, blockSize):
        for y in range(0, win_w, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(win, BLACK, rect, 1)

#--------// All //------------------------------------------------------------------


all = []

def count(): 
    w = 0
    h = 0 
    cx = 1
    cy = 1
    while h <1000:
        if w < 1000:
            all.append((cx,cy))
            cy += 1
            w += blockSize
        elif h < 1000:
            cx += 1
            w = 0
            h += blockSize
            cy = 0
            cy += 1
        else:
            nopass = ""

    
#--------// Colisions//------------------------------------------------------------------

def draw():

    for i in alive:
            s = str(i).replace('(','').replace(')','').split(', ') 
            [dx, dy] = s
            x = blockSize*(int(dx)-1)
            y = blockSize*(int(dy)-1)  
            pygame.draw.rect(win, (0, 0, 0), (x, y, blockSize, blockSize))

#--------// Rules//------------------------------------------------------------------

#pr_in = []
#pr_out = []

def vis():
    pr_in = []
    pr_out = []
    def compare():
        print("COMPARE() START")
        for i in pr_out:
            print("i= " + str(i))
            print("alive= " + str(alive))
            print("out= " + str(pr_out))
            alive.remove(i)
            pr_out.remove(i)
            #
            print("alive-pos= " + str(alive))
            print("out-pos= " + str(pr_out))
            #return alive
        pr_out.clear()

        for i in pr_in:
            print("i= " + str(i))
            print("alive= " + str(alive))
            print("in= " + str(pr_in))
                
            alive.append(i)
            pr_in.remove(i)
            print("in-pos= " + str(pr_in))
            print("alive-pos-add= " + str(alive))
            #return alive
        pr_in.clear()
        print("COMPARE() END")

    pr_out.clear()
    pr_in.clear()
    for i in all:
        
        abs = str(i).replace('(','').replace(')','').split(', ') 
        [fx, fy] = abs
        fx = int(fx)
        fy = int(fy)
        
        vizinhos = [(fx-1, fy+1), (fx, fy+1), (fx+1, fy+1), (fx-1, fy), (fx+1, fy), (fx-1, fy-1), (fx, fy-1), (fx+1, fy-1) ]

        s = sum(vs in alive for vs in vizinhos)
        if s != 0:
            print(i, s)
            


        
        if i not in alive:
            if s == 3:
                print(str(i) + " born")
                pr_in.append(i)
                compare()
                #return pr_in
        else:
            if s >= 4:
                print(str(i) + " dies")
                pr_out.append(i)
                compare()
                #return pr_out
            elif s < 2:
                print(str(i) + " dies")
                pr_out.append(i)
                compare()
                #return pr_out




            

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>> erroooooo <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#--------------------------------------------------------------------------

count()
rodada = 1

run = True


while run:
    pygame.time.delay(1000)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()


    print(rodada)
    rodada += 1

    win.fill((255, 255, 255))
    drawGrid()
    
    
    s = [ax, ay]
    ax = int(ax)
    ay = int(ay)
    #alive.append((ax-1, ay-1))
    
    print(alive)
    draw()
    vis()
    #compare()
    
    

    #print(alive)
    draw()
    pygame.display.update()


pygame.quit() 

#--------------------------------------------------------------------------





    






































