# "14.3 스코어링 시스템"
# 그림 14-5

import pygame.font

class Button:
    """게임의 버튼 생성을 위한 클래스."""

    def __init__(self, ai_game, msg):
        """버튼 속성 초기화."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 버튼의 크기 및 속성 설정.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)  # 진한 녹색
        self.text_color = (255, 255, 255)  # 흰색색
        self.font = pygame.font.SysFont(None, 48)  # 기본 폰트, 크기 48

        # 버튼의 rect 객체 생성하고 스크린 중앙에 배치.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 버튼의 메시지는 한 번만 준비하면 된다.
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """메시지를 렌더링된 이미지로 바꾸고 텍스트를 버튼 가운데에 배치."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
  
    def draw_button(self):
        """빈 버튼을 그린 다음 메시지를 그린다."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)