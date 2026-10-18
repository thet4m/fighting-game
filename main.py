import pygame
from fighter1 import Fighter1
from fighter2 import Fighter2

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Đối Kháng 2D")
clock = pygame.time.Clock()

# 1. Khai báo phím điều khiển
# P1: Dùng A, D để đi chuyển, W để nhảy, J để đánh, K để phòng thủ, C để cast
p1_controls = {
    'left': pygame.K_a, 
    'right': pygame.K_d, 
    'up': pygame.K_w, 
    'attack': pygame.K_j, 
    'defend': pygame.K_k, 
    'cast': pygame.K_c
}

# P2: Dùng Mũi tên trái/phải để di chuyển, Mũi tên lên để nhảy, Phím số 1, 2, 3 phía trên chữ để tấn công/phòng thủ/cast
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

def draw_hp_bar(screen, x, y, hp, color):
    # Viền ngoài
    pygame.draw.rect(screen, (255, 255, 255), (x - 2, y - 2, 204, 24), 2)
    # Nền đỏ
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 200, 20))
    # Máu hiện tại
    if hp > 0:
        pygame.draw.rect(screen, color, (x, y, hp * 2, 20))

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật riêng từng nhân vật, truyền đối thủ vào làm target
    player1.update(player2)
    player2.update(player1)

    screen.fill((30, 30, 30))
    
    # Vẽ sàn đấu
    pygame.draw.line(screen, (250, 250, 250), (0, 500), (800, 500), 2)
    
    all_sprites.draw(screen)

    # Vẽ thanh máu P1 & P2
    draw_hp_bar(screen, 50, 30, player1.hp, (0, 120, 255))
    draw_hp_bar(screen, 550, 30, player2.hp, (0, 220, 100))

    pygame.display.flip()

pygame.quit()