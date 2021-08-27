import random

def filewrite(file_name):
    with open(file_name, 'w') as file_data:
        for i in range(1, 1001):
            if i % 10 == 0:
                line = str(random.randint(1, 9)) + "\n"
            else:
                line = str(random.randint(1, 9)) + ' '
            file_data.write(line)
            print(line)
    return line


print(filewrite("Random.txt"))