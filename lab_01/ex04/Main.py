from QuanLySinhVien import QuanLySinhVien
qlvs = QuanLySinhVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("********************************")
    print("1. them sinh vien")
    print("2. cap nhat sinh vien")
    print("3. xoa sinh vien")
    print("4. tim kiem sinh vien")
    print("5. sap xep sinh vien theo diem trung binh")
    print("6. sap xep sinh vien theo ten chuyn nganh")
    print("7. hien thi danh sach sinh vien")
    print("8. thoat")
    print("********************************")
    option = int(input("Nhap lua chon cua ban: "))
    if(option == 1):
        qlvs.nhapSinhVien()
        print("Sinh vien da duoc them vao danh sach!")
    elif(option == 2):
        if(qlvs.soLuongSinhVien() > 0):
            ID = int(input("Nhap ID sinh vien can cap nhat: "))
            qlvs.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien trong!")
    elif(option == 3):
        if(qlvs.soLuongSinhVien() > 0):
            ID = int(input("Nhap ID sinh vien can xoa: "))
            isDeleted = qlvs.deleteByID(ID)
            if isDeleted:
                print("Sinh vien da duoc xoa!")
            else:
                print(f"Khong tim thay sinh vien co ID = {ID}")
        else:
            print("Danh sach sinh vien trong!")
    elif(option == 4):
        if(qlvs.soLuongSinhVien() > 0):
            keyword = input("Nhap ten sinh vien can tim kiem: ")
            listSV = qlvs.findByName(keyword)
            qlvs.showSinhVien(listSV)
        else:
            print("Danh sach sinh vien trong!")
    elif(option == 5):
        if(qlvs.soLuongSinhVien() > 0):
            qlvs.sortByDiemTB()
            qlvs.showSinhVien(qlvs.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif(option == 6):
        if(qlvs.soLuongSinhVien() > 0):
            qlvs.sortByName()
            qlvs.showSinhVien(qlvs.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif(option == 7):
        if(qlvs.soLuongSinhVien() > 0):
            qlvs.showSinhVien(qlvs.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif(option == 8):
        break
    else:
        print("Lua chon khong hop le! Vui long chon lai!")
print("Ket thuc chuong trinh!")