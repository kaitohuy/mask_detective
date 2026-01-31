# Hướng dẫn làm việc nhóm

Để đảm bảo hai thành viên có thể làm việc độc lập và merge code dễ dàng, vui lòng tuân thủ các quy tắc sau:

## Cấu trúc thư mục

Mỗi thành viên sẽ làm việc trong thư mục riêng của mình:

*   **Thành viên 1**: `game/maps/map_member_1/`
*   **Thành viên 2**: `game/maps/map_member_2/`

## Quy tắc đặt tên (Quan trọng!)

Để tránh xung đột khi gộp code, hãy luôn thêm tiền tố (prefix) vào tên của label, biến, và hình ảnh.

### 1. Labels
*   Thành viên 1: `label map1_ten_label:`
*   Thành viên 2: `label map2_ten_label:`

### 2. Biến (Variables)
*   Thành viên 1: `$ map1_bien_so = 10`
*   Thành viên 2: `$ map2_bien_so = 10`

### 3. Hình ảnh (Images)
*   Thành viên 1: `image map1 bg room = "..."`
*   Thành viên 2: `image map2 bg room = "..."`

## Quy trình làm việc

1.  **Code**: Viết code và thêm tài nguyên vào thư mục của bạn.
2.  **Test**: Chạy game, menu sẽ hiện ra cho phép chọn "Map Member 1" hoặc "Map Member 2" để test riêng biệt.
3.  **Merge**: Khi code ổn định, đẩy code lên Git. Do file nằm ở thư mục riêng nên sẽ rất ít khi bị conflict.

## Lưu ý chung

*   Không sửa file `game/script.rpy` trừ khi cần thay đổi menu chính.
*   Không sửa file của thành viên khác.
*   Tài nguyên chung (như UI, font) để ở các thư mục gốc (`game/gui`, `game/images`) nhưng cần thống nhất trước khi sửa.
