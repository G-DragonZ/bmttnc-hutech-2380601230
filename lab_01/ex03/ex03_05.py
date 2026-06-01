def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_string = input("Nhập một chuỗi, các từ cách nhau bằng dấu cách: ")
words_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(words_list)
print("Số lần xuất hiện của mỗi từ trong chuỗi là:",so_lan_xuat_hien)