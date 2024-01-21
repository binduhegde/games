from sudoku import Sudoku
from tkinter import *
from tkinter import messagebox
from choose_level import choose_level
import time
import random

#*#################################
#*------ALL THE CONSTANTS---------#
#*#################################
NUMBER_FONT = ("ariel", 50)
TEXT_FONT = ("apple chancery", 40) # noteworthy "apple chancery" "Herculanum" "kokonor"
BUTTON_BG = "#5f6e64"
BLUE = "#5ce1ff"
GREEN = '#d0f7dc'

# gives us a number between 0 and 1 which we'll pass to the Sudoku class
# this should be called before we create a window because this function will create a window of its own
# so those two should't clash
level = choose_level()

#*#######################################
#*--------CREATING THE WINDOW----------#
#*#######################################
window = Tk()
window.geometry("900x900")
window.title("Sudoku")
window.config(bg=GREEN)
# enters full screen automatically
window.attributes('-fullscreen',True)
dark_theme = False

#*##################################################
#*---------CRCEATING SUDOKU PUZZLE BOARD-----------#
#*##################################################
# creates a sudoku puzzle
puzzle = Sudoku(3).difficulty(level)
# converts it into a list with sublists as rows of the puzzle
puzzle_board = puzzle.board
solved_board = puzzle.solve().board


#*####################################################
#*----------SETTING UP CANVAS AND BG GRID------------#
#*####################################################
white_bg = PhotoImage(file='images/light_grid_resized.png')
black_bg = PhotoImage(file="images/dark_grid_resized.png")
# creating a canvas to display the sudoku grid image
canvas = Canvas(width=900, height=900, highlightthickness=0)
bg_image = canvas.create_image(450, 450, image=white_bg)
canvas.grid(row=0, column=0, rowspan=9, columnspan=9)


#*########################################################
#*----------DISPLAYING THE NUMBERS AND ENTRIES-----------#
#*########################################################
# this stores the list of lists where sub_list[0] is the canvas widget, sub_list[1]
# is the x cordinate and sub_list[2] is the y cordinate. storing x, y to make it easier to
# check the list with new z, y cordinates to see if it matches
notes = []
# entries is a list with all the entry widgets we will create
entries = []
# numbers are the numbers that will be diaplayed on the grid
numbers = []
hints_left = 3

# this takes the puzzle board and displays the numbers in its box and empty spots with entry widget
# so that the user can type in the answer there
def create_entries(board):
    # making it global so that it can be accessed later
    global entries, numbers
    row, column = 0,0
    for i in range(9):
        for j in range(9):
            # if there is no number, we create an entry widget
            if board[i][j] is None:
                new_entry = Entry(width=1, font=NUMBER_FONT, justify=CENTER, fg='purple', highlightthickness=0, relief='ridge')
                new_entry.grid(row=row, column=column)
                entries.append(new_entry)

            else:
                # there is already a number, we display it
                number = Label(text=board[i][j], font=NUMBER_FONT, bg='white', width=1, fg="#35543f")
                number.grid(row=row, column=column)
                numbers.append(number)
            column += 1
        row += 1
        column = 0
create_entries(puzzle_board)

# call this func which will display the answer on the screen
# for testing purposes only. call this after creating the buttons to
# overlap buttons otherwise buttons will overlap this
def display_answer():
    answer_label = Label(text=puzzle.solve(), font=('ariel', 15))
    answer_label.grid(row=0, column=10, rowspan=4)


#*#################################################
#*----------BUTTON COMMAND FUNCTIONS--------------#
#*#################################################
    
#*----------RELATED TO SUBMIT BUTTON--------------#
# gets all the entries made by the user and outputs it in a list
# outputs all values whether it already existed or the user typed in
def get_answer():
    user_answer = []
    ind = 0
    for i in range(9):
        # makes a new list for that row
        user_answer.append([])
        for j in range(9):
            # if there already exists a number in the sudoku Q, that number is appended to the list
            if puzzle_board[i][j] is not None:
                user_answer[i].append(puzzle_board[i][j])
            # this is the place where the user had to fill an entry
            else:
                # trying to see if the user typed in a integer
                try:
                    user_answer[i].append(int(entries[ind].get()))
                # if the user left that entry box empty
                except ValueError:
                    user_answer[i].append('')
                ind += 1    
    return user_answer

