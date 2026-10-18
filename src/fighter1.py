import pygame

class Fighter1(pygame.sprite.Sprite):
    def __init__(self, x, y, controls, sprite_folder):
        super().__init__()
        self.controls = controls
        
        self.animations = {
            'idle': self.load_frames(f'{sprite_folder}/idle.png', 15, 100, 100, 1.5),
            'walk': self.load_frames(f'{sprite_folder}/walk.png', 6, 100, 100, 1.5),
            'attack': self.load_frames(f'{sprite_folder}/attack.png', 5, 110, 100, 1.5),
            'hurt': self.load_frames(f'{sprite_folder}/hurt.png', 8, 100, 100, 1.5),
            'jump': self.load_frames(f'{sprite_folder}/jump.png', 8, 100, 100, 1.5),
        }
        
        self.state = 'idle'
        self.frame_index = 0
        self.animation_speed = 0.15
        
        self.image = self.animations[self.state][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

        # Chỉ số & Vật lý
        self.hp = 100
        self.max_hp = 100 # Thêm max_hp để đồng bộ với main.py
        self.floor_y = 500
        self.vel_y = 0 
        self.gravity = 1 
        self.jump_power = -15 

        self.direction = 1  # 1: Phải, -1: Trái
        self.attack_cooldown = 0 

    def load_frames(self, path, num_frames, width, height, scale):
        sheet = pygame.image.load(path).convert_alpha()
        frames = []
        for i in range(num_frames):
            frame = pygame.Surface((width, height), pygame.SRCALPHA)
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
        
        # 1. Xử lý di chuyển ngang
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

        # 4. Nếu đang ở trên không, ưu tiên hiển thị nhảy
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
        
        # Xử lý khi chạy hết số frame của animation hiện tại
        if self.frame_index >= len(self.animations[self.state]):
            if self.state in ['attack', 'cast', 'hurt']:
                self.state = 'idle'
                self.frame_index = 0
            elif self.state == 'jump':
                # Giừng ở frame cuối khi đang ở trên không
                self.frame_index = len(self.animations[self.state]) - 1
            else:
                self.frame_index = 0

        # Nếu đã chạm đất mà state vẫn là jump thì phải trả về idle
        if self.rect.bottom >= self.floor_y and self.state == 'jump':
            self.state = 'idle'
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

    def reset(self, x, y):
        self.hp = self.max_hp
        self.rect.topleft = (x, y)
        self.state = 'idle'
        self.frame_index = 0
        self.vel_y = 0
        self.attack_cooldown = 0    