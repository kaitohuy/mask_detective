
# Define Images
image bg m1_hall = Transform("images/map01/BG/Main_hall.png", size=(1920, 1080))
image bg m1_hallway = Transform("images/map01/BG/hallway.png", size=(1920, 1080))
image bg m1_bathroom = Transform("images/map01/BG/bath_room.png", size=(1920, 1080))
image bg m1_kitchen = Transform("images/map01/BG/Living_room.png", size=(1920, 1080)) # Using Living Room as placeholder/kitchen area

# Persistent Positions for Selection Screen (X, Y, Zoom, XZoom for each character)
default persistent.m1_sel_v_x = 100
default persistent.m1_sel_v_y = 200
default persistent.m1_sel_v_zoom = 1.0
default persistent.m1_sel_v_xzoom = 1.0

default persistent.m1_sel_l_x = 400
default persistent.m1_sel_l_y = 250
default persistent.m1_sel_l_zoom = 1.0
default persistent.m1_sel_l_xzoom = 1.0

default persistent.m1_sel_e_x = 800
default persistent.m1_sel_e_y = 200
default persistent.m1_sel_e_zoom = 1.0
default persistent.m1_sel_e_xzoom = 1.0

default persistent.m1_sel_s_x = 1100
default persistent.m1_sel_s_y = 250
default persistent.m1_sel_s_zoom = 1.0
default persistent.m1_sel_s_xzoom = 1.0

default persistent.m1_sel_t_x = 1500
default persistent.m1_sel_t_y = 200
default persistent.m1_sel_t_zoom = 1.0
default persistent.m1_sel_t_xzoom = 1.0

screen m1_selection_screen():
    add "bg m1_hall"
    
    # Victor (Left)
    imagebutton:
        idle Transform("m1_v_img", zoom=persistent.m1_sel_v_zoom, xzoom=persistent.m1_sel_v_xzoom)
        hover Transform("m1_v_img", zoom=persistent.m1_sel_v_zoom, xzoom=persistent.m1_sel_v_xzoom, matrixcolor=TintMatrix("#dddddd"))
        focus_mask True
        xpos persistent.m1_sel_v_x
        ypos persistent.m1_sel_v_y
        action Return("victor_leonard")
        tooltip "Victor & Leonard"

    # Leonard (Left-Center)
    imagebutton:
        idle Transform("m1_l_img", zoom=persistent.m1_sel_l_zoom, xzoom=persistent.m1_sel_l_xzoom)
        hover Transform("m1_l_img", zoom=persistent.m1_sel_l_zoom, xzoom=persistent.m1_sel_l_xzoom, matrixcolor=TintMatrix("#dddddd"))
        focus_mask True
        xpos persistent.m1_sel_l_x
        ypos persistent.m1_sel_l_y
        action Return("victor_leonard")
        tooltip "Leonard"

    # Elena (Center)
    imagebutton:
        idle Transform("m1_e_img", zoom=persistent.m1_sel_e_zoom, xzoom=persistent.m1_sel_e_xzoom)
        hover Transform("m1_e_img", zoom=persistent.m1_sel_e_zoom, xzoom=persistent.m1_sel_e_xzoom, matrixcolor=TintMatrix("#dddddd"))
        focus_mask True
        xpos persistent.m1_sel_e_x
        ypos persistent.m1_sel_e_y
        action Return("elena")
        tooltip "Elena"

    # Sophia (Right-Center)
    imagebutton:
        idle Transform("m1_s_img", zoom=persistent.m1_sel_s_zoom, xzoom=persistent.m1_sel_s_xzoom)
        hover Transform("m1_s_img", zoom=persistent.m1_sel_s_zoom, xzoom=persistent.m1_sel_s_xzoom, matrixcolor=TintMatrix("#dddddd"))
        focus_mask True
        xpos persistent.m1_sel_s_x
        ypos persistent.m1_sel_s_y
        action Return("sophia")
        tooltip "Sophia"

    # Thomas (Right)
    imagebutton:
        idle Transform("m1_t_img", zoom=persistent.m1_sel_t_zoom, xzoom=persistent.m1_sel_t_xzoom)
        hover Transform("m1_t_img", zoom=persistent.m1_sel_t_zoom, xzoom=persistent.m1_sel_t_xzoom, matrixcolor=TintMatrix("#dddddd"))
        focus_mask True
        xpos persistent.m1_sel_t_x
        ypos persistent.m1_sel_t_y
        action Return("thomas")
        tooltip "Thomas"
        
    # Tooltip Logic
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" size 40 color "#ffffff" outlines [(2, "#000", 0, 0)] align (0.5, 0.1)
    
    # DEV Overlay and Poser Tool
    use m1_dev_overlay
    use m1_poser_tool

