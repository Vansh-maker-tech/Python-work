import curses
from curses import wrapper

def main(stdscr):
	stdscr.clear()
	stdscr.addstr(5,10,"Hello World")
	#stdscr.refresh()
	stdscr.getch()
	
wrapper(main)
