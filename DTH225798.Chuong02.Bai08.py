#Lỗi cú pháp (SyntaxError)
print("Hello"  # Thiếu dấu ngoặc đóng

#Lỗi kiểu (TypeError)
s = "Hello" + 5  # Không thể cộng chuỗi với số nguyên

#Lỗi tên (NameError)
print(x)  # x chưa được định nghĩa

#Lỗi chỉ số (IndexError)
list = [1, 2, 3]
print(list[5])  # Chỉ số 5 không tồn tại

#Lỗi giá trị (ValueError)
number = int("abc")  # Không thể chuyển đổi chuỗi không phải số thành số nguyên

#Cách bắt lỗi
#Sử dụng cấu trúc try và except
#Cú pháp
try:
    # Mã có thể gây ra lỗi
except ErrorType:
    # Xử lý lỗi

#Ví dụ
 try:
    result = 10 / 0  # Gây ra lỗi chia cho 0
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0.")