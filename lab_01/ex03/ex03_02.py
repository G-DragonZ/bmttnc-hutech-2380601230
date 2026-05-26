def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập một danh sách số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))
result = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược là:", result)