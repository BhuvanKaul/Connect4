from local_player import *
from bot_easy import *
from bot_medium import *
from bot_hard import *

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
button_color = (50, 50, 50)

# Fonts
font = pygame.font.Font(None, 36)


# Function to display text on the screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# Function to create buttons
def draw_button(rect, color, text, text_color):
    pygame.draw.rect(screen, color, rect)
    display_text(text, text_color, rect.centerx, rect.centery)


# Main menu loop
def main_menu():
    screen.fill(white)

    # Create buttons
    local_multiplayer_button = pygame.Rect(150, 100, 300, 75)
    draw_button(local_multiplayer_button, button_color, "Local Multiplayer", white)

    bot_button = pygame.Rect(150, 225, 300, 75)
    draw_button(bot_button, button_color, "Bot", white)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if local_multiplayer_button.collidepoint(event.pos):
                    pygame.quit()
                    play_local_player()
                    sys.exit()
                    # Add your code for local multiplayer here
                elif bot_button.collidepoint(event.pos):
                    difficulty_menu()


# Difficulty menu loop
def difficulty_menu():
    screen.fill(white)

    # Create difficulty buttons
    easy_button = pygame.Rect(150, 75, 300, 50)
    draw_button(easy_button, button_color, "Easy", white)

    medium_button = pygame.Rect(150, 175, 300, 50)
    draw_button(medium_button, button_color, "Medium", white)

    hard_button = pygame.Rect(150, 275, 300, 50)
    draw_button(hard_button, button_color, "Hard", white)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    pygame.quit()
                    easy_bot()
                    sys.exit()
                elif medium_button.collidepoint(event.pos):
                    pygame.quit()
                    medium_bot()
                    sys.exit()
                elif hard_button.collidepoint(event.pos):
                    pygame.quit()
                    hard_bot()
                    sys.exit()


main_menu()
