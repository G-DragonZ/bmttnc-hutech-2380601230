from SinhVien import SinhVien
class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        if self.soLuongSinhVien() == 0:
            return 1

        maxId = self.listSinhVien[0]._id
        for sv in self.listSinhVien:
            if maxId < sv._id:
                maxId = sv._id
        return maxId + 1

    def soLuongSinhVien(self):
        return len(self.listSinhVien)
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập ngành học sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập ngành học sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên có ID: = {}", format(ID))
        
    def sortById(self):
        self.listSinhVien.sort(key=lambda x : x._id, reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x : x._name, reverse=False)
    
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x : x._diemTB, reverse=True)
    
    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, name):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if name.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Điểm TB", "Học lực"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
                print("\n")
    def getListSinhVien(self):
        return self.listSinhVien