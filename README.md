🥊 Game Đối Kháng 2D (Python & Pygame)

Dự án game đối kháng 2 người chơi (Local 2-Player Fighting Game) được phát triển bằng ngôn ngữ Python sử dụng thư viện `pygame`. 

## ✨ Tính năng nổi bật
* **Hệ thống trạng thái (State Machine):** Quản lý mượt mà các trạng thái của nhân vật: Đứng yên (`idle`), Di chuyển (`walk`), Nhảy (`jump`), Tấn công (`attack`), và Bị thương (`hurt`).
* **Vật lý & Trọng lực:** Mô phỏng lực hút trọng trường, nhảy cao và phát hiện chạm sàn chuẩn xác.
* **Va chạm & Hitbox:** Tính toán hitbox tấn công theo hướng mặt nhân vật và trừ máu đối thủ khi trúng đòn.
* **Thanh máu động (Dynamic HP Bar):** Tự động co giãn theo chỉ số máu tối đa (`max_hp`).
* **Màn hình chiến thắng & Reset:** Tự động hiển thị người chiến thắng khi hết máu và hỗ trợ phím `R` để chơi lại trận đấu ngay lập tức.

## 📁 Cấu trúc thư mục dự án
```text
fighting-game/
│
├── main.py              # Vòng lặp game chính (Game loop), UI, thanh máu, sự kiện
├── .gitignore           # Cấu hình loại bỏ file rác (pycache, venv)
├── README.md            # Tài liệu giới thiệu dự án
├── src/                 # Thư mục chứa mã nguồn các class nhân vật
│   ├── fighter1.py      # Lớp xử lý logic cho Player 1
│   └── fighter2.py      # Lớp xử lý logic cho Player 2
└── assets/              # Thư mục chứa tài nguyên đồ họa (Sprite sheets)
    ├── p1/              # Animation của Player 1 (idle, walk, attack, hurt, jump)
    └── p2/              # Animation của Player 2 (idle, walk, attack, hurt, jump)

🎮 Phím điều khiển
Player 1 (Bên trái):
Di chuyển: Phím A (Trái) / D (Phải)

Nhảy: Phím W

Tấn công: Phím J

Phòng thủ: Phím K

Cast Skill: Phím C

Player 2 (Bên phải):
Di chuyển: Phím Mũi tên Trái / Phải (← / →)

Nhảy: Phím Mũi tên Lên (↑)

Tấn công: Phím số 1

Phòng thủ: Phím số 2

Cast Skill: Phím số 3

🚀 Hướng dẫn cài đặt và chạy game
1. Yêu cầu hệ thống
Đã cài đặt Python trên máy tính.

2. Cài đặt thư viện Pygame
Mở Terminal / PowerShell tại thư mục dự án và chạy lệnh:
pip install pygame

3. Khởi chạy game
Chạy file điều khiển chính:
python main.py

4. Chơi lại (Restart)
Khi màn hình hiển thị người chiến thắng, nhấn phím R để reset trận đấu.