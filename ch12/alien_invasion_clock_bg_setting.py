import sys
import pygame
from settings import Settings  # 추가됨

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()  # 추가됨
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # 수정됨
        pygame.display.set_caption("Alien Invasion")
        
        # Set the background color.
        # self.bg_color = (230, 230, 230)  # 삭제하고 Settings 클래스를 도입함

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)  # Settings 클래스 사용하도록 수정됨
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()