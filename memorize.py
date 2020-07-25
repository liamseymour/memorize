import sys
import curses

def main(stdscr):
	# Setup curses
	stdscr.clear()
	curses.use_default_colors()

	# Get words from file
	fp = sys.argv[1]
	with open(fp, "r") as f:

		# Split words so as to preserve trailing whitespace
		word = ""
		words = []
		wasWhiteSpace = False
		for char in f.read():
			if char in " \n\t":
				word += char
				wasWhiteSpace = True
			elif wasWhiteSpace:
				words.append(word)
				word = char
				wasWhiteSpace = False
			else:
				word += char
		words.append(word)

	# Turn on no delay
	stdscr.nodelay(True)

	word = 0
	while True:
		try:
			key = stdscr.getkey()
			if key == "w" and word < len(words):
				# Print and advance a word
				# Quick anti word wrap
				if len(words[word]) + stdscr.getyx()[1] > curses.COLS:
					stdscr.addstr("\n")
				stdscr.addstr(words[word])
				word += 1
			elif key == "q":
				# Quit the program
				break
			elif key == "r":
				stdscr.clear()
				word = 0
				
		except Exception as e:
			pass

if __name__ == "__main__":

	""" Start curses and begin game """

	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

	curses.wrapper(main)

	""" Exit Program """

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
