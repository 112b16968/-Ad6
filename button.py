import pygame
import random
import time

pygame.init()

size = [400, 350]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = size[0] // 2
y = size[1] // 2 + 25

ballX = random.randrange(0, size[0])
ballY = random.randrange(50, size[1] - 50)

goalX = size[0] // 2 - 10
goalY = size[1] // 2 - 10
goalW = 20
goalH = 20

points = 0

red = pygame.color.Color('#FF8080')
blue = pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')

total_time = 30
start_time = time.time()

def checkOffScreenX(x):
    if x > size[0]:
        x = 0
    elif x < 0:
        x = size[0]
    return x

def checkOffScreenY(y):
    if y > size[1]:
        y = 50
    elif y < 50:
        y = size[1]
    return y

def checkTouching():
    global x, ballX, y, ballY

    if -10 < y - ballY < 10 and -10 < x - ballX < 10:
        pygame.draw.circle(screen, white, [x, y], 15)

        xDiff = x - ballX
        yDiff = y - ballY

        if ballX == 0:
            xDiff -= 5
        elif ballX == size[0]:
            xDiff += 5
        if ballY == 50:
            yDiff -= 5
        elif ballY == size[1]:
            yDiff += 5

        x += xDiff * 2
        ballX -= xDiff * 2
        y += yDiff * 2
        ballY -= yDiff * 2

done = False
while not done:
    screen.fill(black)

    pygame.draw.rect(screen, white, (0, 0, size[0], 50))

    pygame.draw.rect(screen, white, (goalX, goalY, goalW, goalH))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1

    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    ballX = checkOffScreenX(ballX)
    ballY = checkOffScreenY(ballY)

    checkTouching()

    for point in range(points):
        pointX = 0 + point * 5
        pygame.draw.rect(screen, white, (pointX, 53, 4, 7))

    pygame.draw.circle(screen, red, [x, y], 6)

    pygame.draw.circle(screen, blue, [ballX, ballY], 6)

    if goalX <= ballX <= goalX + goalH and goalY <= ballY <= goalY + goalH:
        points += 1
        ballX = random.randrange(0, size[0])
        ballY = random.randrange(50, size[1] - 50)

    remaining_time = max(0, total_time - (time.time() - start_time))
    remaining_time_str = "{:.1f}".format(remaining_time)
    font = pygame.font.Font(None, 36)
    text = font.render("Time left: " + remaining_time_str, True, black)
    text_rect = text.get_rect()
    text_rect.topright = (size[0] - 10, 10)
    screen.blit(text, text_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(72)

pygame.quit()

print("Total points: " + str(points))