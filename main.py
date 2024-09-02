import pygame
import json
from config import SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, WHITE, FONTPATH
from session import GameSession
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

# Initialize Pygame
pygame.init()
pygame.font.init()

# Load JSON data
with open(resource_path("data/flags.json"), "r", encoding="utf-8") as file:
    data = json.load(file)

# Load Font
font = pygame.font.Font(resource_path("assets/Microsoft Sans Serif.ttf"), 30)
korean_font = pygame.font.Font(resource_path("assets/Microsoft Sans Serif.ttf"), 92)
mini_font = pygame.font.Font(resource_path("assets/Microsoft Sans Serif.ttf"), 20)

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flag Typer")

# Clock
clock = pygame.time.Clock()

# Main game loop
game_session = GameSession(data, screen, font, korean_font)

running = True

current_time = 0

while running:
    
    screen.blit(game_session.bg_image, (0, 0))
    
    current_time = pygame.time.get_ticks()
    game_session.update_time(current_time)
    
    for event in pygame.event.get():
        game_session.process_game_loop(event, current_time, screen)
        
    if game_session.transitioning:
        game_session.display_region_transition()
        continue

    if game_session.animation_state != "IDLE":
        game_session.update_capture_animation(screen)

    # Miss Pokemon due to running out of time
    if game_session.current_pokemon:
        if game_session.current_pokemon.elapsed_time > game_session.current_pokemon.time_limit:
            if not game_session.transitioning:
                if game_session.animation_state == "IDLE":
                    game_session.pokemon_missed(10)

    # Display messages
    if game_session.game_ended:
        game_session.draw_end_screen(screen, game_session.font)
    elif game_session.game_paused:
        game_session.draw_pause_menu(screen, game_session.font)
    else:
        if game_session.current_pokemon:
            game_session.draw_game_elements(screen, game_session.large_font, game_session.current_pokemon.elapsed_time, game_session.bg_image)
        # Draw the caught Pokémon icons
        game_session.display_messages(screen, game_session.font, BLACK, SCREEN_WIDTH)
        game_session.display_special_message(screen, game_session.font, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    if not game_session.game_ended:
        game_session.draw_game_scores(screen, game_session.font)
        game_session.draw_caught_pokemon_icons(screen)
    
    
    
    pygame.display.flip()
    clock.tick(60)

        # Draw the copyright line
    copyright_text = "Copyright 2024 Joseph Bae, made for my children and cousins with love"
    text_surface = mini_font.render(copyright_text, True, WHITE)
    screen.blit(text_surface, (SCREEN_WIDTH - text_surface.get_width() - 30, SCREEN_HEIGHT - 30))


pygame.quit()
            
    