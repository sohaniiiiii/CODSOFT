import math
import tkinter as tk
from tkinter import messagebox

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def on_click(row, col):
    if board[row][col] == " " and not game_over:
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED)
        check_game_state()
        if not game_over:
            ai_move()

def ai_move():
    global game_over
    row, col = best_move(board)
    if row != -1 and col != -1:
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state=tk.DISABLED)
    check_game_state()

def check_game_state():
    global game_over
    if is_winner(board, 'X'):
        messagebox.showinfo("Game Over", "Congratulations! You win!")
        game_over = True
    elif is_winner(board, 'O'):
        messagebox.showinfo("Game Over", "AI wins! Better luck next time.")
        game_over = True
    elif is_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        game_over = True

def reset_game():
    global board, game_over
    board = [[" " for _ in range(3)] for _ in range(3)]
    game_over = False
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state=tk.NORMAL)

# Initialize the game window
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

board = [[" " for _ in range(3)] for _ in range(3)]
game_over = False

buttons = [[tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c)) for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

tk.Button(root, text="Reset Game", font=('Arial', 14), command=reset_game).grid(row=3, column=0, columnspan=3)

root.mainloop()
