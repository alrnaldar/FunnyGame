from tkinter import *
import random
from translate import Translator
from PIL import Image, ImageTk
import time
from tkinter import messagebox
import keyboard as key
counta = 0
count = 0
surrender = 0
countb = 0
countc = 0
a = 0
b=0
tk = Tk()
tk.title("funny game")
tk.geometry("500x500")
translation_process = Translator(to_lang="rus")
img = PhotoImage(file="imgs/its_time_to_learn_english.png")
img2 = PhotoImage(file="imgs/start.png")
img3 = PhotoImage(file="imgs/example.png")
img4 = ImageTk.PhotoImage(Image.open(r"imgs/gamemode.png"))
img5 = ImageTk.PhotoImage(Image.open(r"imgs/rama.png"))
img6 = ImageTk.PhotoImage(Image.open(r"imgs/example2.png"))
img7 = PhotoImage(file="imgs/quad.png")
img8 = PhotoImage(file="imgs/quad.png")
img9 = PhotoImage(file="imgs/pointer.png")
bgimage = PhotoImage(file="imgs/bg.png")

with open('wordlist.10000.txt', 'r') as file:
    words = file.readlines()
    words = [s.strip("\n") for s in words]
    def checkcra():
        pass
    def back():
        

        white = Label(tk,image=bgimage)
        white.place(x=0,y=0)
        
        choice()

    def useword():
        global counta,wordqa1,qaquestionl
        
        
        counta +=1
        
        def uncorrectanswer():
                messagebox.showerror("ошибка","неправильный ответ, попробуйте еще раз")
        def switchlanguage():
            global switchsecondbutton,qq2,ww2,ww3,ww4
            wordqa1button.place_forget()
            wordqa2button.place_forget()
            wordqa3button.place_forget()
            switchcrabutton.place_forget()
            counterl.place_forget()
            qaquestionl.place_forget()
            
            def rcraagain():
                global count
                count+=1
                
                counterl = Label(tk,text=f"изучено {count} новых слов",font="header 20")
                counterl.place(x=0,y=0)
                
                coords = [0,300,150]
                ycoords = [300,410,380]
                k1 = random.choice(coords)
                k2 = random.choice(coords)
                k3 = random.choice(coords)

                y1 = random.choice(ycoords)
                y3 = random.choice(ycoords)
                if k1 == k2 or k1 == k3 or y1==y3:
                    k1 = 300
                    k2 = 150
                    k3 = 0
                    # k1 = random.choice(coords)
                    # k2 = random.choice(coords)
                    # k3 = random.choice(coords)
                    y1 = random.choice(ycoords)
                    y3 = random.choice(ycoords)


                word = random.choice(words)
                word2 = random.choice(words)
                word3 = random.choice(words)
                wordqa1 = translation_process.translate(word)
                
                
                qq2.configure(text=wordqa1)
                ww2.configure(text=word)
                ww2.place(x=k1,y=y1)
                ww3.configure(text=word2)
                ww3.place(x=k2,y=340)
                ww4.configure(text=word3)
                ww4.place(x=k3,y=y3)
            
            
            word = random.choice(words)
            word2 = random.choice(words)
            word3 = random.choice(words)
            word_translated = translation_process.translate(word)
            qq2 = Label(tk, text=word,font="header 40")
            qq2.place(x=140,y=40)
            # word1
            wordqa1 = translation_process.translate(word)
            ww2 = Button(tk, text=wordqa1,command=rcraagain)
            ww2.place(x=0,y=300)
            # word2
            wordqa2 = translation_process.translate(word2)
            ww3 = Button(tk, text=wordqa2,command=uncorrectanswer)
            ww3.place(x=150,y=330)
            # word3
            wordqa3 = translation_process.translate(word3)
            ww4 = Button(tk, text=wordqa3,command=uncorrectanswer)
            ww4.place(x=300,y=350)
            switchsecondbutton = Button(tk, text="switch language", font="header 18", command=useword)
            switchsecondbutton.place(x=140,y=455)
        # global word, wordqa1
        
        def craagain():
            global count
            count+=1
            
            

            xcoords = [0,300,150]
            ycoords = [300,410,380]
            k1 = random.choice(xcoords)
            k2 = random.choice(xcoords)
            k3 = random.choice(xcoords)
            
            y1 = random.choice(ycoords)
            y3 = random.choice(ycoords)
            if k1 == k2 or k1 == k3 or y1 == y3:
                k1 = 300
                k2 = 150
                k3 = 0
                # k1 = random.choice(xcoords)
                # k2 = random.choice(xcoords)
                # k3 = random.choice(xcoords)
                y1 = random.choice(ycoords)
                y3 = random.choice(ycoords)
            

            word = random.choice(words)
            word2 = random.choice(words)
            word3 = random.choice(words)
            wordqa1 = translation_process.translate(word)
            wordqa2 = translation_process.translate(word2)
            wordqa3 = translation_process.translate(word3)
            
            qaquestionl.configure(text=word)
            
            wordqa1button.configure(text=wordqa1)
            wordqa1button.place(x=k1,y=y1)
            wordqa2button.configure(text=wordqa2)
            wordqa2button.place(x=k2,y=340)
            wordqa3button.configure(text=wordqa3)
            wordqa3button.place(x=k3,y=y3)
            
            counterl = Label(tk,text=f"изучено{count}новых слов",font="header 20")
            counterl.place(x=0,y=0)
            
        
        if counta >= 2:

            switchsecondbutton.place_forget()
            qq2.place_forget()
            ww2.place_forget()
            ww3.place_forget()
            ww4.place_forget() 
        word = random.choice(words)
        word2 = random.choice(words)
        word3 = random.choice(words)
        qaquestionl = Label(tk, text=word,font="header 40")
        qaquestionl.place(x=140,y=40)
        # word1
        
        wordqa1 = translation_process.translate(word)
        wordqa1button = Button(tk, text=wordqa1,command=craagain)
        wordqa1button.place(x=0,y=300)
        # word2
        wordqa2 = translation_process.translate(word2)
        wordqa2button = Button(tk, text=wordqa2,command=uncorrectanswer)
        wordqa2button.place(x=150,y=330)
        # word3
        wordqa3 = translation_process.translate(word3)
        wordqa3button = Button(tk, text=wordqa3,command=uncorrectanswer)
        wordqa3button.place(x=300,y=350)

        switchcrabutton = Button(tk, text="switch language", font="header 18", command=switchlanguage)
        switchcrabutton.place(x=140,y=455)

        backtochoice = Button(tk, text="back",font="header 15", command=back)
        backtochoice.place(x=0,y=460)

        counterl = Label(tk,text=f"изучено {count} новых слов",font="header 20")
        counterl.place(x=0,y=0)
        
        
               
    def choice():
        global counta,count
        count = 0
        counta = 0
        lbl.place_forget()
        btn.place_forget()
        # gamemode pic
        gamemodel = Label(tk, image=img4)
        gamemodel.place(x=50,y=-5)
        
        # choose right answer
        def cra():
            
            gamemodel.place_forget()
            crabutton.place_forget()
            spoilerb.place_forget()
            qabutton.place_forget()
            spoiler2b.place_forget()
            
            
            strelkil = Label(tk, image=img5)
            strelkil.place(x=0,y=100)
            
            useword()

            


        def showspoiler1():
            def hidespoiler1():
                spoilerbh.place_forget()
                spoilerl.place_forget()
                spoilerb.place(x=0,y=200)
                spoiler()
            spoilerbh= Button(tk, text="hide spoiler",command=hidespoiler1)
            spoilerbh.place(x=0,y=220)
            spoilerl = Label(tk, image=img3)
            spoilerl.place(x=0,y=200)

        
        
        def spoiler():
            global spoilerb
            spoilerb = Button(tk, text="spoiler",font="header 8",command=showspoiler1)
            spoilerb.place(x=0,y=200)
        spoiler()
        
        
        def showspoiler2():
            def hidespoiler2():
                spoiler2l.place_forget()
                spoiler2bh.place_forget()
                spoiler2b.place(x=240,y=200)
                spoiler2()
            spoiler2bh = Button(tk, text="hide spoiler",command=hidespoiler2)
            spoiler2bh.place(x=160,y=200)
            spoiler2l = Label(tk, image=img6)
            spoiler2l.place(x=240,y=200)
            time.sleep(2)

        crabutton = Button(tk, text="choose right answer", font="header 20",command=cra)
        crabutton.place(x=240,y=100)
        def spoiler2():
            global spoiler2b
            
            spoiler2b = Button(tk, text="spoiler",font="header 8", command=showspoiler2)
            spoiler2b.place(x=240,y=200)
        spoiler2()
        
        # question answer
        def qa():
            global question
            gamemodel.place_forget()
            crabutton.place_forget()
            spoilerb.place_forget()
            qabutton.place_forget()
            spoiler2b.place_forget()


            
            
            def qaprocess():
                global question,transled
                
                
                ramkaqa2entry.delete("0",END)
                startb.place_forget()
                question.place_forget()
                word = random.choice(words)
                question = Label(tk, text=word,font="header 15")
                question.place(x=105,y=51)
                lenword = len(word)
                transled = translation_process.translate(word)
                
                print(transled)
                if lenword <18:
                    question.place(x=200,y=51)
                
                def right():
                    messagebox.showinfo("ответ",f"right answer:{transled}")
                    qaprocess()
                def press():
                    def tohide():
                        spoiler3.place_forget()
                        pressentr.place_forget()
                    spoiler3 = Label(tk,text="to enter press enter key")
                    spoiler3.place(x=93,y=320)
                    pressentr.configure(text="hide",command=tohide)
                    
                def check():
                    
                    
                    # transled = translation_process.translate(word)
                    answer = ramkaqa2entry.get()
                    
                    if answer == transled:
                        global countb,surrender
                        surrender = 0
                        countb +=1
                        
                        progress.configure(text=f"новых слов изученно:{countb}")
                        
                        qaprocess()    
                    # else:
                    #     answer = transled
                    #     surrender+=1
                    #     if surrender >= 3:
                    #         surrenderb = Button(tk,text="NEXT",font="header 20", command=qaprocess)
                    #         surrenderb.place(x=0,y=260)
                    #     messagebox.showerror("ошибка","неправильный ответ, попробуй еще раз(возможно первую букву в верхнем регистре)")
                        
                pressentr = Button(tk, text="spoiler",command=press)
                pressentr.place(x=93,y=300)
                next = Label(tk, text='if you cant answer press "check right answer"')
                next.place(x=115,y=400)
                
                checkanswer = Button(tk, text="check right answer",command=right)
                checkanswer.place(x=186,y=426)
                
                key.add_hotkey("enter", check)
                
            ramkaqa1 = Label(tk, image=img7)
            ramkaqa1.place(x=-150,y=-120)

            
            ramkaqa2 = Label(tk, image=img8)
            ramkaqa2.place(x=-150,y=90)

            ramkaqa2entry = Entry(tk,width="21",font="header 20")
            ramkaqa2entry.place(x=103,y=260,height=30)

            pointer = Label(tk, image=img9)
            pointer.place(x=225,y=120)

            question = Label(tk, text="translate this",font="header15")
            question.place(x=105,y=51)


            startb = Button(tk, text="start", font="header 20", command=qaprocess)
            startb.place(x=200,y=400)

            backtochoice = Button(tk, text="back",font="header 15", command=back)
            backtochoice.place(x=0,y=460)
            
            

            

            progress = Label(tk, text=f"новых слов изученно:{0}",font="header 20")
            progress.place(x=0,y=0)
            ramkaqa2entry.insert(0,"text there (entry zone)")
        qabutton = Button(tk, text="question-answer",font="header 20",command=qa)
        qabutton.place(x=0,y=100)


        
        
        
    def show():
        
        lbl2.place(x=100,y=0)
        
        translated = translation_process.translate(word)
        
        
        
        lbl2.configure(text=translated)
        # global word
        # word = random.choice(words)
        
        # lbl2.place_forget()
        
        
        # lbl.configure(text=word)
      

lbl = Label(tk, image=img)
lbl.place(x=0,y=0)


# btn = Button(tk, text="старт",font="header 20",command=choice)
btn = Button(tk, image=img2,command=choice)
btn.place(x=180,y=350)



tk.mainloop()


# некст дей я хочу сделать
# 1. чекнуть функцию check, надо сделать отображение правильных решений
# 2.  