import os
# Delete a File
# os.remove("myfile.txt")

#Check if file exists, then delete it:
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("Deleted myfile.txt")
else:
    print("The file  does not exist !")


## Delete Folder
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
    print("Deleted folder 'myfolder'")
else:
    print("The folder  does not exist !")