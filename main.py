import tkinter as tk
from tkinter import font

class Game_board(tk.Tk):
    def __init__(self) :
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self.create_board_display()
        self.create_board_grid()

    def create_board_display(self):
        displayfram = tk.Frame(master=self)
        displayfram.pack(fill=tk.X)
        self.display = tk.Label(master=displayfram, text="Ready?", font=font.Font(size=28, weight="bold"))
        self.display.pack()
    
    def create_board_grid(self):
        gird_frame = tk.Frame(master=self)
        gird_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=50)
            for col in range(3):
                #button = tk.Button(master=gird_frame, text="", font=font.Font(size=36, weight='bold'), fg="black", width=3, height=2, highlightthickness="lightblue")
                button = tk.Button(master=gird_frame, text="", font=font.Font(size=36, weight='bold'), fg="black", width=3, height=2, highlightthickness=2)

                self._cells[button] = (row, col)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

def main():
    board = Game_board()
    board.mainloop()

if __name__ == '__main__':
    main()