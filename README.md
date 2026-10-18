# 🥊 2D Fighting Game (Python & Pygame)

A local 2-player fighting game project developed in Python using the `pygame` library.

## ✨ Key Features
- **State Machine:** Smoothly manages character states: `idle`, `walk`, `jump`, `attack`, and `hurt`.
- **Physics & Gravity:** Simulates gravitational pull, jump height, and precise floor collision detection.
- **Collisions & Hitboxes:** Calculates attack hitboxes relative to the character's facing direction and deducts health upon hit.
- **Dynamic HP Bar:** Automatically scales according to the maximum health (`max_hp`) index.
- **Victory Screen & Reset:** Automatically displays the winner when health depletes and supports pressing `R` to restart the match instantly.

## 📁 Project Directory Structure
```text
fighting-game/
│
├── main.py              # Main game loop, UI, health bars, event handling
├── .gitignore           # Configuration to ignore junk files (pycache, venv)
├── README.md            # Project documentation
├── src/                 # Source code directory for character classes
│   ├── fighter.py       # Base Fighter class handling core logic and OOP inheritance
│   ├── fighter1.py      # Specific configuration for Player 1
│   └── fighter2.py      # Specific configuration for Player 2
└── assets/              # Graphic asset directory (Sprite sheets)
    ├── p1/              # Player 1 animations (idle, walk, attack, hurt, jump)
    └── p2/              # Player 2 animations (idle, walk, attack, hurt, jump)
```

## 🎮 Controls
* **Player 1 (Left side):**

Movement: A (Left) / D (Right) keys

Jump: W key

Attack: J key

Defend: K key

Cast Skill: C key

* **Player 2 (Right side):**

Movement: Left / Right Arrow keys (← / →)

Jump: Up Arrow key (↑)

Attack: Number 1 key

Defend: Number 2 key

Cast Skill: Number 3 key

## 🚀 Installation and Execution Guide
* **Prerequisites**
Python installed on your computer.

* **Installation**
Open Terminal / PowerShell in the project directory and run:
```bash
pip install pygame
```

* **Execution**
Run the main control file:
```bash
python main.py
```

* **Restart**
When the victory screen appears, press the R key to restart the match immediately.