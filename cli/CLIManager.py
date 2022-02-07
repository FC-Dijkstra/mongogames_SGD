import curses

class CLIManager:
    def __init__(self, screen = curses.initscr()):
        screen.clear()
        screen.keypad(True)
        curses.noecho()
        curses.cbreak()
        self.screen = screen
        self.stack = []
        self.width, self.height = screen.getmaxyx()
        self.win = curses.newwin(self.width, self.height, 0, 0)

    def addElement(self, element):
        self.stack.append(element)

    def interrupt(self, element):
        self.addElement(element)
        self.update()
        element.handleInput()
        self.deleteTop()

    def deleteTop(self):
        self.stack.pop().clear()

    def top(self):
        index = len(self.stack)
        return self.stack[index]

    def loop(self):
        while(True):
            self.update()
            self.top().handleInput()
            self.screen.update()
            self.screen.getkey()

    def update(self):
        for element in self.stack:
            element.clear()
            element.draw()
            element.update()

    def exit(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
