import os
from string import digits

list_files = os.listdir("C:\\Users\\test\\Downloads\\prank\\prank")
#print(list_files)
os.chdir("C:\\Users\\test\\Downloads\\prank\\prank")
#repeat the following steps for all the files in prank dir
for file in list_files:
    #get oldname of file
    old_name = file
    print old_name
    #newname of file = oldname-numbers
    new_name = old_name.lstrip(digits)
    print new_name
    #rename the file(oldname,newname)
    os.rename(old_name,new_name)