
# --------------------------------------------------------------------------------
# DEFINITIONS (ĐỊNH NGHĨA TÀI NGUYÊN)
# --------------------------------------------------------------------------------

# 1. Nhân vật (Sprites) - Scale 1.7
define m2_rosalind = Character("Madam Rosalind", color="#c0392b")
define m2_liam = Character("Doctor Liam", color="#2ecc71")
define m2_sebastian = Character("Sebastian", color="#7f8c8d")
define m2_arthur = Character("Arthur", color="#f39c12")
define m2_player = Character("Tôi", color="#3498db")
define m2_isabella = Character("Isabella", color="#9b59b6")
define m2_victor = Character("Victor", color="#34495e")
define m2_clara = Character("Clara", color="#e056fd")

image rosalind normal = Transform("images/map02/character/Rosalind.png", zoom=1.5)
image liam normal = Transform("images/map02/character/Liam.png", zoom=1.7)
image sebastian normal = Transform("images/map02/character/Sebastian.png", zoom=1.7)
image arthur normal = Transform("images/map02/character/Arthur.png", zoom=1.7)
image arthur nervous = Transform("images/map02/character/Arthur_nervous.png", zoom=1.7)
image isabella normal = Transform("images/map02/character/Isabella.png", zoom=1.7)
image victor normal = Transform("images/map02/character/Victor.png", zoom=1.7)
image clara normal = Transform("images/map02/character/Clara.png", zoom=1.7)

# 2. Backgrounds
image bg map02_outside = Transform("images/map02/background/outside_house.png", size=(1920, 1080))
image bg map02_livingroom = Transform("images/map02/background/living_room.png", size=(1920, 1080))
image bg map02_hallway = Transform("images/map02/background/hallway.jpg", size=(1920, 1080))
image bg map02_gallery = Transform("images/map02/background/gallery.png", size=(1920, 1080)) # Cần thêm file này nếu có
image bg map02_gallery_empty = Transform("images/map02/background/gallary_after_kill.png", size=(1920, 1080))
image bg map02_rosalind_bedroom = Transform("images/map02/background/rosalind_bedroom.png", size=(1920, 1080))
image bg map02_rosalind_bedroom_dead = Transform("images/map02/background/rosalind_bedroom.png", size=(1920, 1080)) # Tạm dùng chung
image bg map02_arthur_room = Transform("images/map02/background/arthur_bedroom.png", size=(1920, 1080)) # Placeholder
image bg map02_backyard = Transform("images/map02/background/arthur_dead.png", size=(1920, 1080)) # Placeholder
image bg m2_true_ending = Transform("images/map02/background/true_ending.jpeg", size=(1920, 1080))
image bg m2_bad_ending = Transform("images/map02/background/bad_ending.jpeg", size=(1920, 1080))

# 3. Âm thanh (Audio Streams)
# Khai báo Audio Channels hoặc File paths
define audio.m2_bgm_intro = "audio/storm.mp3"         # Nhạc bão (Intro)
define audio.m2_bgm_calm = "audio/nhac_khan_phong.mp3"      # Nhạc nhẹ (Tiệc trà) - Placeholder
define audio.m2_bgm_tension = "audio/suspense.mp3"    # Nhạc căng thẳng (Án mạng 1) - Placeholder
define audio.m2_bgm_investigation = "audio/nhac_dieu_tra.mp3" # Nhạc điều tra (Intermission) - Placeholder
define audio.m2_bgm_murder2 = "audio/horror.mp3"      # Nhạc kinh dị (Án mạng 2) - Placeholder
define audio.m2_bgm_climax = "audio/nhac_pha_an.mp3"       # Nhạc cao trào (Đối chất) - Placeholder

# SFX
define audio.sfx_thunder = "audio/thunder.mp3"
define audio.sfx_glass_break = "audio/broken-glass.mp3"
define audio.sfx_door_bang = "audio/hit_door.mp3"

# 4. Biến Manh Mối (Clues) & Tiến độ
# Giai đoạn 2 & 3 (Vụ Rosalind)
default m2_clue_teacup = False            # Tách trà có cặn
default m2_clue_transom = False           # Ô thoáng tróc sơn
default m2_clue_masks_scratched = False   # Mặt nạ bị xước
default m2_clue_arthur_note = False       # Giấy hẹn trong phòng Arthur

# Giai đoạn 4 (Vụ Arthur)
default m2_clue_suicide_note = False      # Thư tuyệt mệnh
default m2_clue_fishing_line = False      # Dây cước dính máu
default m2_clue_arthur_hand = False       # Vết thương nốt ruồi/lỗ thủng trên tay Arthur

# Giai đoạn 5 (Đối chất)
default m2_clue_parker_pen = False        # Bút bị hỏng
default m2_clue_liam_finger = False       # Ngón tay bị đứt

# Biến trạng thái game
default m2_progress_talked_liam = False
default m2_progress_talked_sebastian = False
default m2_progress_talked_isabella = False

# 5. Transforms
transform slow_zoom_in:
    xalign 0.5 yalign 0.5 zoom 1.0
    linear 10.0 zoom 1.2
