import tkinter as tk
from tkinter import messagebox
from astar import astar
from state import find_zero
import time
import customtkinter as ctk

LEVELS = {
    "Easy":   [[1, 2, 3], [4, 0, 6], [7, 5, 8]],
    "Medium": [[1, 0, 3], [4, 2, 5], [7, 8, 6]],
    "Hard":   [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
}

GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Puzzle8GUI:
    def __init__(self, master):
        self.master = master
        master.title("8-Puzzle Solver")
        master.withdraw() # إخفاء النافذة الرئيسية حتى يتم اختيار المستوى

        self.level = "Easy" # القيمة الافتراضية
        self.show_level_selection()

    def show_level_selection(self):
        selection_win = ctk.CTkToplevel(self.master)
        selection_win.title("Select Level")
        selection_win.geometry("300x250")

        # تعديل العنوان بالشكل الجديد
        title_label = ctk.CTkLabel(
            selection_win, 
            text="Choose Difficulty", 
            font=ctk.CTkFont(family="Helvetica", size=18, weight="bold")
        )
        title_label.pack(pady=20)

        # تعديل الزراير عشان تكون Modern
        for lvl_name in LEVELS.keys():
            btn = ctk.CTkButton(
                selection_win, 
                text=lvl_name, 
                font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"),
                width=180, 
                height=40, 
                corner_radius=15, # الزوايا الدائرية
                command=lambda l=lvl_name: self.start_game(l, selection_win)
            )
            btn.pack(pady=8)

    def start_game(self, chosen_level, selection_win):
        selection_win.destroy() # إغلاق نافذة الاختيار
        self.master.deiconify() # إظهار النافذة الرئيسية
        
        self.level = chosen_level
        self.board = [row[:] for row in LEVELS[self.level]]
        self.start_time = time.time()
        self.moves_count = 0

        self.setup_ui()

    def setup_ui(self):
        self.tiles = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                num = self.board[i][j]
                text = str(num) if num != 0 else ""
                
                # تحديد الألوان (أزرق للمربعات، ورمادي غامق للمربع الفاضي)
                tile_color = "#1f538d" if num != 0 else "#2B2B2B"
                
                btn = ctk.CTkButton(
                    self.master,
                    text=text,
                    width=90,
                    height=90,
                    corner_radius=15,
                    font=ctk.CTkFont(family="Helvetica", size=24, weight="bold"),
                    fg_color=tile_color,
                    text_color="white",
                    hover=False # عشان المربعات دي مش زراير هنضغط عليها بالماوس
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.tiles[i][j] = btn

        # ... (باقي كود الـ bind للأسهم وزرار Solve هيفضل زي ما هو مؤقتاً)
        # ربط الأسهم (التحكم الطبيعي)
        self.master.bind("<Up>", self.press_up)
        self.master.bind("<Down>", self.press_down)
        self.master.bind("<Left>", self.press_left)
        self.master.bind("<Right>", self.press_right)

        ctk.CTkButton(self.master, text="Solve Automatically", font=ctk.CTkFont(family="Helvetica", size=12), command=self.solve).grid(row=3, column=0, columnspan=3, sticky="we", pady=10)
        
        self.status_label = ctk.CTkLabel(self.master, text=f"Moves: {self.moves_count} Time: 0s", font=ctk.CTkFont(family="Helvetica", size=12))
        self.status_label.grid(row=4, column=0, columnspan=3)
        
        self.update_timer()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                num = self.board[i][j]
                
                # تجهيز النص واللون الجديد
                text = str(num) if num != 0 else ""
                tile_color = "#1f538d" if num != 0 else "#2B2B2B"
                
                # استخدام configure لتحديث المربع في CustomTkinter
                self.tiles[i][j].configure(text=text, fg_color=tile_color)

    def move(self, di, dj):
        i, j = find_zero(self.board)
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            self.board[i][j], self.board[ni][nj] = self.board[ni][nj], self.board[i][j]
            self.moves_count += 1
            self.update_board()
            self.update_status()
            if self.board == GOAL:
                elapsed = int(time.time() - self.start_time)
                messagebox.showinfo("Success!", f"Level: {self.level}\nMoves: {self.moves_count}\nTime: {elapsed}s")
                return True
        return False

    def press_up(self, e):
        self.move(-1, 0)
    def press_down(self, e):
        self.move(1, 0)
    def press_left(self, e):
        self.move(0, -1)
    def press_right(self, e):
        self.move(0, 1)

    def solve(self):
        sol = astar(self.board, GOAL)
        if sol:
            for move_name in sol:
                self.master.update()
                time.sleep(0.3)
                if move_name == "UP": self.move(-1, 0)
                elif move_name == "DOWN": self.move(1, 0)
                elif move_name == "LEFT": self.move(0, -1)
                elif move_name == "RIGHT": self.move(0, 1)

    def update_status(self):
        elapsed = int(time.time() - self.start_time)
        self.status_label.configure(text=f"Moves: {self.moves_count}   Time: {elapsed}s")
    
    def update_timer(self):
        if self.board != GOAL:
            self.update_status()
            self.master.after(1000, self.update_timer)

def main():
    ctk.set_appearance_mode("Dark")
    root = ctk.CTk()
    app = Puzzle8GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()