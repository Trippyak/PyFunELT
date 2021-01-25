import csv

# open_csv to open file and return a string
# functionname(file variable: type) -> return type
# pros: assists in reading files faster 

def open_csv(filepath: string) -> None: 
    with open(filepath) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(', '.join(row))
