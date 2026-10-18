import pygame
from src.fighter1 import Fighter1
from src.fighter2 import Fighter2

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Đối Kháng 2D")
clock = pygame.time.Clock()

# Khởi tạo font chữ để hiện thông báo thắng thua
font = pygame.font.SysFont("arial", 50, bold=True)

# 1. Khai báo phím điều khiển
p1_controls = {
    'left': pygame.K_a, 
    'right': pygame.K_d, 
    'up': pygame.K_w, 
    'attack': pygame.K_j, 
    'defend': pygame.K_k, 
    'cast': pygame.K_c
}

p2_controls = {
    'left': pygame.K_LEFT, 
    'right': pygame.K_RIGHT, 
    'up': pygame.K_UP, 
    'attack': pygame.K_1,   
    'defend': pygame.K_2,   
    'cast': pygame.K_3      
}

# 2. Khởi tạo 2 nhân vật
player1 = Fighter1(100, 420, p1_controls, 'assets/p1')
player2 = Fighter2(650, 420, p2_controls, 'assets/p2')

all_sprites = pygame.sprite.Group(player1, player2)

# Hàm vẽ thanh máu động
def draw_hp_bar(screen, x, y, current_hp, max_hp, color):
    bar_width = 200
    bar_height = 20
    current_hp = max(0, current_hp)
    ratio = current_hp / max_hp
    
    # Viền ngoài
    pygame.draw.rect(screen, (255, 255, 255), (x - 2, y - 2, bar_width + 4, bar_height + 4), 2)
    # Nền đỏ
    pygame.draw.rect(screen, (255, 0, 0), (x, y, bar_width, bar_height))
    # Máu hiện tại
    pygame.draw.rect(screen, color, (x, y, bar_width * ratio, bar_height))

winner = None
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Cho phép bấm phím R để chơi lại khi game kết thúc
        elif event.type == pygame.KEYDOWN and winner and event.key == pygame.K_r:
            player1.reset(100, 420)
            player2.reset(650, 420)
            winner = None

    # Nếu chưa có người thắng thì tiếp tục cập nhật game
    if not winner:
        player1.update(player2)
        player2.update(player1)

        # Kiểm tra điều kiện thắng thua
        if player1.hp <= 0:
            winner = "PLAYER 2 WINS!"
        elif player2.hp <= 0:
            winner = "PLAYER 1 WINS!"

    # Vẽ màn hình
    screen.fill((30, 30, 30))
    pygame.draw.line(screen, (250, 250, 250), (0, 500), (SCREEN_WIDTH, 500), 2)
    
    all_sprites.draw(screen)

    # Vẽ thanh máu
    max_hp_p1 = getattr(player1, 'max_hp', 100)
    max_hp_p2 = getattr(player2, 'max_hp', 100)
    
    draw_hp_bar(screen, 50, 30, player1.hp, max_hp_p1, (0, 120, 255))
    draw_hp_bar(screen, 550, 30, player2.hp, max_hp_p2, (0, 220, 100))

    # Nếu có người thắng, hiện thông báo lên màn hình
    if winner:
        text_surf = font.render(winner, True, (255, 255, 0))
        text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text_surf, text_rect)
        
        # Hướng dẫn chơi lại
        restart_font = pygame.font.SysFont("arial", 25)
        restart_surf = restart_font.render("Press 'R' to Restart", True, (255, 255, 255))
        restart_rect = restart_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(restart_surf, restart_rect)

    pygame.display.flip()

pygame.quit()