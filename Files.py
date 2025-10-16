

names_list=("Sara\n"
            "Rivka\n"
            "Rachel\n"
            "Lea\n"
            "Avraham\n"
            "Yzchak\n"
            "Yaakov\n")

file_name = input("write file name ")

# writing to file
with open("C:/Users/user1/Desktop/PythonProject/" + file_name+".txt", "a", encoding="utf-8") as f:
    f.write(str(names_list))
# reading a file
with open("C:/Users/user1/Desktop/PythonProject/" + file_name + ".txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for l in range(1,len(lines),2):
            print(lines[l])



