def read():
    cleaned_data = []
    file = open('data.txt', 'r')
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        line = line.replace("'", '"')
        cleaned_data.append(line)
    return cleaned_data


