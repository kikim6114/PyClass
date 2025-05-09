import sys
import pygame
from settings import Settings 
from ship import Ship          

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)  
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  # 추가됨 : 리팩토링 차원

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
            
    def _check_events(self):                            # 리팩토링하여 추가 
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()