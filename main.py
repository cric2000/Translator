from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1080x400')

root.resizable(0,0)
root.config(bg = '#191919')

root.title("Anmol Lamba")

Label(root, text = "Translator", font = "verdana 20 bold", bg='#191919', pady="10" , fg='light green').pack()

Label(root,text ="Enter Text", font = 'verdana 12 bold', bg ='#191919' , fg='#FCB5AC').place(x=270,y=80)

Input_text = Text(root,font = 'verdana 10', height = 11, wrap = WORD, padx=5, pady=5, width = 53)
Input_text.place(x=30,y = 120)

Label(root,text ="Output", font = 'verdana 12 bold', bg ='#191919' , fg='#FCB5AC').place(x=700,y=80)

Output_text = Text(root,font = 'verdana 10', height = 11, wrap = WORD, padx=5, pady= 5, width =53 )
Output_text.place(x = 610 , y = 120)

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width =22 )
src_lang.place(x=40,y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=800,y=60)
dest_lang.set('choose output language')

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_btn = Button(root, text = 'Translate',font = 'verdana 10',pady = 5 , width=9,command = Translate , bg = 'white smoke', activebackground = '#FBB80F', fg='black')

trans_btn.place(x = 490, y= 180 )

root.mainloop()