import tkinter as tk
import analyser

'''
TextAnalyser(source_file="text.txt",
            parts_of_speech=["NOUN", "VERB"])
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
    analyser.TextAnalyser(source_file=file_path.get(),
                          parts_of_speech=["NOUN", "VERB"],
                          destination_file="wordcloud.png",
                          words_ammount=int(words_ammount.get()),
                          wc_width=int(width.get()),
                          wc_height=int(height.get()),
                          wc_background=bgc.get(),
                          )


window = tk.Tk()
window.title('test')
window.geometry('300x300')
VERB_1 = tk.StringVar()
VERB = tk.Checkbutton(window, text='VERB', onvalue='VERB', offvalue='',
                      variable=VERB_1)
ADJF_1 = tk.StringVar()
ADJF = tk.Checkbutton(window, text='ADJF', onvalue='ADJF', offvalue='',
                      variable=ADJF_1)
NOUN_1 = tk.StringVar()
NOUN = tk.Checkbutton(window, text='NOUN', onvalue='NOUN', offvalue='',
                      variable=NOUN_1)
ADVB = tk.Checkbutton(window, text='ADVB', onvalue='ADVB')
button = tk.Button(text='test', command=run)
words_ammount = tk.Entry(window)
bgc = tk.Entry(window)
file_path = tk.Entry(window)
width = tk.Entry(window)
height = tk.Entry(window)
file_path.pack()
width.pack()
height.pack()
bgc.pack()
words_ammount.pack()

VERB.pack()
ADJF.pack()
NOUN.pack()
ADVB.pack()

button.pack()


window.mainloop()
