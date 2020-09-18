if __name__ == '__main__':

    file_in = open("./hangman_play.py")

    linee = 0
    for line in file_in:
        if line.strip() != "":
            linee += 1

    file_in = open("./start.py")

    for line in file_in:
        if line.strip() != "":
            linee += 1

    print(linee)