# Characters Images
image m1_v_img = "images/map01/character/victor.png"
image m1_l_img = "images/map01/character/leonard_stand.png"
image m1_s_img = "images/map01/character/sophia_stand.png"
image m1_e_img = "images/map01/character/elena_before_killed_stand.png"
image m1_t_img = "images/map01/character/Thomas_Serve.png"

# Define Characters with Images
define m1_v = Character("Victor", color="#800000", image="m1_v_img")
define m1_l = Character("Leonard", color="#000080", image="m1_l_img")
define m1_s = Character("Sophia", color="#FF69B4", image="m1_s_img")
define m1_e = Character("Elena", color="#800080", image="m1_e_img")
define m1_t = Character("Thomas", color="#ADD8E6", image="m1_t_img")
define m1_nv = Character(None, kind=nvl)

# Persistent Character Transforms
# Default values in PIXELS: xpos (0-1920), ypos (0-1080, where 1080=bottom), zoom, xzoom
default persistent.m1_v_xpos = 200
default persistent.m1_v_ypos = 1080
default persistent.m1_v_zoom = 1.0
default persistent.m1_v_xzoom = 1.0

default persistent.m1_l_xpos = 400
default persistent.m1_l_ypos = 1080
default persistent.m1_l_zoom = 1.0
default persistent.m1_l_xzoom = 1.0

default persistent.m1_s_xpos = 1400
default persistent.m1_s_ypos = 1080
default persistent.m1_s_zoom = 1.0
default persistent.m1_s_xzoom = 1.0

default persistent.m1_e_xpos = 960
default persistent.m1_e_ypos = 1080
default persistent.m1_e_zoom = 1.0
default persistent.m1_e_xzoom = 1.0

default persistent.m1_t_xpos = 1700
default persistent.m1_t_ypos = 1080
default persistent.m1_t_zoom = 1.0
default persistent.m1_t_xzoom = 1.0

transform m1_v_tf:
    xpos persistent.m1_v_xpos ypos persistent.m1_v_ypos
    xanchor 0.5 yanchor 1.0
    zoom persistent.m1_v_zoom xzoom persistent.m1_v_xzoom

transform m1_l_tf:
    xpos persistent.m1_l_xpos ypos persistent.m1_l_ypos
    xanchor 0.5 yanchor 1.0
    zoom persistent.m1_l_zoom xzoom persistent.m1_l_xzoom

transform m1_s_tf:
    xpos persistent.m1_s_xpos ypos persistent.m1_s_ypos
    xanchor 0.5 yanchor 1.0
    zoom persistent.m1_s_zoom xzoom persistent.m1_s_xzoom

transform m1_e_tf:
    xpos persistent.m1_e_xpos ypos persistent.m1_e_ypos
    xanchor 0.5 yanchor 1.0
    zoom persistent.m1_e_zoom xzoom persistent.m1_e_xzoom

transform m1_t_tf:
    xpos persistent.m1_t_xpos ypos persistent.m1_t_ypos
    xanchor 0.5 yanchor 1.0
    zoom persistent.m1_t_zoom xzoom persistent.m1_t_xzoom

# Variables
default m1_mind = 100
default m1_fear = "None"
default m1_time = 7
default m1_clues = [] # List of strings
default m1_evidence = [] # List of strings
default m1_inventory = [] # List of strings
default m1_affection = {
    "Leonard": 0,
    "Sophia": 0,
    "Elena": 0,
    "Thomas": 0
}
default m1_suspect_choice = ""