# this is called when the user presses the submit_button
def is_correct():
    global timer_on
    # getting the user_ans from the above func
    user_ans = get_answer()
    # correct answer to the puzzle
    correct_ans = solved_board
    # if the user solved it right
    if user_ans == correct_ans:
        # getting hold of the timer before destroying all the widgets
        time_taken = timer_label.cget('text')[2:]
        # clearing all the widgets on the screen
        for widget in window.winfo_children():
            widget.destroy()
        timer_on = False
        # showing this label
        Label(text=f"Congrats! \nYou won 🏆\nTime taken: {time_taken}", font=TEXT_FONT, justify=CENTER, bg="#b7f7ca", relief='ridge', bd=15 ,height=3, padx=20, pady=20).place(relx=0.35, rely=0.35)
    else:
        # this label only displayed for 4000 ms (4 secs)
        result = Label(text="Incorrect answer \nKeep going 🦋", font=TEXT_FONT, bg="#d0f7dc", relief='ridge', bd=15 ,height=3, padx=10)
        result.grid(row=3, column=2, columnspan=5, rowspan=3)
        window.after(4000, result.destroy)


#*---------RELATED TO NOTES BUTTON---------------#
# understand write_note func before this 
# this helps us remove a note. when the user clicks note, 
# all the values in that entry box will be moved to notes. 
# but what if the user wamts to remove a number from notes. 
# here, this takes what's already there in the note box and the new entry. 
#if there is a value in the new box which already exists in the note box, this removes it
def create_text(already, new):
    result = ''
    for char in new:
        if char in already:
            already = already.replace(char, '')
        else:
            result += char
    result += already
    return result

# understand focus_on func before this 
def write_note(x, y, text):
    global notes
    # to see if there already exists a note made by the user previously
    # if so, append to that note
    for item in notes:
        if item[1] == x and item[2] == y:
            # text will be the new note plus the note that was already there
            text = create_text(canvas.itemcget(item[0], "text"), str(text))
            # configuting the note to the new text
            canvas.itemconfig(item[0], text= str(text))
            break
    else:
        # if there was no note before, this creates a new note and appends it to the notes list
        # the reason we're using canvas text instead of tk Label is because with Label, it creates a text box
        # where the backround will be a color. it overlapes with the grid image. It won't look neat
        # canvas' text widget will have a transparent background
        note = canvas.create_text(x, y, text=str(text), font=("ariel", 15))
        notes.append([note, x, y])

# this is called when the user clicks the notes button
def focus_on():
    global entries
    # focused_widget is the entry widget where the user's curser in on
    focused_widget = window.focus_get()
    # iteratin through all the entries and seeing if the curser is on that
    for widget in entries:
        if focused_widget == widget:
            # get the x, y cordinates of the entry widget
            # adding 45 to x and deducting 5 from y to make our note appear on the upper right corner of the grid location
            x, y = widget.winfo_rootx()+45, widget.winfo_rooty()-5
            # this func writes the note in the x, y location
            write_note(x, y, widget.get())
            # clears the entry made in the entry box
            widget.delete(0, 'end')


#*-----------RELATED TO HINT BUTTON--------------#
# related to hint_clicked func
def change_bg():
    correct.config(bg='white')

