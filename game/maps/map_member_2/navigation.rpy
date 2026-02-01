
transform arrow_hover:
    on idle:
        alpha 0.8 zoom 1.0
    on hover:
        alpha 1.0 zoom 1.1

# Screen hiển thị mũi tên điều hướng
screen m2_navigation(left_label=None, right_label=None, down_label=None):
    zorder 100
    
    if left_label:
        imagebutton:
            idle "images/ui/arrow4.png" # Giả định arrow4 là trái
            hover "images/ui/arrow4.png"
            at arrow_hover
            align (0.05, 0.5)
            action Jump(left_label)
            
    if right_label:
        imagebutton:
            idle "images/ui/arrow1.png" # Giả định arrow1 là phải
            hover "images/ui/arrow1.png"
            at arrow_hover
            align (0.95, 0.5)
            action Jump(right_label)
            
    if down_label:
        imagebutton:
            idle "images/ui/arrow3.png" # Giả định arrow3 là xuống/quay lại
            hover "images/ui/arrow3.png"
            at arrow_hover
            align (0.5, 0.95)
            action Jump(down_label)

# Helper screen cho fallback text (Dự phòng chưa có ảnh)
screen fallback_text_display(t, a):
    text t size 40 color "#fff" outlines [(2, "#000", 0, 0)] align a

# Tạm thời dùng Textbutton thay vì Imagebutton nếu chưa có asset
screen m2_simple_nav(room_left=None, room_right=None, room_back=None):
    
    if room_left:
        textbutton "⬅ [room_left[1]]": 
            align (0.02, 0.5)
            text_size 30 text_color "#fff" text_hover_color "#f00" 
            background "#00000080"
            action Jump(room_left[0])
            
    if room_right:
        textbutton "[room_right[1]] ➡": 
            align (0.98, 0.5)
            text_size 30 text_color "#fff" text_hover_color "#f00" 
            background "#00000080"
            action Jump(room_right[0])
            
    if room_back:
        textbutton "⬇ [room_back[1]]": 
            align (0.5, 0.95)
            text_size 30 text_color "#fff" text_hover_color "#f00" 
            background "#00000080"
            action Jump(room_back[0])

