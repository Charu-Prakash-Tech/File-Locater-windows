import os

name = input("Enter the name of the file: ")  # No need to explicitly convert to str
path = "C:\\"  # Root search path

def locate(name, path):
    found = []
    
    for root, dirs, files in os.walk(path):
        if name in files:
            found.append(os.path.join(root, name))

    if found:
        print("\n🔍 Found Files:")
        for file in found:
            print(file)
    else:
        print("❌ File Not Found")

locate(name, path)