# reveals the number in a random entry
def hint_clicked():
    global entries, puzzle_board, correct, numbers, hints_left
    # means there is no entry box. it's when the user used hint till every entry was done
    if len(entries) == 0:
        return
    if hints_left == 0:
        result = Label(text="Sorry! \nNo more hints left 😞", font=TEXT_FONT, bg="#d0f7dc", relief='ridge', bd=15 ,height=3, padx=20)
        result.grid(row=3, column=2, columnspan=5, rowspan=3)
        window.after(3000, result.destroy)
        return
    # taking a random entry widget
    entry_widget = random.choice(entries)
    # saving the grid location before destrying the entry widget
    location_row = entry_widget.grid_info()['row']
    location_column = entry_widget.grid_info()['column']
    # removing the widget from entries list because we are going to destroy it
    entries.remove(entry_widget)
    entry_widget.destroy()
    
    # this is the number to be displayed in the grid location 
    # location_row and location_column also happen to be the address 
    # of the solved board's number in the grid location
    number_to_go = solved_board[location_row][location_column]
    correct = Label(text=number_to_go, font=NUMBER_FONT, bg='#5ff590', width=1, fg="#35543f")
    correct.grid(row=location_row, column=location_column)
    # we set the bg to green to grab the attention of the user to let them know where 
    # we are diaplaying the hint. changing it back to white after 0.8 secs
    window.after(800, change_bg)
    # also adding this to puzzle board so that it will be there while checking the answer
    puzzle_board[location_row][location_column] = number_to_go
    numbers.append(correct)
    hints_left -= 1 
    result = Label(text=f"{hints_left} Hints left 💡", font=TEXT_FONT, bg="#d0f7dc", relief='ridge', bd=15 ,height=2, padx=10)
    result.grid(row=3, column=2, columnspan=5, rowspan=3)
    window.after(2000, result.destroy)


#*--------RELATED TO VALIDATE BUTTON------------#
def validate_clicked():
    user_ans = get_answer()
    # once we detect a mistake, we set this to True
    something_wrong = False
    # going through every box
    for i in range(9):
        for j in range(9):
            # if user ans and correct ans are not matching AND that box is not empty
            if user_ans[i][j] != solved_board[i][j] and user_ans[i][j] != '':
                something_wrong = True
                break
    text = "Something is wrong 🧐" if something_wrong else "Everything looks okay 🤓"
    result = Label(text=text, font=TEXT_FONT, bg="#d0f7dc", relief='ridge', bd=15 ,height=2, width=23)
    result.grid(row=3, column=1, rowspan=3, columnspan=7)
    window.after(2000, result.destroy)


#*--------RELATED TO RESTART BUTTON------------#
def restart_clicked():
    global entries, hints_left
    restart = messagebox.askyesno(title="Confirmation", message="Are you sure you want to restart this game?")
    if restart:
        for entry in entries:
            entry.delete(0, 'end')
        for note in notes:
            canvas.itemconfig(note[0], text='')
        hints_left = 3


#*-------RELATED TO INSTRUCTIONS BUTTON---------#
def instructions_clicked():
    message = "1. Select an empty square \n2.Then type in the number to fill the square\n3. Click notes to add the typed values to notes\n4. To erase a certain value from notes, type in that value and click notes\n5.If you're unsure of your answers, click validate to know\n6. You only get 3 hints per game\n7. Click submit when you are done"
    messagebox.showinfo(title="Instructions", message=message)


#*--------RELATED TO THEME BUTTON--------------#
# if the theme is white, it changes to dark and vice versa
def change_theme():
    global dark_theme, numbers, entries, notes, timer_label
    # if dark theme is already on, changes everything to white
    if dark_theme:
        # changing_dark theme to False
        dark_theme = False
        canvas_bg_image = white_bg
        number_bg, number_fg = 'white', 'black'
        entry_bg, entry_fg = 'white', 'purple'
        note_fill_color = 'black'
        timer_bg, timer_fg = GREEN, 'black'
        window_bg = GREEN
    else:
        # changing_dark theme to True
        dark_theme = True
        canvas_bg_image = black_bg
        number_bg, number_fg = 'black', BLUE
        entry_bg, entry_fg = 'black', 'yellow'
        note_fill_color = 'white'
        timer_bg, timer_fg = 'black', 'white'
        window_bg = 'black'

    # changing the background grid image
    canvas.itemconfig(bg_image, image=canvas_bg_image)
    # hanging the numbers in the Q
    for number in numbers:
        number.config(bg=number_bg, fg=number_fg)
    # changing user's entries
    for entry in entries:
        entry.config(bg=entry_bg, fg=entry_fg)
    # changing the note color they might have made
    for note in notes:
        canvas.itemconfig(note[0], fill=note_fill_color)
    # changin the timer colors
    timer_label.config(bg=timer_bg, fg=timer_fg)
    # changing window bg
    window.config(bg=window_bg)


