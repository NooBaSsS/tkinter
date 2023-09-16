import tkinter as tk
import analyser

'''
analyser.TextAnalyser(file_path=file_path.get(),
                          encoding='UTF-8',
                          pos=pos,
                          contour_color=color.get(),
                          bgc=bgc.get(),
                          contour_width=int(contour_width.get()),
                          max_words=int(words_ammount.get())
                          )
'''


def run():
    pos = []
    if VERB_1.get():
        pos.append(VERB_1.get())
    if ADJF_1.get():
        pos.append(ADJF_1.get())
    if NOUN_1.get():
        pos.append(NOUN_1.get())

    print(pos)


window = tk.Tk()
window.title('a')
window.geometry('300x300')
VERB_1 = tk.StringVar()
VERB = tk.Checkbutton(window, text='VERB', onvalue='VERB', offvalue='', variable=VERB_1)
ADJF_1 = tk.StringVar()
ADJF = tk.Checkbutton(window, text='ADJF', onvalue='ADJF', offvalue='', variable=ADJF_1)
NOUN_1 = tk.StringVar()
NOUN = tk.Checkbutton(window, text='NOUN', onvalue='NOUN', offvalue='', variable=NOUN_1)
ADVB = tk.Checkbutton(window, text='ADVB', onvalue='ADVB')
button = tk.Button(text='a', command=run)
words_ammount = tk.Entry(window)
color = tk.Entry(window)
bgc = tk.Entry(window)
file_path = tk.Entry(window)
contour_width = tk.Entry(window)
file_path.pack()
color.pack()
bgc.pack()
contour_width.pack()
words_ammount.pack()

VERB.pack()
ADJF.pack()
NOUN.pack()
ADVB.pack()

button.pack()


window.mainloop()

'''
не запускается на main.py
запускается на & C:/Users/username/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/username/Desktop/Новая папка (2)/main.py" в PS
запускается на C:/Users/username/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/username/Desktop/Новая папка (2)/main.py" в cmd
'''
