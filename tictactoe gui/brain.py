import random

# CLASS GAMEBRAIN'S NEXT MOVE():
# return a dictionary:
# {board: [[]], is_complete: true/false, winner: 0/1/2, line:[0, 1, 2]}

# --------------BOARD------------------#
# board is the current state of the board

# --------------IS_COMPLETE----------------#
# True is the game is over (one of the players won or it's a tie), False if the game is still on

# --------------WINNER-------------------#
# winner - 0 => tie
# winner - 1 => user X
# winner - 2 => computer O

# ------------LINE----------------#
# a list of indices whose values are all same i.e., either it's ('X','X','X') or ('O','O','O'). which means a player won

# Note: what's there in winner and line doesn't matter as long as is_complete is false
# so we start with random values for winner and line


class GameBrain:
    def __init__(self, level: int) -> None:
        # first creates an empty board with all values None
        self.board = [None for _ in range(9)]
        # stores the user's string
        self.user = 'X'
        # stored the comp's string
        self.computer = 'O'
        # stored the level number
        # this level can be easy, medium, hard or play against a friend
        # 1: easy, 2: medium, 3:hard and 0: play against a friend
        self.level = level
        self.winning_lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

    # returns the indices of the cells where the value is None
    def get_empty_spots(self) -> list:
        return [i for i in range(9) if self.board[i] == None]

    # this is called when the user makes a move.
    # the user's move is already updated to the board by the main.py
    # this just thinks what is the next step.
    # NOTE: This  func DOESN'T update the board with the comp's move
    def next_move(self) -> dict:
        # go to the top of the file to understand this
        result = {'board': self.board, 'is_complete': False,
                  'winner': 0, 'line': [0, 1, 2]}
        # seeing if X won (prev player)
        x_won = self.check_winner(self.user)
        # if X won, we update the result dict
        if x_won[0]:
            result['is_complete'] = True
            result['winner'] = 1
            result['line'] = x_won[1]
        # if it's a tie, we only need to change is_complete because
        # we already started with winner = 0 which means it's a tie
        elif self.check_tie():
            result['is_complete'] = True
        # we aren't checking if the computer won because we'll do it after the computer makes a move

        else:  # means computer has to make a move according to the difficulty level
            self.make_move()

        # after the computer made its move, we're checking if the comp won
        o_won = self.check_winner(self.computer)
        # updateting the dict if the comp won
        if o_won[0]:
            result['is_complete'] = True
            result['winner'] = 2
            result['line'] = o_won[1]

        return result

    # makes a move according to the difficulty level
    def make_move(self) -> None:
        # what difficulty level means
        # 1: easy, 2: medium, 3:hard and 0: play against a friend
        if self.level == 1:
            self.easy_move()
        elif self.level == 2:
            self.medium_move()
        elif self.level == 3:
            self.hard_move()
        # we don't have to do this else part. just doing to keep it organized and readable
        else:
            self.against_friend()

    # *##########################################################
    # *-------------RELATED TO EASY LEVEL-----------------------#
    # *##########################################################
    # updates the board with a value in a random empty cell
    def easy_move(self) -> None:
        choice = random.choice(self.get_empty_spots())
        self.board[choice] = self.computer

    # *##########################################################
    # *-------------RELATED TO MEDIUM LEVEL---------------------#
    # *##########################################################

    def medium_move(self) -> None:
        # seeing is the compter or the user is one step away from winning
        is_comp_one_step_away = self.one_steps_away(self.computer)
        is_user_one_step_away = self.one_steps_away(self.user)
        # if the comp is one step away from winning, we mark the spot and win
        if is_comp_one_step_away[0]:
            self.board[is_comp_one_step_away[1]] = self.computer
        # if the user is one step away from winning, we block them
        elif is_user_one_step_away[0]:
            self.board[is_user_one_step_away[1]] = self.computer
        # if neither are one step away, we mark a spot in which line there already exists a computer mark
        # we get 1 step closer to winning, if the user doesn't block us, we'll win in the next step
        else:
            self.two_steps_away()

        # NOTE: the funciton one_step_away returns a tuple, it doesn't update the board
            # but the function two_steps away just updates the board, doesn't return anything

    # returns a tuple. first value is a bool saying whether or not the said played is one step away from winning
    # if so, sencond value is the index of the call where we need to mark our sign ('O') whether to win pr block them from winning
    # so the tuple's second value doesn't matter as long as the first value is not True
    def one_steps_away(self, player: str) -> tuple:
        # iterating through all the lines
        for line in self.winning_lines:
            # count is the count number of the player's sign occurence at each line.
            # resets to 0 after each line
            count = 0
            # number of None in a line
            none_count = 0
            # index of the None value in a line so that we can return it and mark it with the computer's sign
            none_ind = 0
            for ind in line:
                if self.board[ind] == player:
                    count += 1
                elif self.board[ind] is None:
                    none_count += 1
                    none_ind = ind
            # to be one step away from winning, a line has to have 2 values of the player and one None so that we can mark out value there
            if count == 2 and none_count == 1:
                return True, none_ind
        return False, -1

    # if none of the players is one step away from winning, computer marks a cell in a line where it has the chance of winning
    # making the no of its occurences 2 which makes it one step away from winning if the other player doen't block us
    # logic same as the one_step_away func but this directly updates a board instead of returning the index number
    def two_steps_away(self) -> None:
        for line in self.winning_lines:
            count = 0
            none_count = 0
            none_ind = []
            for ind in line:
                if self.board[ind] == self.computer:
                    count += 1
                elif self.board[ind] is None:
                    none_count += 1
                    none_ind.append(ind)
            if count == 1 and none_count == 2:
                choice = random.choice(none_ind)
                self.board[choice] = self.computer
                # returning none just to stop the func from running
                return None
        # if the func is still running, it means this is the first step the computer has to make hance there are no two-steps-away spots
        # so we mark a random spot. that's why we're calling easy_move which updates the board with a random value
        self.easy_move()

    # *##########################################################
    # *-------------RELATED TO HARD LEVEL-----------------------#
    # *##########################################################
    # this is where we impliment and call the minimax algorithm

    def hard_move(self) -> None:
        # best score is -infinity initially
        best_score = float('-inf')
        best_move = 0
        # we're iterating through every empty spot and changing that None value to the computer's sign and see how it goes
        for pos in self.get_empty_spots():
            # temporarily assigning this position with the comp's sign to all the minimaz func
            self.board[pos] = self.computer
            # calling minimax function. False because we don't want to maximise the score because the maximizing already happened in the prev line of code
            score = self.minimax(False)
            # again resetting that value to None
            self.board[pos] = None
            # score is the outcome we'd get if we made that move
            if score > best_score:
                best_score = score
                best_move = pos
        # actually update the board with the best move
        self.board[best_move] = self.computer

    def minimax(self, is_maximizing: bool) -> int:
        # if we already won, returns 1 which is the score
        if self.check_winner(self.computer)[0]:
            return 1
        # if the user already won, returns -1 which is the score
        elif self.check_winner(self.user)[0]:
            return -1
        # if it's a tie, returns 0 which is the score
        elif self.check_tie():
            return 0

        # if mazining was True when we called minimax, goes through the same process but calls the minimax function with False as the parameter
        if is_maximizing:
            best_score = float('-inf')
            for pos in self.get_empty_spots():
                self.board[pos] = self.computer
                score = self.minimax(False)
                self.board[pos] = None

                if score > best_score:
                    best_score = score
            return best_score
        # if mazining was False when we called minimax, goes through the same process but calls the minimax function with True as the parameter
        else:
            best_score = float('inf')
            for pos in self.get_empty_spots():
                self.board[pos] = self.user
                score = self.minimax(True)
                self.board[pos] = None

                if score < best_score:
                    best_score = score
            return best_score

    # *##########################################################
    # *--------RELATED TO PLAYING WITH A FRIEND-----------------#
    # *##########################################################
    # doesn't do anything because both the players are users. we have nothing to do
    # but we check if this other friend won in the next move

    def against_friend(self) -> None:
        pass

    # *##########################################################
    # *-----------RELATED TO CHECKING WINNERS/TIES--------------#
    # *##########################################################

    # check if the player (X or O) won and returns a tuple. first value is a bool about whether or not the player won
    # 2nd value is the list of indices of the winning line. doesn't matter what is if the first value is False
    def check_winner(self, player: str) -> tuple:
        for line in self.winning_lines:
            for ind in line:
                if self.board[ind] != player:
                    break
            else:
                return True, line
        return False, line

    # if there is any empty spot in the board, returns false else true
    def check_tie(self):
        tie = True if len(self.get_empty_spots()) == 0 else False
        return tie
