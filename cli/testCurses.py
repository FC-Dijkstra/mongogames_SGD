from curses import wrapper
import curses


def main(screen):

    screen.clear()

    screen.addstr(0, 0, "This string gets printed at position (0, 0)")

    # Python 3 required for unicode
    screen.addstr(3, 1, "Try Russian text: Привет")
    screen.addstr(4, 4, "X")
    screen.addch(5, 5, "Y")

    screen.refresh()
    screen.getkey()


wrapper(main)
