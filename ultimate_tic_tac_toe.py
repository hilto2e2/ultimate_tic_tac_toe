from tkinter import *
from tkinter import messagebox
import random

############### GameFrame Class #######################
class GameFrame:

    def __init__(self, frame, row, col, color):
        self.frame_winner = "None"
        self.frame_full = 0
        self.buttons = [[],[],[]]
        #print ("row=", row, "col=", col)
        self.frame = create_frame(frame, color)
        #self.frame.config(command= lambda row=row,col=col:change_frame(row,col))
        self.frame.grid(row=row, column=col)
        #self.frame.bind("<Button>", lambda event, row=row, col=col: change_frame(row, col))
        for i in range(3):
            for j in range(3):
                self.buttons[i].append(create_button(self.frame))
                self.buttons[i][j].config(command= lambda game_frame=self,row=i,col=j:click(game_frame,row,col))
                self.buttons[i][j].grid(row=i,column=j)

    def check_frame_winner(self, turn):
        b = self.buttons
        for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==turn or
               b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==turn):
                self.frame_winner = turn
                self.disable_frame_buttons(turn)
                return turn
                
        if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==turn or
           b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==turn):
            self.frame_winner = turn
            self.disable_frame_buttons(turn)
            return turn

        return "None"

    def check_full_frame(self):
        b = self.buttons
        for i in range(3):
            for j in range (3):
                if(b[i][j]["text"] != "X" and b[i][j]["text"] != "O"):
                    self.frame_full = 0
                    return "false"
                    
        self.frame_full=1
        return "true"
    
    def disable_frame_buttons(self, turn):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["state"] = DISABLED
                #if turn == "X":
                    #self.buttons[i][j].config(bg="green")
               # else:
                    #self.buttons[i][j].config(bg="blue")


    def enable_frame_buttons(self):
        print("enable buttons")
        for i in range(3):
            for j in range(3):
                print("button_text ", i, j, "= ", self.buttons[i][j]["text"])
                if (self.buttons[i][j]["text"] != "X" and self.buttons[i][j]["text"] != "O"):
                    self.buttons[i][j]["state"] = NORMAL
                else:
                    print("skipping enable of button: ", i, j)
                
    def reset_frame(self):
        self.frame_winner = "None"
        self.frame_full = 0
        b = self.buttons
        for i in range(3):
            for j in range(3):
                b[i][j]["text"] = ""

        self.enable_frame_buttons()        
############### GameBoard Class #######################
class GameBoard:
    colors = [['blue', 'yellow', 'red'], ['green', 'purple', 'black'], ['brown', 'magenta', 'pink']]

    def __init__(self, frame):
        self.frames = [[],[],[]]
        self.turn=random.choice(['O','X'])
        for i in range(3):
            for j in range(3):
                #game_frame = GameFrame(frame, i, j, self.colors[i][j])
                game_frame = GameFrame(frame, i, j, "white")
                self.frames[i].append(game_frame)

    def check_winner(self):
        f = self.frames

        for i in range(3):
            if(f[i][0].frame_winner==f[i][1].frame_winner==f[i][2].frame_winner==self.turn or
               f[0][i].frame_winner==f[1][i].frame_winner==f[2][i].frame_winner==self.turn):
                messagebox.showinfo("Congrats!!","'"+self.turn+"' has won")
                self.reset_game()
                return "true"
            if(f[0][0].frame_winner==f[1][1].frame_winner==f[2][2].frame_winner==self.turn or
               f[0][2].frame_winner==f[1][1].frame_winner==f[2][0].frame_winner==self.turn):
                messagebox.showinfo("Congrats!!","'"+self.turn+"' has won")
                self.reset_game()
                return "true"
            elif(f[0][0].frame_winner==f[0][1].frame_winner==f[0][2].frame_winner==f[1][0].frame_winner==f[1][1].frame_winner==f[1][2].frame_winner==f[2][0].frame_winner==f[2][1].frame_winner==f[2][2].frame_winner==DISABLED):
                messagebox.showinfo("Tied!!","The match ended in a draw")
                self.reset_game()
                return "true"
            
        return "false"

    def check_enable_frame(self, row, col): 
        f = self.frames
        #f_winner = f[row][col].check_frame_winner(self.turn)
        f_full = f[row][col].check_full_frame()
        f_winner = f[row][col].frame_winner
        print("frame_winner = ", f_winner)
        print("frame_full = ", f_full)
        for x in range(3):
            for y in range(3):
                if (f_winner != "None" or f_full=="true"):
                    if (f[x][y].frame_winner == "None" and f[x][y].check_full_frame() =="false"):
                        f[x][y].enable_frame_buttons()
                        f[x][y].frame.config(bg="red")
                    else:
                        f[x][y].disable_frame_buttons(self.turn)
                        f[x][y].frame.config(bg="white")
                elif (x==row and y==col):
                    print('frame enable', row , col)
                    f[x][y].enable_frame_buttons()
                    f[x][y].frame.config(bg="red")
                else:
                    f[x][y].disable_frame_buttons(self.turn)
                    print("disabled frame: ", x, y)
                    f[x][y].frame.config(bg="white")

                
                    

    def change_turn(self):
        print(self.turn)
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        
    def reset_game(self):
        f = self.frames
        for i in range(3):
            for j in range(3):
                f[i][j].reset_frame()
                f[i][j].frame.config(bg="white")
                
        self.turn=random.choice(['O','X'])

                
############### Global Functions #######################
def create_button(frame):
    #b = Button(frame, padx=1, bg="papaya whip", width=3, text="   ", font=('arial',32,'bold'), relief="sunken", bd=5)
    b = Button(frame, padx=1, bg="black", width=3, text="   ", font=('arial',32,'bold'), relief="sunken", bd=5)
    return b

def create_frame(root, color):
    f = Frame(root, width=200, height=200, bd=2, bg=color, padx=5, pady=5)
    return f

       
def click(game_frame,row,col):
    print("click detected: ", row, col)
    print("frame: ", game_frame.frame)
    game_frame.frame.config(bg="red")
    game_frame.buttons[row][col].config(text=board.turn,state=DISABLED,disabledforeground=colour[board.turn])
    print("here:"+board.turn)
    val = game_frame.check_frame_winner(board.turn)
    print(val)
    has_winner = board.check_winner()
    if (has_winner == "false"):
        board.check_enable_frame(row, col)
        board.change_turn()
        label.config(text=board.turn+"'s Turn")
        
###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe")   #Title given
#root.geometry("1000x1000")
#root.rowconfigure([0,1,2], weight=1)
#root.columnconfigure([0,1,2], weight=1)

colour={'O':"deep sky blue",'X':"lawn green"}
board = GameBoard(root)

reset_button = Button(root, padx=1, bg="blue", width=6, text="RESET", font=('arial', 20, 'bold'), bd=5)
reset_button.config(command= lambda :board.reset_game())
reset_button.grid(row=5, column=5, columnspan=5)

label=Label(text=board.turn+"'s Turn",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()

