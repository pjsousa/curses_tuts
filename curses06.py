import curses
import time

MESSAGE = "Hello World!"

screen = curses.initscr()
curses.noecho()
dims = screen.getmaxyx()

q = -1
x, y = 0,0
vertical = 1
horizontal = 1
while q != ord('q'):
	screen.clear()
	screen.addstr(y,x,MESSAGE)
	screen.refresh()
	
	q = screen.getch()

	if q == ord("w") and y > 0:
		y -= 1
	elif q == ord("s") and y < dims[0] - 1:
		y += 1
	elif q == ord("a") and x > 0:
		x -= 1
	elif q == ord("d") and x < dims[1] - len(MESSAGE) - 1:
		x += 1
	else:
		pass


	#time.sleep(0.1)

screen.refresh()
screen.getch()
curses.endwin()
