import pygame
import time
import random
import json

# Starta pygame
pygame.init()

# Definiera färger som används i spelet
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Sätt storleken på fönstret 
dis_width = 600
dis_height = 400

# Skapa fönstret 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game v4.2.0 by Andreas Värmfors')

# Skapa en klocka för att hålla koll på spelets hastighet 
clock = pygame.time.Clock()

# sätt storleken på masken och även hastigheten på masken 
snake_block = 10
snake_speed = 11

# Skapa font-stil för poäng och meddelanden 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 25)

def read_from_file(filename, key):
    with open(filename, "r") as f:
        json_dict = json.load(f)

    return json_dict[key]

def write_to_file(filename, dict):
    with open(filename, "w") as f:
        f.write(dict)

def highscore(highscore):
    if read_from_file("highscore.json", "highscore") > highscore:
        return None


    else:
        highscore_dict = {
            "highscore" : highscore
        }

        json_dict = json.dumps(highscore_dict, indent=4)

        write_to_file("highscore.json", json_dict)
 
# Funktion för att visa poängen 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [0, 0])
 
 
# Funktion för att få pygame att rita masken 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 

# Funktion för att kunna visa meddelanden 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
# Loopen som i princip innehåller själva spelet. 
def gameLoop():
    game_over = False # En variabel som kontrollerar om spelet är över
    game_close = False # En variabel som kontrollerar om spelet är förlorat
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        # Kolla så att spelet inte är förlorat.
        while game_close == True:
            highscore(Length_of_snake - 1)
            dis.fill(red)
            message("You Lost! Press C-Play Again or Q-Quit", black)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            # När man dör ska man kunna välja att starta om eller avsluta spelet genom att trycka på k eller c
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("goodbye")
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # Sätta kontrollerna för spelet så att man kan kontrollera masken
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    print("Left")
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    print("Right")
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    print("Up")
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    print("Down")

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #om man åker utanför spelplanen dör man.
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block]) #Rita maten
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1) #Poängen på spelet är  längden på masken - huvudet.
 
        pygame.display.update() #uppdatera skärmen.
 
        if x1 == foodx and y1 == foody: #vad som händer om man äter maten.
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed) #uppdateringshastigheten.
 
    pygame.quit()
    quit()
 
 
gameLoop()
#Går det att programmera spel som en nybörjare inom programmering?