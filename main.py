file = open("number.txt", "r")

try:
    print(file.read(25))
except FileNotFoundError:
    print("The file does not exist")
except PermissionError:
    print("The program does not have permission to access the file")
except ValueError:
    print("The file contains non-numeric values")
finally:
    file.close()
    print("Completion of program execution")
