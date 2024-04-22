#variable inside a function cant be accessed outside of it. it becomes local scope
#global var u can access outside. better to use return statements or class
#read more on timer in pygame
#sprites combines a surface w a rect
import pygame
import random
from sys import exit

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <0: 
        player_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x>0: #ball movinf R
        if abs(ball.right - player.left) < 10: #check what side collision occured and if ball hit the left of paddle
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


    if ball.colliderect(opponent) and ball_speed_x<0: #ball moving left
        if abs(ball.left - opponent.right) < 10: #so ball wont hit the top or bottom of paddle
            ball_speed_x *= -1
        #so ball bounces off from top/bottom of paddles
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        

def player_animation(): 
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top <ball.y: #if opponent is above the ball, move opponent down
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed #opponent moves up
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time
    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks() #what time u r on rn
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_number = game_font.render("3", False, light_grey)
        screen.blit(number_number, (screen_width/2 - 10, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_number = game_font.render("3", False, light_grey)
        screen.blit(number_number, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100: #when this is <2.1s, ball is placed back in centre
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None

pygame.init()
clock = pygame.time.Clock()
'clock helps to control frame rate'

screen_width = 1200
screen_height = 610
screen = pygame.display.set_mode((screen_width, screen_height)) #display surface
pygame.display.set_caption('pong') 
'to change title'



'all obj represented as rect'
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30) #(x, y, width, height) u r placing ball in centre
player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 100)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 100)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
ball_moving = False
score_time = True

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

#timer
score_time = None

while True:
    'loop will run forever cuz its alwys true'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
            'this exit() stops calling the while true loop'
        if event.type == pygame.KEYDOWN: #checks if ANY of the keys on keyboard is pressed
            if event.key == pygame.K_DOWN: #checks if down key is pressed
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_DOWN: 
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


    ball_animation()
    player.y += player_speed
    #prevents player from leaving screen
    player_animation()
    opponent_animation()
    


    'visuals to display/draw on screen'
    screen.fill(bg_color) #called first so its layer will be the lowest (so behind all the obj)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball) #ellipse becomes circle cuz of specified dimensions
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

    if score_time: 
        ball_restart() #if ball hits L/R screens restart ball to middle


    player_text = game_font.render(f"{player_score}",False,light_grey)
    screen.blit(player_text, (624, 305)) #puts one surface on the other
    
    opponent_text = game_font.render(f"{opponent_score}",False,light_grey)
    screen.blit(opponent_text, (560, 305)) #puts one surface on the other


    pygame.display.flip() #take evrything in loop to draw on screen
    clock.tick(60)

    



