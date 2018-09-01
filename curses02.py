import curses

screen = curses.initscr()

screen.addstr(0,0,"Hello World")
screen.addstr(1,0,"Hello World", curses.A_BOLD)

screen.refresh()

screen.getch()

curses.endwin()