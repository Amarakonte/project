import getch

char = str()
while str(char) != "b\'\\x1b\'":
    char = getch.getch()
    print(char)