# Notebook & Puzzle Variables
default m1_puzzle_eyes_idx = 0
default m1_puzzle_border_idx = 0
default m1_puzzle_feather_idx = 0
default m1_puzzle_solved = False

define m1_eye_options = ["Tròn", "Mắt Mèo", "Vuông"]
define m1_border_options = ["Bạc", "Vàng", "Đồng"]
define m1_feather_options = ["Không có", "Xanh", "Tím"]

# UI Images
image ui_icon_book = "images/map01/UI/closebook.png"
image ui_bg_book = "images/map01/UI/openbook.png"

screen m1_hud():
    zorder 100
    
    # === STATUS PANEL (Top-Left) ===
    frame:
        xalign 0.0
        yalign 0.0
        xmargin 15
        ymargin 15
        padding (15, 12)
        background Solid("#000000CC")
        
        vbox:
            spacing 6
            
            # Mind
            hbox:
                spacing 8
                text "🧠" size 18
                text "Mind:" size 16 color "#aaa"
                text "[m1_mind]" size 16 color "#0f0" bold True
            
            # Fear
            hbox:
                spacing 8
                text "😨" size 18
                text "Nỗi sợ:" size 16 color "#aaa"
                if m1_fear and m1_fear != "None":
                    text "[m1_fear]" size 14 color "#f88"
                else:
                    text "Không" size 14 color "#888"
            
            # Time/Days
            hbox:
                spacing 8
                text "⏰" size 18
                text "Thời gian:" size 16 color "#aaa"
                text "[m1_time]" size 16 color "#ff0" bold True
    
    # === TOOLBAR (Top-Right) ===
    hbox:
        xpos 1780
        ypos 10
        spacing 15
        
        # Inventory Button
        imagebutton:
            idle Transform("images/map01/UI/bag.png", zoom=0.35)
            hover Transform("images/map01/UI/bag.png", zoom=0.4, matrixcolor=TintMatrix("#ffff88"))
            action Show("m1_inventory_screen")
        
        # Notebook Button  
        imagebutton:
            idle Transform("images/map01/UI/closebook.png", zoom=0.35)
            hover Transform("images/map01/UI/closebook.png", zoom=0.4, matrixcolor=TintMatrix("#ffff88"))
            action ShowMenu("m1_notebook")

screen m1_dev_overlay():
    zorder 200
    # Developer Toggle
    textbutton "DEV":
        xalign 0.02
        yalign 0.02
        text_color "#ffffff"
        action [SetVariable("m1_poser_active", True), Show("m1_poser_tool")]

screen m1_notebook():
    modal True
    tag menu
    
    # Dim background
    add Solid("#00000080")

    # Main Notebook Paper Frame
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 800
        background Solid("#FFF5E1") # Paper color
        padding (50, 50)

        default current_tab = "notes"

        vbox:
            xalign 0.5
            yalign 0.0
            spacing 20

            # Title / Header
            hbox:
                xalign 0.5
                spacing 20
                add "ui_bg_book" yalign 0.5 zoom 0.5 # Small icon header
                text "SỒ TAY ĐIỀU TRA" color "#3e2723" size 50 yalign 0.5 bold True

            # Tabs
            hbox:
                xalign 0.5
                spacing 50
                textbutton "Ghi Chú" action SetScreenVariable("current_tab", "notes") text_color "#3e2723" text_hover_color "#d7ccc8"
                textbutton "Ghép Mặt Nạ" action SetScreenVariable("current_tab", "puzzle") text_color "#3e2723" text_hover_color "#d7ccc8"
                textbutton "Đóng" action Return() text_color "#b71c1c"

            # Content Area
            if current_tab == "notes":
                use m1_notebook_notes
            elif current_tab == "puzzle":
                use m1_notebook_puzzle

screen m1_notebook_notes():
    viewport:
        xsize 900 ysize 500
        xalign 0.5
        scrollbars "vertical"
        mousewheel True
        
        vbox:
            spacing 10
            if not m1_clues:
                text "Chưa có manh mối nào." color "#000"
            else:
                for clue in m1_clues:
                    text "• [clue]" color "#000" size 25

