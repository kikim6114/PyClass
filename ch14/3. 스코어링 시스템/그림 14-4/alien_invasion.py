# "14.3 스코어링 시스템"
# 그림 14-4

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """게임 에셋과 동작을 관리하기 위한 전체 클래스."""

    def __init__(self):
        """게임 초기화 후 게임 리소스 생성."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 게임 통계를 저장하기 위한 인스턴스 생성,
        #   그리고 스코어보드 생성.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Alien Invasion을 비활성 상태에서 시작.
        self.game_active = False

        # Play button 만들기.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """게임을 위한 메인 루프 시작."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """키누름과 마우스 이벤트에 대한 응답."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """플레이어가 Play를 클릭하면 새 게임 시작."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # 게임 설정 리셋.
            self.settings.initialize_dynamic_settings()

            # 게임 통계 리셋.
            self.stats.reset_stats()
            self.sb.prep_score()
            
            self.game_active = True

            # 남아있는 총알 및 외계인 제거.
            self.bullets.empty()
            self.aliens.empty()

            # 새 함대 생성하고 우주선을 중앙에 배치.
            self._create_fleet()
            self.ship.center_ship()

            # 마우스 커서 숨기기.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """키누름에 대한 반응."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """키업에 대한 반응."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """새 총알을 생성하여 bullets group에 추가."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """총알 위치 업데이트하고 사라진 총알들을 제거."""
        # 총알 위치 업데이트.
        self.bullets.update()

        # 사라진 총알들을 제거.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """총알-외계인 충돌에 대한 반응."""
        # 충동한 총알과 외계인 제거.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # 기존 총알 파괴하고 새 함대 생성.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # 감소시켜 우주선을 좌로, 그리고 스코어보드 업데이트.
            self.stats.ships_left -= 1

            # 남아있는 총알과 외계인 제거.
            self.bullets.empty()
            self.aliens.empty()

            # 새 함대 생성하고 우주선을 중앙에 배치.
            self._create_fleet()
            self.ship.center_ship()

            # 일시 멈춤.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """함대에 있는 모든 외계인 위치 업데이트트"""
        """함대가 엣지에 있는지 확인하고 그렇다면 위치 업데이트."""
        self._check_fleet_edges()
        self.aliens.update()

        # 외계인-우주선 충돌이 있는지 확인.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 스크린 바닥과 충돌한 외계인이 있는지 확인.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """스크린 바닥까지 도달한 외계인이 있는지 확인."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 우주선이 충돌한 것과 같게 취급.
                self._ship_hit()
                break

    def _create_fleet(self):
        """외계인 함대 생성."""
        # 외계인을 생성하여 빈곳이 없을 때까지 계속 추가.
        # 외계인들 사이의 간격은 한 외계인 너비와 한 외계인 높이.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 한 줄 완료; x 값 리셋하고 y 값 증가시킴.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """외계인 생성하고 함대에 배치."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """엣지에 도달한 외계인이 있는지 확인하고 있으면 적절하게 처리."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """전체 함대를 아래로 내리고 이동 방향을 전환."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """스크린 상의 이미지 업데이트하고 새 스크린에 표시."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        # 점수 정보를 화면에 표시.
        self.sb.show_score()

        # 게임이 비활성 상태이면 Play 버튼을 표시.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # 게임 이스턴스를 만들고 게임을 실행시킨다.
    ai = AlienInvasion()
    ai.run_game()