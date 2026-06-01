def tinh_tong_so_chan(lst):
 tong=0
 for i in lst:
  if i%2==0:
   tong+=i
 return tong
input_list = input("Nhập một danh sách số nguyên, cách nhau bằng dấu phẩy: ")
numbers = [int(x.strip()) for x in input_list.split(",")]
result = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong danh sách là:", result)