screen m1_notebook_puzzle():
    vbox:
        xalign 0.5
        spacing 30
        
        text "Tái tạo đặc điểm hung thủ:" color "#000" xalign 0.5

        # Eye Shape
        hbox:
            spacing 20
            text "Dáng Mắt:" color "#333" min_width 200
            textbutton "<" action SetVariable("m1_puzzle_eyes_idx", (m1_puzzle_eyes_idx - 1) % 3)
            text "[m1_eye_options[m1_puzzle_eyes_idx]]" color "#000" min_width 150 xalign 0.5
            textbutton ">" action SetVariable("m1_puzzle_eyes_idx", (m1_puzzle_eyes_idx + 1) % 3)

        # Border
        hbox:
            spacing 20
            text "Viền:" color "#333" min_width 200
            textbutton "<" action SetVariable("m1_puzzle_border_idx", (m1_puzzle_border_idx - 1) % 3)
            text "[m1_border_options[m1_puzzle_border_idx]]" color "#000" min_width 150 xalign 0.5
            textbutton ">" action SetVariable("m1_puzzle_border_idx", (m1_puzzle_border_idx + 1) % 3)

        # Feather
        hbox:
            spacing 20
            text "Lông Vũ:" color "#333" min_width 200
            textbutton "<" action SetVariable("m1_puzzle_feather_idx", (m1_puzzle_feather_idx - 1) % 3)
            text "[m1_feather_options[m1_puzzle_feather_idx]]" color "#000" min_width 150 xalign 0.5
            textbutton ">" action SetVariable("m1_puzzle_feather_idx", (m1_puzzle_feather_idx + 1) % 3)

        textbutton "Xác Nhận Đối Chiếu":
            xalign 0.5
            action Function(m1_check_puzzle)

    if m1_puzzle_solved:
        text "Chính xác! Đã mở khóa manh mối mới." color "#008000" xalign 0.5 yalign 0.8

# Init Python for Mechanics
init python:
    import random

    def m1_check_puzzle():
        global m1_puzzle_solved
        
        # Target: Cat Eye (1), Gold Border (1), Purple Feather (2)
        target_eye = 1
        target_border = 1
        target_feather = 2
        
        if (m1_puzzle_eyes_idx == target_eye and 
            m1_puzzle_border_idx == target_border and 
            m1_puzzle_feather_idx == target_feather):
            
            m1_puzzle_solved = True
            msg = "Mặt Nạ Hung Thủ: Mắt mèo + Viền vàng + Lông vũ tím"
            if msg not in m1_clues:
                m1_clues.append(msg)
                renpy.notify("SUY LUẬN CHÍNH XÁC!")
        else:
            renpy.notify("Suy luận chưa chính xác.")

    def m1_init_game():
        global m1_mind, m1_time, m1_clues, m1_evidence, m1_inventory, m1_affection, m1_fear
        m1_mind = 100
        m1_time = 7
        m1_clues = []
        m1_evidence = []
        m1_inventory = []
        m1_affection = {"Leonard": 0, "Sophia": 0, "Elena": 0, "Thomas": 0}
        
        fears = ["Mysophobia", "Claustrophobia", "Necrophobia", "Aquaphobia", "Monophobia", "Enochlophobia"]
        m1_fear = random.choice(fears)

    def m1_reduce_mind(amount, reason=""):
        global m1_mind
        m1_mind -= amount
        renpy.notify(f"Mind -{amount} ({reason})")
        if m1_mind <= 0:
            renpy.jump("m1_bad_end_3")

    def m1_has_fear(fear_name):
        return m1_fear == fear_name

    def m1_gain_affection(char_name, amount):
        global m1_affection
        if m1_has_fear("Enochlophobia"):
            amount = int(amount * 0.65)
        
        if char_name in m1_affection:
            m1_affection[char_name] = min(100, m1_affection[char_name] + amount)
            renpy.notify(f"Thiện cảm {char_name} +{amount}")

    def m1_add_clue(clue_text):
        global m1_clues
        if clue_text not in m1_clues:
            m1_clues.append(clue_text)
            renpy.notify("Đã thêm manh mối!")

    def m1_add_evidence(ev_text):
        global m1_evidence
        if ev_text not in m1_evidence:
            m1_evidence.append(ev_text)
            renpy.notify("Đã thu thập vật chứng!")

    def m1_add_inventory(item):
        global m1_inventory
        if item not in m1_inventory:
            m1_inventory.append(item)
            renpy.notify(f"Đã nhận vật phẩm: {item}")

