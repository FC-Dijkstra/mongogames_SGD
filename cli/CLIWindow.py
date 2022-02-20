import curses

from cli.CLIElement import CLIElement


class CLIWindow(CLIElement):
    def __init__(self, width, height, x, y):
        super(x, y)
        self.width = width -1
        self.height = height -1
        self.win = curses.newwin(height, width, y, x)

    def draw(self):
        horizontal = "+"
        for i in range (self.width -2):
            horizontal += "-"
        horizontal += "+"

        #set cursor X Y
        self.win.addstr(self.y, self.x, horizontal);
        self.win.addstr(self.y + self.height, self.x, horizontal)
