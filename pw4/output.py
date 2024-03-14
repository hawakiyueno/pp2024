# output.py
import curses

def initialize_curses():
    curses.curs_set(0)  # Hide the cursor

def clear_screen(stdscr):
    stdscr.clear()

def show_message(stdscr, message, row, col, attributes=curses.A_NORMAL):
    stdscr.addstr(row, col, message, attributes)
    stdscr.refresh()

def get_choice(stdscr):
    stdscr.addstr(11, 5, "Enter your choice: ")
    stdscr.refresh()
    choice = stdscr.getch() - ord('0')
    return choice
