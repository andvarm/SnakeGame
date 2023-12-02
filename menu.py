"""Main menu"""
print("Starting imports")
import SnakeGame
print("imported SnakeGame")
import pygame
import pygame_menu
print("imported pygame and pygame_menu")

volume = 1
user_name = 'Artyom'

def set_volume(index, value):
    """Saves volume in a variable"""
    global volume
    volume = value
    
    print(f"volume set to: {volume}")

def save_user_name(value):
    """Saves username in variable"""
    global user_name
    user_name = value
    print(user_name)

def start_the_game():
    """Starts the game"""
    print("Game starts with volume: ", volume)
    SnakeGame.gameLoop(user_name, volume)

def menu():
    """Menu"""
    """Initiates pygame"""
    pygame.init()
    
    surface = pygame.display.set_mode((600, 400))

    menu = pygame_menu.Menu('Imperium Aureum', 600, 400,
    theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Username: ', default='Artyom', onchange=save_user_name)
    menu.add.selector('Volume: ', [('1', 1), ('0.9', 0.9), ('0.8', 0.8), ('0.7', 0.7), ('0.6', 0.6), \
                                        ('0.5', 0.5), ('0.4', 0.4), ('0.2', 0.2), ('0.1', 0.1)], onchange=\
                                        set_volume)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)

if __name__ == "__main__":
    menu()
