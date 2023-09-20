import tkinter
from tkinter import filedialog as fd
from tkinter import colorchooser


def select_file():
    filename = fd.askopenfilename()
    file_label['text'] = filename


def select_color():
    color = colorchooser.askcolor()
    color_label['text'] = color[1]
    color_square['bg'] = color[1]


def run():
    color = color_label['text']
    file = file_label['text']


window = tkinter.Tk()
file_label = tkinter.Label(window, text='файл')
color_label = tkinter.Label(window, text='цвет')
width_label = tkinter.Label(window, text='ширина')
height_label = tkinter.Label(window, text='высота')
words_label = tkinter.Label(window, text='количество слов')
color_square = tkinter.Canvas(window, width=50, height=50, bg='#ffffff')
file_button = tkinter.Button(window, text='выбрать файл', command=select_file)
color_button = tkinter.Button(window, text='выбрать цвет', command=select_color)
words_ammount = tkinter.Entry(window)
width = tkinter.Entry(window)
height = tkinter.Entry(window)
make_wordcloud = tkinter.Button(window, text='создать', command=run)


file_label.pack()
file_button.pack()
color_label.pack()
color_button.pack()
color_square.pack()
width_label.pack()
width.pack()
height_label.pack()
height.pack()
words_label.pack()
words_ammount.pack()


window.mainloop()
