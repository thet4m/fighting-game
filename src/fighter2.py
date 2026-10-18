from .fighter import Fighter

class Fighter2(Fighter):
    def __init__(self, x, y, controls, sprite_folder):
        animations_config = {
            'idle': ('idle.png', 7, 100, 100, 1.5),
            'walk': ('walk.png', 6, 100, 100, 1.5),
            'attack': ('attack.png', 8, 100, 100, 1.5),
            'hurt': ('hurt.png', 4, 100, 100, 1.5),
            'jump': ('jump.png', 10, 100, 100, 1.5),
            'defend': ('idle.png', 1, 100, 100, 1.5),
        }
        super().__init__(x, y, controls, sprite_folder, animations_config, initial_direction=-1)