import curses
from time import sleep
import random

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

BODY_CHAR = "X"
BODY_INIT_SIZE = 10
GROW_LEN = 5
FOOD_CHAR = "@"
MESSAGE1 = "GAME OVER"
MESSAGE2 = "YOU GOT %s POINTS"
MESSAGE3 = "[press <space> to play again]"
MESSAGE4 = "[press <enter> to exit]"

SPEEDS = {
	"EASY": 0.1,
	"MEDIUM": 0.06,
	"HARD": 0.04
}

ACCELERATION = True

DIFICULTY = "MEDIUM"

def menu(screen):
	curses.noecho()
	curses.curs_set(False)
	screen.keypad(True)

	screen.nodelay(0)

	dims = screen.getmaxyx()
	
	selection = -1
	option = 0
	while selection < 0:
		graphics = [0] * 5
		graphics[option] = curses.A_REVERSE
		screen.addstr(0,dims[1]//2 - 3, "Snake")
		screen.addstr(dims[0]//2-2, dims[1]//2-2, "Play", graphics[0])
		screen.addstr(dims[0]//2-1, dims[1]//2-6, "Instructions", graphics[1])
		screen.addstr(dims[0]//2, dims[1]//2-6, "Game Options", graphics[2])
		screen.addstr(dims[0]//2+1, dims[1]//2-5, "High Scores", graphics[3])
		screen.addstr(dims[0]//2+2, dims[1]//2-2, "Exit", graphics[4])

		screen.refresh()
		action = screen.getch()
		if action == curses.KEY_UP:
			option = (option - 1) % 5
		elif action == curses.KEY_DOWN:
			option = (option + 1) % 5
		elif action == ord("\n"):
			selection = option

	if selection == 0:
		game(screen)
	if selection == 4:
		return



def game(screen):
	curses.noecho()
	curses.curs_set(False)
	screen.keypad(True)
	screen.clear()
	screen.nodelay(1)

	head = [1,1]
	body = [head[:]] * BODY_INIT_SIZE

	screen.border()

	direction = RIGHT
	gameover = False
	deadcell = body[-1][:]
	dims = screen.getmaxyx()

	foodmade = False
	food = []


	while not gameover:
		while not foodmade:
			y,x = random.randrange(1, dims[0]-1), random.randrange(1, dims[1]-1)

			if screen.inch(y,x) == ord(' '):
				foodmade = True
				screen.addch(y,x,FOOD_CHAR)

		if deadcell not in body:
			screen.addch(deadcell[0], deadcell[1], " ")

		screen.addch(head[0],head[1], BODY_CHAR)
		key = screen.getch()

		if key == curses.KEY_UP and direction != DOWN:
			direction = UP
		elif key == curses.KEY_DOWN and direction != UP:
			direction = DOWN
		elif key == curses.KEY_RIGHT and direction != LEFT:
			direction = RIGHT
		elif key == curses.KEY_LEFT and direction != RIGHT:
			direction = LEFT

		if direction == RIGHT:
			head[1] += 1
		elif direction == LEFT:
			head[1] -= 1
		elif direction == DOWN:
			head[0] += 1
		elif direction == UP:
			head[0] -= 1

		deadcell = body[-1][:]
		body = [head[:]] + body[:-1]

		if key == 27:
			break

		char_below_head = screen.inch(*head)
		if char_below_head != ord(' '):
			if char_below_head == ord('@'):
				foodmade = False
				screen.addch(y,x, " ")
				for x in range(GROW_LEN):
					body.append(body[-1][:])
			else:
				gameover = True
		#screen.move(dims[0] - 1, dims[1] - 1)
		screen.refresh()

		if not ACCELERATION:
			sleep(SPEEDS[DIFICULTY])
		else:
			sleep(15.0 * SPEEDS[DIFICULTY] / len(body))

	screen.clear()
	screen.nodelay(0)

	endscore = MESSAGE2 % (int((len(body) - BODY_INIT_SIZE) / GROW_LEN))

	screen.addstr(dims[0]//2 - 2, dims[1]//2 - len(MESSAGE1)//2, MESSAGE1)
	screen.addstr(dims[0]//2 - 1, dims[1]//2 - len(endscore)//2, endscore)
	screen.addstr(dims[0]//2 - 0, dims[1]//2 - len(MESSAGE3)//2, MESSAGE3)
	screen.addstr(dims[0]//2 + 1, dims[1]//2 - len(MESSAGE4)//2, MESSAGE4)
	
	while True:
		key = screen.getch()

		if key == ord(' '):
			screen.clear()
			game(screen)
		if key == 10:
			break



		

curses.wrapper(menu)