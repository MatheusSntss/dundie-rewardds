def load(filepath):
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError:
        print("Filepath is invalid")

