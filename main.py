file = open("number.txt", "r")

try:
    content = file.read().strip()
    if not all(map(str.isdigit, content.split())):
        raise ValueError("The file contains non-numeric values")
    print(content)
except FileNotFoundError:
    print("The file does not exist")
except PermissionError:
    print("The program does not have permission to access the file")
except ValueError as e:
    print(e)
finally:
    file.close()
    print("Completion of program execution")
