import tkinter as tk
import analyser


def run():
    analyser.TextAnalyser(file_path='text.txt',
                          encoding='UTF-8',
                          pos=['VERB', 'ADJF', 'NOUN', 'ADVB'],
                          contour_color='black',
                          bgc='white',
                          contour_width=3,)


window = tk.Tk()
window.title('a')
window.geometry('300x300')
button = tk.Button(text='a', command=run)
words_ammount = tk.Entry(window)
button.pack()
words_ammount.pack()

window.mainloop()

'''
не запускается на main.py
запускается на & C:/Users/username/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/username/Desktop/Новая папка (2)/main.py" в PS 
запускается на C:/Users/username/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/username/Desktop/Новая папка (2)/main.py" в cmd
'''
