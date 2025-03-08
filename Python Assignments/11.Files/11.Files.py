#1.Reading a text file.

def read_file(file_path):
    try:
        with open(file_path) as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
read_file("text.txt")

#2.Writing text to text file using InputStream.

def wtf(file_path):
    try:
        text = input("Enter text to write to file: ")
        with open(file_path, 'w') as file:
            file.write(text)
        print("Text written to file successfully.")
    except Exception as e:
        print("An error occurred:", e)
wtf("text1.txt")


#3.Reading a file stream.

def rfs(fp):
    try:
        with open(fp, 'r') as file:
            for f in file:
                print(f, end='')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
rfs("text1.txt")


#4.Reading a file stream supporting random access.

def rfar(fp, p):
    try:
        with open(fp, 'r') as file:
            file.seek(p)
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
rfar("text1.txt",10)


#5.Reading a file stream using a particular index.

def reading_index(fp, p, l):
    try:
        with open(fp, 'r') as file:
            file.seek(p)
            print(file.read(l))
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
reading_index("text1.txt", 10, 20)


#6.checking whether a file has permissions.

import os
def cp(fp):
    print("Read access:", os.access(fp, os.R_OK))
    print("Write access:", os.access(fp, os.W_OK))
cp("text.txt")


































