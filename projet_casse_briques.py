import pgzrun

WIDTH = 800
HEIGHT = 600
brick = Actor("brick", anchor = ["left","top"])
brick.pos =[0,0]

all_bricks =[]

player= Actor("player")
player.pos = [WIDTH/2,550]

ball = Actor("ball")
ball.pos = [WIDTH/2,500]
ball_speed = [3,-3]


def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1
def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1

def update():
    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]
    ball.pos = [new_x, new_y]
    
    if ball.right > WIDTH or ball.left < 0:
        invert_horizontal_speed()
    if ball.top < 0:
        invert_vertical_speed()
    if ball.colliderect(player):
        invert_vertical_speed()
    
        
    for brick in all_bricks:
        if ball.colliderect (brick):
            all_bricks.remove(brick)
            invert_vertical_speed()

        


    


for y in range (0,7*30,30):
    for x in range (0,800,100):
        brick= Actor("brick", anchor = ["left","top"])
        brick.pos=[x,y]
        all_bricks.append(brick)


        
def on_mouse_move(pos):
    player.pos = [pos [0],player.pos[1]]



def draw():
    screen.clear()
    for brick in all_bricks:
        brick.draw()
    player.draw()
    ball.draw()



    


    





#dernière ligne
pgzrun.go()