label map1_start:
    $ m1_init_game()
    show screen m1_dev_overlay
    show screen m1_poser_tool
    
    scene bg m1_hall
    show m1_v_img at m1_v_tf
    show m1_l_img at m1_l_tf
    
    # --- PHASE 1: INTRO ---
    
    # Scene 1: Party
    "Nỗi sợ của bạn là: [m1_fear]"
    "Dạ tiệc của những chiếc mặt nạ. Nơi danh tính bị xóa nhòa."
    "Đại sảnh biệt thự lộng lẫy, ánh đèn vàng kim, nhạc cổ điển du dương."
    "Trong thế giới của những chiếc mặt nạ, danh tính bị xóa nhòa. Muốn nhớ ai, phải nhớ trang phục và những phụ kiện nhỏ nhất trên người họ."

    # Scene 2: The Conflict
    "Tại một góc khuất trong đại sảnh..."
    "Tại một góc khuất trong đại sảnh..."
    show m1_v_img at m1_v_tf
    show m1_l_img at m1_l_tf
    m1_l "Mày... mày sẽ hủy hoại tất cả chúng tao!"
    "Leonard túm cổ áo Victor, mặt đỏ gay. Victor chỉ nhếch mép cười."
    hide m1_v_img
    hide m1_l_img
    
    "Cách đó không xa, Sophia đang lo lắng, hai tay xoắn vào nhau."
    "Elena quan sát điềm tĩnh, ánh mắt sắc lạnh."
    "Cách đó không xa, Sophia đang lo lắng, hai tay xoắn vào nhau."
    "Elena quan sát điềm tĩnh, ánh mắt sắc lạnh."
    show m1_e_img at m1_e_tf
    m1_e "Cậu thấy chưa Sophia? Hắn ta sẽ hủy hoại tất cả chúng ta."
    "Câu nói khiến Sophia càng thêm hoảng loạn."
    hide m1_e_img

    # Scene 3: Choice (Interactive)
    # Hide characters to use the screen's imagebuttons
    hide m1_v_img
    hide m1_l_img
    hide m1_e_img
    hide m1_s_img
    
    "Hãy chọn một người để trò chuyện..."
    call screen m1_selection_screen

    $ choice = _return

    if choice == "victor_leonard":
        jump m1_talk_victor_leonard
    elif choice == "sophia":
        jump m1_talk_sophia
    elif choice == "elena":
        jump m1_talk_elena
    elif choice == "thomas":
        jump m1_talk_thomas

label m1_talk_victor_leonard:
    $ m1_add_clue("Victor và Leonard có xích mích")
    "Victor đang uống rượu mạnh để kìm nén."
    "Hắn lầm bầm: 'Hắn ta phải biến mất.'"
    "Victor chỉnh lại cà vạt, khoe khoang sắp công bố bí mật hủy diệt Leonard."
    jump m1_scene_4

label m1_talk_sophia:
    $ m1_add_clue("Son môi Sophia: Màu đỏ rượu vang")
    $ m1_add_clue("Sophia khen mặt nạ Mèo của Elena")
    m1_s "Elena vừa tặng tôi thỏi son màu đỏ rượu vang này, cô ấy nói nó giúp tôi mạnh mẽ hơn."
    m1_s "Mặt nạ dáng mắt mèo của cậu ấy đẹp thật."
    jump m1_scene_4

