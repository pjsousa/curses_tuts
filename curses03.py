import curses

screen = curses.initscr()
dims = screen.getmaxyx()
screen.addstr(dims[0]//2, dims[1]//2 - 5,"Hello World")
screen.addstr(1,0,"Hello World", curses.A_BOLD)

screen.refresh()

screen.getch()

curses.endwin()