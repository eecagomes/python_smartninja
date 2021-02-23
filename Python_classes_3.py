with open("ninja.txt.","r") as ninja_file:
    content=ninja_file.read()## python will read the txt file
    print(content)

    content_line=ninja_file.read().splitlines() ## all lines

    for line in content_line:
        print(line)


##write

with open("ninja.txt","w") as ninja_file:
    ninja_file.write("Hello World")