label m1_talk_elena:
    $ m1_add_clue("Mặt nạ Elena: Dáng mắt mèo + Viền vàng + Chùm lông vũ tím")
    "Elena cầm ly rượu, mỉm cười thân thiện."
    "Cô khen chiếc khăn tay thêu tên của Sophia để gây sự chú ý vào nó."
    "Tôi ghi nhớ chiếc mặt nạ Elena đang đeo: Dáng mắt mèo, viền mạ vàng, và có chùm lông vũ tím bên thái dương."
    jump m1_scene_4

label m1_talk_thomas:
    $ m1_gain_affection("Thomas", 20)
    m1_t "Tôi đặc biệt ấn tượng với những chiếc lông vũ trang trí hôm nay."
    "Anh ta than thở về việc khó nhớ mặt khách."
    jump m1_scene_4

label m1_scene_4:

    # Scene 4: The Drink
    "Victor quay lại nhóm phụ nữ."
    "Sophia cầm một ly rượu vang đỏ đưa cho Victor. Victor uống cạn một hơi để thể hiện sự ngạo nghễ."
    "Leonard nhìn theo với ánh mắt hằn học."
    
    # Scene 5: The Shadow
    "Victor say, lảo đảo đi vào hành lang dẫn tới nhà tắm."
    if m1_has_fear("Claustrophobia"):
        $ m1_reduce_mind(10, "Sợ không gian hẹp (Hành lang)")
        
    "Victor đi khuất sau hành lang tối."
    "Ngay sau đó, một bóng người lướt theo. Tôi không thấy rõ toàn thân, chỉ thấy chi tiết chùm lông vũ màu tím đung đưa."
    
    # Scene 6: The Scream
    scene black
    stop music
    play sound "audio/glass_break.ogg" # Placeholder
    "XOẢNG!"
    m1_t "CÓ NGƯỜI CHẾT! ÔNG VICTOR...!!!"
    
    # Scene 7: Crime Scene (Interactive)
    scene bg m1_bathroom
    if m1_has_fear("Aquaphobia"):
        $ m1_reduce_mind(10, "Sợ nước (Nhà tắm)")

    "Victor nằm gục, mép có bọt trắng."
    "Tôi phải khám nghiệm hiện trường..."
    
    # Show interactive crime scene
    call screen m1_crime_scene
    
    "Thomas run rẩy nép cửa. Leonard, Sophia, Elena chạy tới."
    
    # --- PHASE 2: INVESTIGATION ---
    
    "Giai đoạn Điều Tra bắt đầu. Tôi có [m1_time] đơn vị thời gian."
    jump m1_investigation_hub

