import re
import numpy as np

def parse_input():
    with open('data/input4.txt', 'r') as f:
        collapse_whitespace = re.compile(r'\s+')
        data = f.read().split('\n\n')
        numbers = np.array(data[0].split(',')).astype(int)
        board_data = [board.split('\n') for board in data[1:-1]]
        boards = []
        for board in board_data:
            board = np.array([
                np.array(collapse_whitespace.sub(' ', row).strip().split(' '))
                for row in board
            ]).astype(int)
            boards.append(board)
        boards = np.array(boards)
        
        return numbers, boards

if __name__ == "__main__":
    numbers, boards = parse_input()
    
    play_boards = boards.copy()
    for i, number in enumerate(numbers):
        play_boards = np.where(play_boards == number, -1, play_boards)
        if i >= 5:
            bingo_columns = np.all(play_boards == -1, axis=1)
            bingo_rows = np.all(play_boards == -1, axis=2)
            if np.any(bingo_columns):
                winning_boards, _ = np.where(bingo_columns)
                break
            elif np.any(bingo_rows):
                winning_boards, _ = np.where(bingo_rows)
                break
                
    winning_board = play_boards[winning_boards[0]]
    print(f'Part 1: {winning_board[winning_board != -1].sum() * numbers[i]}')
          
    play_boards = boards.copy()
    for i, number in enumerate(numbers):
        play_boards = np.where(play_boards == number, -1, play_boards)
        if i >= 5:
            bingo_columns = np.all(play_boards == -1, axis=1)
            bingo_rows = np.all(play_boards == -1, axis=2)
            non_winning_boards = np.where(~np.any(np.logical_or(bingo_columns, bingo_rows), axis=1))[0]
            if len(non_winning_boards) == 0:
                break
            non_winners = non_winning_boards
          
    last_winning_board = play_boards[non_winners[0]]
    print(f'Part 2: {last_winning_board[last_winning_board != -1].sum() * numbers[i]}')