#Toán tử chia /
#Thực hiện phép chia và trả về kết quả là một số thực (float)
print("10/3 = ",10/3)

#Toán tử chia lấy phần nguyên //
#Thực hiện phép chia nguyên và trả về kết quả là phần nguyên
print("10//3: ",10//3)

#Toán tử chia lấy dư %
#Thực hiện phép chia và trả về kết quả là phần dư
print("10%3: ",10%3)

#Toán tử mũ **
#Thực hiện phép lũy thừa, lấy số ở bên trái làm cơ số và số ở bên phải làm số mũ.
print("2**3: ",2**3)

#Toán tử logic and
#Toán tử này trả về True nếu cả hai biểu thức đều đúng. Nếu một trong hai biểu thức sai, nó sẽ trả về False
print("(6>3) and (7>4):", (6>3)and(7>4))

#Toán tử logic or
#Toán tử này trả về True nếu ít nhất một trong hai biểu thức đúng. Nếu cả hai đều sai, nó sẽ trả về False.
print("(6 > 3) or (8 < 5): ",(6 > 3) or (8 < 5))

#Toán tử so sánh is
#Toán tử này được sử dụng để kiểm tra xem hai biến có cùng
#một đối tượng trong bộ nhớ hay không (tức là xem chúng có tham chiếu đến cùng một đối tượng hay không).
a = [1, 2, 3]
b = a
print("a is b: ",a is b)