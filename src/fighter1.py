from .fighter import Fighter

class Fighter1(Fighter):
    def __init__(self, x, y, controls, sprite_folder):
        animations_config = {
            'idle': ('idle.png', 15, 100, 100, 1.5),
            'walk': ('walk.png', 6, 100, 100, 1.5),
            'attack': ('attack.png', 5, 110, 100, 1.5),
            'hurt': ('hurt.png', 8, 100, 100, 1.5),
            'jump': ('jump.png', 8, 100, 100, 1.5),
            'defend': ('idle.png', 1, 100, 100, 1.5), # Tạm dùng idle nếu chưa có asset defend riêng
        }
        super().__init__(x, y, controls, sprite_folder, animations_config, initial_direction=1)