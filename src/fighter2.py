import pygame

class Fighter2(pygame.sprite.Sprite):
    def __init__(self, x, y, controls, sprite_folder):
        super().__init__()
        self.controls = controls
        
        self.animations = {
            'idle': self.load_frames(f'{sprite_folder}/idle.png', 7, 100, 100, 1.5),
            'walk': self.load_frames(f'{sprite_folder}/walk.png', 6, 100, 100, 1.5),
            'attack': self.load_frames(f'{sprite_folder}/attack.png', 8, 100, 100, 1.5),
            'hurt': self.load_frames(f'{sprite_folder}/hurt.png', 4, 100, 100, 1.5),
            'jump': self.load_frames(f'{sprite_folder}/jump.png', 10, 100, 100, 1.5), # Thêm animation nhảy
        }
        
        self.state = 'idle'
        self.frame_index = 0
        self.animation_speed = 0.15
        
        self.image = self.animations[self.state][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

        # Chỉ số & Vật lý
        self.hp = 100
        self.floor_y = 500
        self.vel_y = 0 
        self.gravity = 1 
        self.jump_power = -15 

        self.direction = -1  # Mặc định quay mặt về bên trái
        self.attack_cooldown = 0 

    def load_frames(self, path, num_frames, width, height, scale):
        sheet = pygame.image.load(path).convert_alpha()
        frames = []
        for i in range(num_frames):
            frame = pygame.Surface((width, height), pygame.SRCALPHA)
            # Ép kiểu int cho tọa độ cắt để tránh sai số hiển thị gây nhấp nháy
            frame.blit(sheet, (0, 0), (int(i * width), 0, int(width), int(height)))
            frame = pygame.transform.scale(frame, (int(width * scale), int(height * scale)))
            frames.append(frame)
        return frames

    def handle_input(self, target):
        # Nếu đang tấn công hoặc bị thương thì không nhận phím
        if self.state in ['attack', 'hurt']:
            return 

        keys = pygame.key.get_pressed()
        new_state = 'idle'
        
        # 1. Xử lý di chuyển ngang (Cho phép vừa di chuyển vừa đổi hướng kể cả khi đang nhảy)
        if keys[self.controls['left']]:
            new_state = 'walk'
            self.rect.x -= self.speed
            self.direction = -1
        elif keys[self.controls['right']]:
            new_state = 'walk'
            self.rect.x += self.speed
            self.direction = 1

        # 2. Xử lý tấn công
        if keys[self.controls['attack']] and self.attack_cooldown == 0:
            new_state = 'attack'
            self.attack(target)
            
        # 3. Xử lý nút nhảy
        if keys[self.controls['up']] and self.rect.bottom >= self.floor_y:
            self.vel_y = self.jump_power
            new_state = 'jump'

        # 4. Nếu đang ở trên không (đang lơ lửng/rơi), ưu tiên hiển thị hình ảnh nhảy
        if self.rect.bottom < self.floor_y:
            new_state = 'jump'
            
        if self.state != new_state:
            self.state = new_state
            self.frame_index = 0

    def attack(self, target):
        if self.attack_cooldown == 0:
            hitbox = pygame.Rect(0, 0, 40, 40)
            hitbox.centery = self.rect.centery
            if self.direction == 1:
                hitbox.left = self.rect.right
            else:
                hitbox.right = self.rect.left

            if hitbox.colliderect(target.rect):
                target.get_hit() 
            
            self.attack_cooldown = 30

    def get_hit(self):
        if self.state != 'defend': 
            self.hp = max(0, self.hp - 10)
            self.state = 'hurt'
            self.frame_index = 0

    def update_animation(self):
        self.frame_index += self.animation_speed
        
        if self.frame_index >= len(self.animations[self.state]):
            if self.state in ['attack', 'cast', 'hurt']:
                self.state = 'idle'
                self.frame_index = 0
            elif self.state == 'jump':
                # Giữ nguyên frame cuối cùng khi đang lơ lửng trên không
                self.frame_index = len(self.animations[self.state]) - 1
            else:
                self.frame_index = 0
            
        current_image = self.animations[self.state][int(self.frame_index)]
        
        if self.direction == -1:
            self.image = pygame.transform.flip(current_image, True, False)
        else:
            self.image = current_image

    def update(self, target):
        self.handle_input(target)        

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
        # Trọng lực và xử lý rơi
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        if self.rect.bottom >= self.floor_y:
            self.rect.bottom = self.floor_y
            self.vel_y = 0

        self.update_animation()