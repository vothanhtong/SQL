# # BÀi 77: Viết hàm đưa vào một list số nguyên và một số nguyên dương k.
# #  Hãy tìm và trả về vị trí của phần tử đầu tiên có giá trị k trong list số nguyên, nếu không có thì trả về -1
# def find_first_occurrence(lst, k):
#     # Duyệt qua danh sách
#     for index in range(len(lst)):
#         if lst[index] == k:
#             return index  # Trả về vị trí đầu tiên tìm thấy
#     return -1  # Trả về -1 nếu không tìm thấy