
with open('./src/temp/input.txt', 'r') as f:
    for line in f:
        print(line.split('-')[1].split('*')[1])
