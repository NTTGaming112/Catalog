class ContributorWithType:
    """Lấy tên từ lớp Contributor và thêm nghề nghiệp của người đóng góp."""
    def __init__(self,contributor,type):
        self.contributor = Contributor(contributor)
        self._type = type   
class Contributor:
    """Đại diện cho tên người đóng góp."""
    def __init__(self,name):
        self.name = name

class LibraryItem:
    """Lớp cơ sở cho các mục trong thư viện, chứa thông tin chung."""
    def __init__(self, title, upc, subject, contributors):
        self.title = title
        self.upc = upc
        self.subject = subject
        self.contributors = contributors
class Book(LibraryItem):
    """Đại diện cho một cuốn sách trong thư viện."""
    def __init__(self, title, upc, subject, contributors, isbn, dds_number):
        super().__init__(title, upc, subject, contributors)
        self.isbn = isbn
        self.dds_number = dds_number
class CD(LibraryItem):
    """Đại diện cho một CD trong thư viện."""
    pass
class DVD(LibraryItem):
    """Đại diện cho một DVD trong thư viện."""
    def __init__(self, title, upc, subject, contributors, genre):
        super().__init__(title, upc, subject, contributors)
        self.genre = genre
class Magazine(LibraryItem):
    """Đại diện cho một cuốn tạp chí trong thư viện."""
    def __init__(self, title, upc, subject, contributors, volume, issue):
        super().__init__(title, upc, subject, contributors)
        self.volume = volume
        self.issue = issue

class Catalog:
    """Danh mục của thư viện, chứa các mục thư viện."""
    def __init__(self):
        self.items = []
        self.contributors = []
    def add_item(self, item):
        """Thêm một mục vào danh mục."""
        self.items.append(item)
    def add_contributor(self, contributor):
        """Thêm một người đóng góp vào danh mục."""
        self.contributors.append(contributor)
    def search(self, search_key,key):
        """Tìm kiếm mục trong danh mục."""
        if key == '1':
            return [item for item in self.items if search_key.lower() in item.title[0]]  
        elif key == '2':
            return [item for item in self.items if search_key.lower() in item.upc[0]]   
        elif key == '3':
            return [item for item in self.items if search_key.lower() in item.subject[0]]  
        elif key == '4':
            return [item for i in self.contributors if search_key.lower() in i.contributor.name.lower() for item in self.items]   
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        return '1'

def main_menu():
    """Hiển thị menu chính và xử lý lựa chọn của người dùng."""
    catalog = Catalog()
    while True:
        print("===== Menu Chính =====")
        [print(i) for i in ["1. Thêm item", "2. Thêm contributor","3. Tìm kiếm", "4. Thoát"]]
        choice = input("Nhập lựa chọn của bạn (1-4): ") 
        if choice == '1':
            while True:
                print("===== Thêm item =====")
                [print(i) for i in ["1. Sách", "2. CD", "3. DVD", "4. Tạp chí"]]
                type = input("Nhập lựa chọn (1-4): ").strip()
                if type == '1':
                    print("===== Sách =====")
                    a = list(input(f"Nhập {i}: ").strip().split(",") for i in ["Title", "UPC", "Subject", "Contributors (cách nhau bởi dấu ',')", "ISBN", "DDS Number"])
                    book = Book(*a)
                    catalog.add_item(book)
                    break
                elif type == '2':
                    print("===== CD =====")
                    a = list(input(f"Nhập {i}: ").strip().split(",") for i in ["Title", "UPC", "Subject", "Contributors (cách nhau bởi dấu ',')"])
                    cd = CD(*a)
                    catalog.add_item(cd)
                    break
                elif type == '3':
                    print("===== DVD =====")
                    a = list(input(f"Nhập {i}: ").strip().split(",") for i in ["Title", "UPC", "Subject", "Contributors (cách nhau bởi dấu ',')", "Genre"])
                    dvd = DVD(*a)
                    catalog.add_item(dvd)
                    break
                elif type == '4':
                    print("===== Tạp chí =====")
                    a = list(input(f"Nhập {i}: ").strip().split(",") for i in ["Title", "UPC", "Subject", "Contributors (cách nhau bởi dấu ',')", "Volume", "Issue"])
                    manazine = Magazine(*a)
                    catalog.add_item(manazine)
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        elif choice == '2':
            print("===== Thêm contributor =====")
            a = [input(f"Nhập {i}: ").strip() for i in ["tên","nghề nghiệp"]]
            contributor = ContributorWithType(*a)
            catalog.add_contributor(contributor)
        elif choice == '3':
            while True:
                print("===== Tìm kiếm =====")
                [print(i) for i in ["1. Title", "2. UPC", "3. Subject", "4. Contributor"]]
                type = input("Nhập lựa chọn (1-4): ").strip()
                search_key = input("Nhập từ khóa tìm kiếm: ")
                search_results = catalog.search(search_key,type)
                if search_results != '1':
                    print("Kết quả tìm kiếm:", *[i.__dict__ for i in search_results], sep='\n')
                    break
        elif choice == '4':
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        input("Done")
main_menu()