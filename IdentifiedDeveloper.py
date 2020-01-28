import os

path_name = input("julieann11202@icloud.com
Please enter the path of the file you want to unblock: ")

os.system("xattr -d com.apple.quarantine \"" + str(path_name) + "\"")
