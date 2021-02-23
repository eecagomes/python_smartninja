import os  ##check if file exists

filename = "data.csv"
file_lines = ["Name,Age,Gender", "Tina,23,female", "Jakob,35,male", "Barbara,44,female"]

if not os.path.exists(filename):  ##if file doesn't exist
    with open(filename, "w") as csvfile:
        for line in file_lines:  ##go for each line in file_lines vector
            csvfile.write(line + "\n")  ## write every line and do the line break with '\n'
    csvfile.close()

with open(filename, "r") as csvfile:
    all_lines = csvfile.readlines()
    n_all_lines = len(all_lines)  ##dim of the list of all the lines of the file

    for line in all_lines[1:n_all_lines]:  ## starting at position 1 since the 0 pos is the header info
        content_line = line.strip()  ## remove the '\n' of the vectors
        content_line = content_line.split(",")  ## spliting by commas the content in 3 positions
        n_content_line = len(content_line)  ## dim of the content_line vector
        sentence = ""  ## initiating variable

        for i in range(n_content_line):## looping through the content_line vector and using ifs to create the sentences

            if i == 0:
                sentence = str(content_line[i])
            if i == 1:
                sentence = sentence + " is " + str(content_line[i]) + " years old"
            if i == 2:
                sentence = sentence + " and " + str(content_line[i])
                print(sentence)
