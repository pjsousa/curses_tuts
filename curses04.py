import curses
import time

screen = curses.initscr()
dims = screen.getmaxyx()

for i in range(dims[1]-12):
	screen.clear()
	screen.addstr(dims[0]//2, i,"Hello World")
	screen.refresh()
	time.sleep(0.001)

screen.refresh()
screen.getch()
curses.endwin()