#*---------RELATED TO QUIT BUTTON--------------#
def quit_clicked():
    global entries, buttons, notes, timer_on
    # asks popup conformation
    do_quit = messagebox.askyesno(title="Confirmation", message="Are you sure you want to quit this game?")
    # if user said no, the func ends, the user can resume the game
    if not do_quit:
        return
    # asks if the user wants to see the ans
    show_ans = messagebox.askyesno(title="Confirmation", message="Do you want to see the answer to this game?")
    # if the user wants to see the answers
    if show_ans:
        # destroying all the entries so that we can write the ans there
        for entry in entries:
            entry.destroy()
        # creating the solved board numbers
        create_entries(solved_board)
        # destrying every button so that the user can't submit or anything
        for button in buttons_list:
             button.destroy()
        # shows an error if we destroy notes hence changing its text to en empty string
        for note in notes:
            canvas.itemconfig(note[0], text='')
        # destroying the time_label
        # also changing timer on to False so that update_timer() doesn't run forever
        timer_label.destroy()
        timer_on = False
    else:
        window.destroy()


#*##############################################
#*---------------ALL THE BUTTONS---------------#
#*##############################################
button_width = 14

submit_button = Button(text='Submit 📥', font=TEXT_FONT, command=is_correct, width=button_width, highlightbackground=BUTTON_BG)
submit_button.place(x=1000, y=650)

note_button = Button(text="Note 📝", font=TEXT_FONT, command=focus_on, width=button_width, highlightbackground=BUTTON_BG, height=1)
note_button.place(x= 1000, y=560)

hint_button = Button(text="Hint 💡", font=TEXT_FONT, width=button_width, command=hint_clicked, highlightbackground=BUTTON_BG)
hint_button.place(x=1000, y=470)

validate_button = Button(text="Validate ✔️", font=TEXT_FONT, width=button_width, command=validate_clicked, highlightbackground=BUTTON_BG)
validate_button.place(x=1000, y=380)

restart_button = Button(text="Restart ↻", font=TEXT_FONT, width=button_width, command=restart_clicked, highlightbackground=BUTTON_BG)
restart_button.place(x=1000, y=290)

instructions_button = Button(text="Instrustions 📜", font=TEXT_FONT, command=instructions_clicked, width=button_width, highlightbackground=BUTTON_BG)
instructions_button.place(x=1000, y=200)

theme_button = Button(text="Theme 🎨", font=TEXT_FONT, width=button_width, highlightbackground=BUTTON_BG, command=change_theme)
theme_button.place(x=1000, y=110)

quit_button = Button(text="I give up 🚫", font=TEXT_FONT, width=button_width, highlightbackground=BUTTON_BG, command=quit_clicked)
quit_button.place(x=1000, y=740)

# saving all the buttons in this list so that we can destroy it by iterating through it when the user hit the quit button
buttons_list = [submit_button, note_button, hint_button, validate_button, restart_button, instructions_button, theme_button, quit_button]

#*###################################################
#*---------------TIMER FUNCTIONALITY----------------#
#*###################################################
timer_on = True
def update_timer(seconds):
    if not timer_on:
        return
    timer_label.configure(text=f"🕰 {format_time(seconds)}")
    seconds +=1
    # after 1000 mm (1 sec), the fun calls itself. hence it updates the timer_label every sec
    window.after(1000, update_timer, seconds)
# takes number of secs as the input and outputs in hh:mm:ss format
def format_time(secs):
    return time.strftime('%H:%M:%S', time.gmtime(secs))
seconds = 0 # start with 0th sec
# creating the timer label so that it can ge configured later
timer_label = Label(font=("ariel", 30), bg="#d0f7dc")
# got the x, y cordinate through trial and error
timer_label.place(x=1230, y=40)
update_timer(seconds)



#display_answer()
window.mainloop()