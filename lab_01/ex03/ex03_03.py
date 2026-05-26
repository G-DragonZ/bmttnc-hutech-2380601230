def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập một danh sách số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))
result = tao_tuple_tu_list(numbers)
print("Tuple sau khi tạo từ danh sách là:", result)