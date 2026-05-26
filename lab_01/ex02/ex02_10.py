def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_str = input("Nhap chuoi: ")
reversed_str = dao_nguoc_chuoi(input_str)
print("Chuoi sau khi dao nguoc la: " + reversed_str)