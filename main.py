import tkinter as tk
import analyser

def run():
    TextAnalyser(file_path='text.txt',
                    encoding='UTF-8',
                    pos=['VERB', 'ADJF', 'NOUN', 'ADVB'],
                    contour_color='black',
                    bgc='white',
                    contour_width=3,
                    )


window = tk.Tk()
window.title('a')
window.geometry('300x300')
button = tk.Button(text='a', command=run)
words_ammount = tk.Entry(window)
button.pack()
words_ammount.pack()

window.mainloop()
