import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from random import choice

root=tk.Tk()
root.title("Rock paper scissors")
root.iconbitmap("icon.ico")
root.geometry("1000x5000")

comp_score=0
play_score=0

def play_1():
    playf=tk.Frame(root,bg='tomato')
    playf.place(relwidth=1,relheight=1)

    global comp_score
    global play_score

    def play_2(name):
        total=score_set.get()
        cname=name.replace(" ","")

        if total=="Scores" and len(cname)==0:
            messagebox.showinfo("Error","You have'nt chosen a score and didnot enter your name")

        elif total=="Scores":
            messagebox.showinfo("Error","You have'nt chosen a score")

        elif len(cname)==0:
            messagebox.showinfo("Error","You have'nt entered your name")

        else:
            global comp_score
            global play_score
 
            playf2=tk.Frame(root,bg='tomato')
            playf2.place(relheight=1,relwidth=1)


            def player_dec(choice):
                global comp_score
                global play_score

                nums=[0,1,2]
                computer_choice=random.choice(nums)
                computer_choices=["rock","paper","scissors"]
                computer_chosen=computer_choices[computer_choice]
                if int(comp_score)<int(total) and int(play_score)<int(total):
                    if choice=="rock":
                        status1.config(text="Rock")
                        if computer_chosen=="rock":
                            status2.config(text="Rock")

                        if computer_chosen=="paper":
                            status2.config(text="Paper")
                            comp_score+=1
                            score2.config(text=comp_score)

                        if computer_chosen=="scissors":
                            status2.config(text="scissors")
                            play_score=play_score+1
                            score1.config(text=play_score)

                    if choice=="paper":
                        status1.config(text="Paper")
                    
                        if computer_chosen=="rock":
                            status2.config(text="Rock")
                            play_score+=1
                            score1.config(text=play_score)

                        if computer_chosen=="paper":
                            status2.config(text="Paper")
                            comp_score+=0
                            score2.config(text=comp_score)

                        if computer_chosen=="scissors":
                            status2.config(text="scissors")
                            comp_score+=1
                            score2.config(text=comp_score)

                    if choice=="scissors":
                        status1.config(text="Scissors")
                    
                        if computer_chosen=="paper":
                            status2.config(text="paper")
                            play_score+=1
                            score1.config(text=play_score)

                        if computer_chosen=="scissors":
                            status2.config(text="scissors")
                            comp_score+=0
                            score2.config(text=comp_score)

                        if computer_chosen=="rock":
                            status2.config(text="rock")
                            comp_score+=1
                            score2.config(text=comp_score)

                else:
                    if play_score>comp_score:
                        messagebox.showinfo("Winner","Conguratulations "+name+" ! You won,Keep it up")
                        home()

                    if comp_score>play_score:
                        messagebox.showinfo("Loser","Oops! You lost,Try again "+name)
                        home()

                    if comp_score==play_score:
                        messagebox.showinfo("Tie","Lucky! It's a tie "+name)
                        home()

                    play_score=0
                    comp_score=0

            you=tk.Label(playf2,text="You:",bg='tomato')
            you.place(relx=0.1,rely=0.0)
            
            comp=tk.Label(playf2,text="Computer:",bg='tomato')
            comp.place(relx=0.5,rely=0.0)

            score1=tk.Label(playf2,fg='white',bg='black',font='Ariel 30',text=0)
            score1.place(relx=0.1,rely=0.1,relheight=0.1,relwidth=0.2)

            score2=tk.Label(playf2,fg='white',bg='black',font='Ariel 30',text=0)
            score2.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.2)
            
            status1=tk.Label(playf2,font="ariel 20")
            status1.place(relx=0.1,rely=0.4,relheight=0.3,relwidth=0.2)

            status2=tk.Label(playf2,font="ariel 20")
            status2.place(relx=0.5,rely=0.4,relheight=0.3,relwidth=0.2)

            rock=tk.Button(playf2,text="Rock",command=lambda:player_dec("rock"))
            rock.place(relx=0.1,rely=0.8)

            paper=tk.Button(playf2,text="Paper",command=lambda:player_dec("paper"))
            paper.place(relx=0.3,rely=0.8)

            scissors=tk.Button(playf2,text="Scissors",command=lambda:player_dec("scissors"))
            scissors.place(relx=0.5,rely=0.8)


    name_h=tk.Label(playf,text="Enter your name:",bg='tomato')
    name_h.place(relx=0.3,rely=0.2)
    name=tk.Entry(playf)
    name.place(relx=0.5,rely=0.2)
    
    score_seth=tk.Label(playf,text="Choose your total score:",bg='tomato')
    score_seth.place(relx=0.3,rely=0.3)
    score_set=ttk.Combobox(playf,values=["Scores",5,10,15,20])
    score_set.place(relx=0.5,rely=0.3)
    score_set.current(0)

    start=tk.Button(playf,text="start",command=lambda:play_2(name.get()))
    start.place(relx=0.5,rely=0.4)

    back=tk.Button(playf,text="Back",command=home)
    back.place(relx=0.1,rely=0.7)

def about():
    messagebox.showinfo("About this game","Name:Rock Paper Scissors\nDate created:14/7/2020\nWritten in:Python\nWritten by:Govind Rajeesh")
def exit():
    exiter=messagebox.askquestion("Exit!","Are you sure that you want to quit the game?")

    if exiter=="yes":
        root.destroy()

    if exiter=="no":
        home()
def home():
    homef=tk.Frame(root,bg='tomato')
    homef.place(relheight=1,relwidth=1)

    heading=tk.Label(homef,text="Rock Paper Scissors",font='Ariel 40',bg='tomato')
    heading.place(relx=0.3,rely=0.1)

    play_btn=tk.Button(homef,text="Play",pady=5,padx=75,command=play_1,bg="deep sky blue")
    play_btn.place(relx=0.4,rely=0.3)

    about_btn=tk.Button(homef,text="About",pady=5,padx=75,bg="deep sky blue",command=about)
    about_btn.place(relx=0.4,rely=0.5)
 
    exit_btn=tk.Button(homef,text="   Exit",pady=5,padx=75,bg="deep sky blue",command=exit)
    exit_btn.place(relx=0.4,rely=0.7)


home()

root.mainloop()