label m1_investigation_hub:
    show screen m1_hud
    if m1_time <= 0 or m1_mind <= 0:
        jump m1_judgment_start

    # Use interactive investigation screen
    call screen m1_investigation_screen
    $ _choice = _return
    
    if _choice == "thomas":
        if m1_mind < 7:
            "Không đủ Mind."
            jump m1_investigation_hub
        $ m1_reduce_mind(7, "Phỏng vấn")
        m1_t "Tôi đứng ở góc khuất nên không thấy rõ mặt. Nhưng lúc người đó đi ngang qua ánh đèn, tôi chắc chắn đã thấy một chùm lông vũ màu tím rất lớn bên thái dương."
        $ m1_gain_affection("Thomas", 20)
        $ m1_add_clue("Thomas: Hung thủ có lông vũ tím trên mặt nạ")
        if m1_affection["Thomas"] >= 100:
            "Thomas có vẻ tin tưởng tôi hoàn toàn."
        jump m1_investigation_hub

    elif _choice == "leonard":
        if m1_mind < 7:
            "Không đủ Mind."
            jump m1_investigation_hub
        if m1_affection["Leonard"] > 50:
            "Leonard trả lời không do dự."
        else:
            $ m1_reduce_mind(7, "Phỏng vấn")
        
        m1_l "Tôi chả quan tâm. Nhưng lúc tôi đi lấy rượu, tôi thấy một người phụ nữ lảng vảng gần hành lang. Mặt nạ của cô ta có viền vàng phản chiếu chói cả mắt."
        $ m1_add_clue("Leonard: Hung thủ có viền vàng trên mặt nạ")
        jump m1_investigation_hub

    elif _choice == "sophia":
        if m1_mind < 7:
            "Không đủ Mind."
            jump m1_investigation_hub
        if m1_affection["Sophia"] > 50:
            "Sophia trả lời thành thật."
        else:
            $ m1_reduce_mind(7, "Phỏng vấn")
        m1_s "Lúc nãy tôi thấy Elena... à không, tôi không chắc. Nhưng tôi nhớ Elena rất thích chiếc mặt nạ dáng mắt mèo của cô ấy."
        $ m1_add_clue("Sophia: Elena thích mặt nạ mắt mèo")
        jump m1_investigation_hub

    elif _choice == "elena":
        if m1_mind < 7:
            "Không đủ Mind."
            jump m1_investigation_hub
        $ m1_reduce_mind(7, "Phỏng vấn")
        m1_e "Tôi chẳng thấy gì cả. Tôi đang ở trong phòng nghỉ. Tại sao các người cứ hỏi tôi?"
        "Elena có vẻ né tránh câu hỏi."
        $ m1_add_clue("Elena: Tỏ vẻ né tránh khi bị hỏi")
        jump m1_investigation_hub

    elif _choice == "search_hallway":
        "Tìm thấy Khăn tay thêu chữ 'S.V'."
        $ m1_add_inventory("Khăn Tay")
        "Quá lộ liễu. Kẻ sát nhân không ngu ngốc đến mức đánh rơi vật định danh mình ngay lối đi. Đây là bẫy. (-7 Mind)"
        $ m1_reduce_mind(7, "Suy luận")
        jump m1_investigation_hub

    elif _choice == "search_bathroom":
        if m1_has_fear("Necrophobia"):
            $ m1_reduce_mind(30, "Sợ xác chết")
        "Ly rượu có vết son môi."
        $ m1_add_evidence("Ly Rượu Vết Son")
        "Vết son trùng màu với son Sophia."
        jump m1_investigation_hub
    
    elif _choice == "open_trash":
        # Fear check
        if m1_has_fear("Mysophobia"):
            $ m1_reduce_mind(10, "Sợ bẩn")
            "Tôi run rẩy nhìn vào thùng rác... (-10 Mind)"
        
        # Open trash bin puzzle
        call screen m1_trash_bin_puzzle
        $ _trash_result = _return
        
        if _trash_result == "found_lipstick":
            "Tìm thấy một thỏi son bị bẻ gãy đầu!"
            $ m1_add_evidence("Thỏi Son Gãy")
            $ m1_lipstick_found = True
            
            if m1_affection["Thomas"] >= 100:
                "Thomas chỉ cho tôi một thứ khác."
                "Một vỏ viên thuốc con nhộng (Capsule) rỗng."
                $ m1_add_evidence("Vỏ Thuốc")
                "Nó rất trơn, khó tách đôi khi đeo găng. Tôi tìm thấy một dấu vân tay rõ nét!"
                $ m1_add_evidence("Dấu Vân Tay")
                "Tôi lén lấy dấu vân tay trên ly rượu Elena uống dở ở sảnh để đối chiếu... TRÙNG KHỚP 100%"
        
        jump m1_investigation_hub

    elif _choice == "judgment":
        jump m1_judgment_start
    
    jump m1_investigation_hub

label m1_judgment_start:
    hide screen m1_hud
    scene bg m1_hall # Back to hall for judgment
    "Thời khắc phán quyết đã điểm."
    
    "Leonard và Elena hùa nhau buộc tội Sophia dựa trên 'Khăn tay' và 'Vết son'."
    m1_s "Không phải tôi! Tôi bị oan!"
    m1_e "Bằng chứng rành rành ra đó!"
    
    menu:
        "Ai là hung thủ?"
        
        "Sophia":
            $ m1_suspect_choice = "Sophia"
            jump m1_bad_end_1
            
        "Leonard":
            $ m1_suspect_choice = "Leonard"
            jump m1_bad_end_1
            
        "Elena":
            $ m1_suspect_choice = "Elena"
            jump m1_judgment_elena

