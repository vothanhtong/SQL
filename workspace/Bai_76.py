 # BÀI 76: Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list

# def find_max_index(lst):
#     if len(lst) == 0:
#         return None  # Trả về None nếu danh sách rỗng

#     max_value = lst[0]
#     max_index = 0

#     # Duyệt qua danh sách, bắt đầu từ vị trí thứ 1
#     for i in range(1, len(lst)):
#         if lst[i] > max_value:
#             max_value = lst[i]
#             max_index = i

#     return max_index