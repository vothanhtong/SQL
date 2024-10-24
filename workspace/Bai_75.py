# # BÀI 75 :Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số Armstrong hay không
# def is_armstrong(a):
#     # Chuyển số thành chuỗi để dễ dàng đếm số chữ số và truy cập từng chữ số
#     digits = str(a)
#     n = len(digits)
    
#     # Tính tổng các lũy thừa của từng chữ số lên mũ số lượng chữ số
#     sum_of_powers = sum(int(digit) ** n for digit in digits)
    
#     # Kiểm tra xem tổng có bằng số ban đầu hay không
#     return sum_of_powers == a