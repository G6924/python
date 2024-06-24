
#+ String Upper :

print("\n" + "( String Upper )".center(100, "-"))
str = "hello"
print("+/ str = " + str)
print("Notes : Chuyển đổi tất cả các ký tự trong chuỗi thành chữ in hoa.")
print("USE: str.upper()")
print("Result -> " +str.upper())



#+ String lower :

print("\n" + "( String Lower )".center(100, "-"))
str = "HELLO"
print("+/ str = " + str)
print("Notes : Chuyển đổi tất cả các ký tự trong chuỗi thành chữ thuong.")
print("USE: str.lower()")
print("Result -> " +str.lower())


#+ String Capitalize :

print("\n" + "( String Capitalize )".center(100, "-"))
str = "hello"
print("+/ str = " + str)
print("Notes : Chuyển đổi ký tự đầu tiên của chuỗi thành chữ in hoa và các ký tự còn lại thành chữ thường.")
print("USE: str.capitalize()")
print("Result -> " +str.capitalize())

#+ String Title :

print("\n" + "( String Title )".center(100, "-"))
str = "hello world"
print("+/ str = " + str)
print("Notes : Chuyển đổi ký tự đầu tiên của mỗi từ trong chuỗi thành chữ in hoa.")
print("USE: str.title()")
print("Result -> " +str.title())

#+ String Strip :

print("\n" + "( String Strip )".center(100, "-"))
str = "  hello world  "
print("+/ str = " + str)
print("Notes : Loại bỏ các ký tự trắng ở đầu và cuối chuỗi.")
print("USE: str.strip()")
print("Result -> " +str.strip())


#+ String lstrip :

print("\n" + "( String lstrip )".center(100, "-"))
str = "  hello world  "
print("+/ str = " + str)
print("Notes :  Loại bỏ các ký tự trắng ở đầu chuỗi.")
print("USE: str.lstrip()")
print("Result -> " +str.lstrip())


#+ String rstrip :

print("\n" + "( String rstrip )".center(100, "-"))
str = "  hello world  "
print("+/ str = " + str)
print("Notes :  Loại bỏ các ký tự trắng ở cuoi chuỗi.")
print("USE: str.rstrip()")
print("Result -> " +str.rstrip())



#+ String split :

print("\n" + "( String split )".center(100, "-"))
str = "  hello , world  "
print("+/ str = " + str)
print("Notes :  Tách chuỗi thành danh sách các từ con bằng cách sử dụng ký tự phân cách separator.")
print("USE: str.split(',')")
temp = str.split(",")
print("Result -> " , temp)


#+ String Join :

print("\n" + "( Sring join )".center(100, "-"))
arr = ["hello", "world"]
print("+/ arr = " + "['hello' , 'world']")
print("Notes :   Ghép các phần tử của một iterable thành một chuỗi, ngăn cách bởi chuỗi ban đầu.")
print("USE: ', '.join(arr)")
temp = ", ".join(arr)
print("Result -> " , temp)

#+ String find :

print("\n" + "( String find )".center(100, "-"))
str = "hello world  "
print("+/ str = " + str)
print("Notes :   Tìm vị trí đầu tiên của chuỗi con sub trong chuỗi ban đầu. Trả về -1 nếu không tìm thấy.")
print("USE: str.find('he')")
print("Result -> " + f"{str.find('l')}")


#+ String Replace :

print("\n" + "( String Replace )".center(100, "-"))
str = "hello world  "
print("+/ str = " + str)
print("Notes :   Thay thế tất cả các lần xuất hiện của chuỗi con old bằng chuỗi new.")
print("USE: str.replace('he', 'new')")
print("Result -> " + f"{str.replace('he', 'new')}")

#+ String Count :

print("\n" + "( String Count )".center(100, "-"))
str = "hello world  "
print("+/ str = " + str)
print("Notes :  Đếm số lần xuất hiện của chuỗi con sub trong chuỗi ban đầu.")
print("USE: str.count('l')")
print("Result -> " + f"{str.count('l')}")


#+ String End sWith :

print("\n" + "( String Endswith )".center(100, "-"))
str = "hello world"
print("+/ str = " + str)
print("Notes : Kiểm tra xem chuỗi có kết thúc bằng chuỗi con suffix không..")
print("USE: str.endswith('rld')")
print("Result -> " + f"{str.endswith('rld')}")


#+ String IsDigit :

print("\n" + "( String IsDigit )".center(100, "-"))
str = "123123"
print("+/ str = " + str)
print("Notes : Kiểm tra xem chuỗi chỉ chứa các ký tự số không.")
print("USE: str.isdigit()")
print("Result -> " + f"{str.isdigit()}")