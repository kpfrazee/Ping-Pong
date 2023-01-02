### imports
import random
import sys, pygame
pygame.init()

# gives a randomly generated location to reposition the ball at each start of round
def location():
    y = random.randint(0,780)
    return y

# initial settings - ball, screen
size = width, height = 1200, 800
speed = [1,1]
black = 0, 0, 0
white = 255, 255, 255
x_coord = (width/2)-10
y_coord = location()
x_change = 0.6
y_change = 0.5
screen = pygame.display.set_mode(size)

# allows paddles to move
class mover:
    def __init__(self,x,y,w,h):
        self.x_value = x
        self.y_value = y
        self.width_value = w
        self.height_value = h
    def draw_mover(self):
        mover = (self.x_value,self.y_value), (self.width_value, self.height_value)
        mover_rect = pygame.Rect(mover)
        return mover_rect

# depicts score at top of game screen
class score_counter:
    def __init__(self,score,local):
        self.score_count = score
        self.location = local
    def show_score(self):
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(),100)
        text = font.render(str(self.score_count), True, (100,100,100), black)
        textRect = text.get_rect()
        if self.location == 'left':
            textRect[0] = 600 - ((textRect[2])+10)
        elif self.location == 'right':
            textRect[0] = 600 + 10
        textRect[1] = 5
        return(screen.blit(text,textRect))

# instances of classes from above
left = mover(5,370,10,60)
right = mover(1185,370,10,60)
left_score = score_counter(0,'left')
right_score = score_counter(0,'right')

pygame.key.set_repeat(2,0)

# main code
while True:
    # movers
    lefty = left.draw_mover()
    righty = right.draw_mover()

    # quit key, move keys
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            hit = pygame.key.get_pressed()
            if hit[pygame.K_w]:
                if left.y_value > 0:
                    left.y_value += -1
            elif hit[pygame.K_s]:
                if left.y_value < 740:
                    left.y_value += 1
            if hit[pygame.K_UP]:
                if right.y_value > 0:
                    right.y_value += -1
            elif hit[pygame.K_DOWN]:
                if right.y_value < 740:
                    right.y_value += 1
            if hit[pygame.K_ESCAPE]:
                pygame.quit()

    # ball move - bounce, reset
    ball = (x_coord,y_coord), (20,20)
    ballrect = pygame.Rect(ball)
    x_coord += x_change
    y_coord += y_change
    if 14.75 <= x_coord <= 15.25:
        if (left.y_value - 19) <= y_coord <= (left.y_value + 79):
            x_change = -x_change
            y_change += (random.randint(-10,10)/100)
        else:
            x_change = -0.8
            y_change = -y_change
            x_coord = 590
            y_coord = location()
            left.y_value = 370
            right.y_value = 370
            right_score.score_count += 1
    elif 1164.75 <= x_coord <= 1165.25:
        if (right.y_value - 19) <= y_coord <= (right.y_value +79):
            x_change = -x_change
            y_change += (random.randint(-10,10)/100)
        else:
            x_change = 0.8
            y_change = -y_change
            x_coord = 590
            y_coord = location()
            left.y_value = 370
            right.y_value = 370
            left_score.score_count += 1
    if y_coord < 0 or y_coord > (height-20):
        y_change = -y_change

    # display
    screen.fill(black)
    pygame.draw.line(screen,(100,100,100),(599,0),(599,800),2)
    left_score.show_score()
    right_score.show_score()
    pygame.draw.rect(screen,white,ballrect)
    pygame.draw.rect(screen,(255,0,0),lefty)
    pygame.draw.rect(screen,(0,255,0),righty)
    pygame.display.flip()