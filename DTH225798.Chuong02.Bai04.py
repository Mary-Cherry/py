#Kiểu số nguyên
#VD: 3, 5, 10
from operator import index

x = 9
print("Gia tri cua x: ",x)
print("Kieu du lieu cua x: ",type(x))

#Kiểu số thực
#VD: 1.5, 4.4
y = 3.14
print("Gia tri cua y: ",y)
print("Kieu du lieu cua y: ",type(y))

#Kiểu boolean (bool)
#Có 2 giá trị là True (đúng) và False (sai)
#Được sử dụng để kiểm tra các điều kiện trong các câu lệnh điều khiển, như câu lệnh if-else hoặc vòng lặp while.
#Sử dụng các toán tử so sánh (ví dụ: >, <, >=, <=, ==, !=) để so sánh các giá trị và trả về kết quả là True hoặc False.
z = 10
t = 20
print("z > t: ", z > t)
print("z < t: ",z < t)
print("z == t: ",z == t)
print("z != t: ",z != t)

#Kiểu số phức (complex)
#Kiểu số phức được sử dụng để lưu trữ các số phức, trong đó một số phức có dạng "a + bi", trong đó a và b là các số thực và i là đơn vị ảo.

z = 4 + 5j
print("Gia tri cua z: ",z)
print("Kieu du lieu cua z: ",type(z))
#Phep cong so phuc
w = 2 + 1j
s = z + w
print("Tong cua z va w: ",s)
#Phep nhan so phuc
p = z * w
print("Tich cua z va w: ",p)