import pygame
import random
import unicodedata
from config import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, BLACK
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

class Country:
    def __init__(self, data, font):
        self.alpha = f"{data['alpha2']}"
        self.raw_name = data["en"].upper().split(',')[0]
        self.name = self.get_name()
        self.font = font
        self.is_caught = False
        self.caught_time = None
        self.ball_hit = False
        self.is_fast = False
        self.is_super_fast = False
        self.time_limit = self.get_time_limit()
        self.walk_offset = [0,0]
        self.start_time = pygame.time.get_ticks()
        self.current_position = [0,0]
        self.elapsed_time = 0
        self.total_paused_time = 0
        self.bg = self.load_bg_image()
        self.sprite = self.get_flag(128)
        self.icon = self.get_flag(25)
        

    def get_name(self):

        return ''.join(c for c in unicodedata.normalize('NFD', self.raw_name) if unicodedata.category(c) != 'Mn')

    def get_time_limit(self):
        return 10*1000
    
    def walk(self):
        self.walk_offset[0] += random.randint(-5, 5)
        self.walk_offset[1] += random.randint(-5, 10)
        
    def copy(self):
        # Create a new Pokemon instance without initializing it
        new_copy = Country.__new__(Country)

        # Copy the attributes from the current instance to the new one
        new_copy.__dict__ = self.__dict__.copy()

        return new_copy
    
    def get_flag(self, target_height, outline_color = WHITE, outline_thickness = 2 ):
        
        which_folder = 128 if target_height > 32 else 32

        flags = f"flags{which_folder}"

        original_image = pygame.image.load(resource_path(os.path.join(f'assets/{flags}', f"{self.alpha}.png")))

        return pygame.transform.smoothscale(original_image, (target_height, target_height))

    
    def load_bg_image(self, target_size=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2), gray_alpha=0.9):
        new_width, new_height = target_size
        
        original_image = self.get_flag(128)
        scaled_image = pygame.transform.smoothscale(original_image, (new_height, new_height))
        gray_surface = pygame.Surface(scaled_image.get_size(), pygame.SRCALPHA)
        gray_surface.fill((128, 128, 128, int(255 * gray_alpha)))
        final_image = scaled_image.copy()
        final_image.blit(gray_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        #japanese_surface = self.font.render(self.huneum, True, BLACK)  # Stylize the text as needed (e.g., color)
        #korean_surface = self.font.render(f"Stroke: {self.strokes}", True, BLACK)  # Stylize the text as needed (e.g., color)
        #id_surface = self.font.render(f"Grade: {self.grade}", True, BLACK)
        
        # Position the text at the bottom-right corner, justified to the right edge
        #japanese_rect = japanese_surface.get_rect(bottomright=(new_width - 10, new_height - 10))  # 10-pixel padding from edges
        #final_image.blit(japanese_surface, japanese_rect.topleft)
        #korean_rect = korean_surface.get_rect(bottomright=(new_width - 10, japanese_rect.top - 10))  # 10-pixel padding from edges
        #final_image.blit(korean_surface, korean_rect.topleft)
        #id_rect = id_surface.get_rect(bottomright=(new_width - 10, korean_rect.top - 10))
        #final_image.blit(id_surface, id_rect.topleft)
        
        return final_image