label m1_judgment_elena:
    "Tôi cáo buộc Elena."
    m1_e "Anh nói gì vậy? Bằng chứng đâu?"
    
    # Step 1
    if "Thỏi Son Gãy" in m1_evidence:
        "Tôi đưa ra Thỏi son gãy."
        "Kẻ sát nhân đã dùng cây son này để lại vệt trên miệng ly, chứ không phải Sophia."
        "Cô đã nhận son từ Elena, nên Elena cũng có thể có một cây tương tự."
        "Khăn tay chỉ là cái bẫy vụng về."
    else:
        "Tôi không đủ bằng chứng để phản biện về vết son..."
        
    # Step 2
    m1_e "Mặt nạ của tôi màu Bạc, không hề có lông vũ!" 
    "(Cô ta giơ mặt nạ hiện tại ra)"
    
    if "Mặt Nạ Hung Thủ: Mắt mèo + Viền vàng + Lông vũ tím" in m1_clues:
        "Tôi tung ra 3 Lời khai (Thomas, Leonard, Sophia)."
        "Thomas thấy lông vũ tím, Leonard thấy viền vàng, Sophia xác nhận dáng mắt mèo."
        "Cộng lại chính là chiếc mặt nạ cô đeo lúc đầu buổi tiệc! Cô đã thay nó sau khi giết Victor!"
    else:
        "Tôi không thể chứng minh cô ta đã thay mặt nạ..."
        jump m1_bad_end_1
         
    # Step 3
    if "Dấu Vân Tay" in m1_evidence:
        "Elena vẫn cứng đầu: 'Đó chỉ là suy đoán. Không có bằng chứng tôi ở hiện trường.'"
        "Tôi đưa ra Vỏ thuốc con nhộng & Kết quả đối chiếu dấu vân tay."
        "Cô rất cẩn thận đeo găng tay khi vẽ son. Nhưng chiếc vỏ thuốc con nhộng trơn tuột đã hại cô."
        "Cô buộc phải tháo găng tay ra để tách nó, và dấu vân tay của cô đã in vĩnh viễn trên hung khí giết người này!"
        jump m1_true_end
    else:
        m1_e "Chỉ là suy đoán vô căn cứ."
        jump m1_bad_end_1

label m1_bad_end_1:
    "BAD ENDING: Kết tội sai"
    "Sophia bị còng tay, gào khóc thảm thiết."
    "Leonard nhìn theo vô cảm."
    "Elena đứng trong góc tối, mỉm cười, ném chiếc mặt nạ cũ (có lông vũ tím) vào lò sưởi đang cháy."
    "Lửa nuốt chửng bằng chứng cuối cùng."
    "GAME OVER"
    return

label m1_bad_end_3:
    hide screen m1_hud
    "BAD ENDING: Thám tử kém cỏi"
    "Tâm trí tôi mụ mị. Tôi không thể suy luận được nữa."
    "Elena đứng trong góc tối, mỉm cười, ném chiếc mặt nạ cũ vào lò sưởi."
    "GAME OVER"
    return

label m1_true_end:
    "Elena bị vạch trần. Cô ta ngửa mặt cười lớn, ánh mắt trở nên điên dại."
    m1_e "Khá lắm. Ta đã tính hết mọi nước cờ, trừ cái vỏ thuốc chết tiệt đó."
    
    "Elena bất ngờ rút ra một quả bom khói, ném mạnh xuống sàn."
    "Khói mù mịt tỏa ra. Tiếng kính vỡ choang."
    
    "Tôi chạy đến bên cửa sổ: Một chiếc trực thăng đen bay sát sạt, thả dây xuống."
    "Elena đu dây tẩu thoát, bỏ lại hiện trường hỗn loạn."
    
    "Tuy hung thủ chạy thoát, nhưng Sophia được minh oan."
    "Tôi nhận được tin nhắn từ Elena: 'Ván cờ mới chỉ bắt đầu.'"
    "TRUE ENDING (Phá án thành công)"
    return
