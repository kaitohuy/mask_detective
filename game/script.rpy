
image background_game = Transform("images/intro/background_game.png", size=(1920, 1080))
image map01_idle = Transform("images/intro/background_map01.jpeg", size=(480, 270))
image map01_hover = Transform("images/intro/background_map01.jpeg", size=(480, 270))
image map02_idle = Transform("images/intro/background_map02.png", size=(480, 270))
image map02_hover = Transform("images/intro/background_map02.png", size=(480, 270))

# UI IMAGES (Thay thế bằng file ảnh thật của bạn)
# Frame(path, left, top, right, bottom) giúp ảnh không bị vỡ khi co giãn.
# Nếu ảnh của bạn là size cố định, có thể dùng "images/intro/item_grid_bg.png" trực tiếp.
image ui_grid_bg = Frame("images/ui/ui_text.png", 20, 20) 
image ui_tooltip_bg = Frame("images/ui/ui_text.png", 20, 20)

define e = Character("Eileen")


# The game starts here.

label start:

    # --- INTRO SEQUENCE ---
    scene background_game with fade
    
    # Nhạc nền (Bỏ comment và sửa đường dẫn khi có file nhạc)
    # Dùng placeholder hoặc file nhạc intro nếu có
    play music "audio/true-ending.mp3" fadein 0.5

    # Intro text effect
    show text "{size=60}{b}{color=#f1c40f}MASK DETECTIVE{/color}{/b}{/size}" at Position(yalign=0.2) with dissolve
    pause 4.0 
    hide text with dissolve

    show text "{size=40}{color=#ecf0f1}Nhiều vụ án đầy bí ẩn...{/color}{/size}" with dissolve
    pause 3.0
    hide text with dissolve

    show text "{size=40}{color=#ecf0f1}Bạn đã sẵn sàng để khám phá sự thật?{/color}{/size}" with dissolve
    pause 3.0
    hide text with dissolve

    # --- MAP SELECTION ---
    # Gọi màn hình chọn map thay vì menu cũ
    call screen map_selection
