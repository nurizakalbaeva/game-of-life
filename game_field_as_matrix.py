from tkinter import *
from time import sleep
from random import randint, choice
from turtle import heading
 
class Field:
    def __init__(self, c, n, m, width, height):
        '''
       c - canvas instance
       n - number of rows
       m - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       
       '''
        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        av_m = round(self.m / 2)
        av_n = round(self.n / 2)
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                # self.a[i].append(choice([0, 1]))
                if i == av_n - 7 and j == av_m:
                    self.a[av_n - 7].append(1)
                elif i == av_n - 6 and (av_m - 2 < j < av_m + 2):
                    self.a[av_n - 6].append(1)
                elif i == av_n - 5 and (av_m - 3 < j < av_m + 3):
                    self.a[av_n - 5].append(1)
                elif i == av_n - 4 and (av_m - 4 < j < av_m + 4):
                    self.a[av_n - 4].append(1)
                elif i == av_n - 3 and (av_m - 5 < j < av_m + 5):
                    self.a[av_n - 3].append(1)
                elif i == av_n - 2 and (av_m - 6 < j < av_m + 6):
                    self.a[av_n - 2].append(1)
                elif i == av_n - 1 and (av_m - 7 < j < av_m + 7):
                    self.a[av_n - 1].append(1)
                elif i == av_n  and (av_m - 8 < j < av_m + 8):
                    self.a[av_n].append(1)
                elif i == av_n + 1 and (av_m - 7 < j < av_m + 7):
                    self.a[av_n + 1].append(1)
                elif i == av_n + 2 and (av_m - 6 < j < av_m + 6):
                    self.a[av_n + 2].append(1)
                elif i == av_n + 3 and (av_m - 5 < j < av_m + 5):
                    self.a[av_n + 3].append(1)
                elif i == av_n + 4 and (av_m - 4 < j < av_m + 4):
                    self.a[av_n + 4].append(1)
                elif i == av_n + 5 and (av_m - 3 < j < av_m + 3):
                    self.a[av_n + 5].append(1)
                elif i == av_n + 6 and (av_m - 2 < j < av_m + 2):
                    self.a[av_n + 6].append(1)
                elif i == av_n + 7 and j == av_m:
                    self.a[av_n + 7].append(1)
                else:
                    self.a[i].append(0)
       
        
        self.draw()
   
    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)
       
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neib_sum = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + self.a[i - 1][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1]
                if neib_sum < 2 or neib_sum > 4:
                    b[i][j] = 0
                elif neib_sum == 3 or neib_sum == 2 or neib_sum == 4:
                    b[i][j] = 1
                else:
                    b[i][j] = self.a[i][j]
       
        self.a = b
 
 
    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()
 
    def draw(self):
        '''
       draw each element of matrix as a rectangle with white background and wall rectangle should have dark grey background
       '''
        color = "grey"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "yellow"
                else:
                    color = "white"
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
    
        self.c.after(500, self.draw)
 
 
root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()
 
f = Field(c, 39, 39, 800, 800)
f.print_field()
root.mainloop()