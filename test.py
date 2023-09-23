import tkinter
from tkinter import filedialog as fd
from tkinter import colorchooser
import analyser


window = tkinter.Tk()
window.title('test')
window.geometry('550x420')


def select_file():
    filename = fd.askopenfilename()
    file_label['text'] = 'файл: ' + filename


def select_color():
    color = colorchooser.askcolor()
    color_label['text'] = color[1]
    color_square['bg'] = color[1]


def run():
    color = color_label['text']
    file = file_label['text']
    analyser.TextAnalyser(source_file=file,
                          parts_of_speech=generate_pos(),
                          destination_file="wordcloud.png",
                          words_ammount=int(words_ammount.get()),
                          wc_width=int(width.get()),
                          wc_height=int(height.get()),
                          wc_background=color,
                          )


# Create a list of possible POS tags
pos_tags = ["NOUN",
            "ADJF",
            "ADJS",
            "VERB",
            "INFN",
            "PRTF",
            "PRTS",
            "GRND",
            "NUMR",
            "ADVB",
            "NPRO",
            "PRED",
            "PREP"
            "CONJ",
            "PRCL",
            "INTJ"
            ]

# Create a dictionary to store the state of each checkbutton
pos_states = {}


# Create a function to generate the POS tags based on the selected checkbuttons
def generate_pos():
    selected_pos = []
    for pos, state in pos_states.items():
        if state.get() == 1:
            selected_pos.append(pos)
    if len(selected_pos) == 0:
        result_label.config(text="Please select at least one POS tag.")
    else:
        result = ", ".join(selected_pos)
        result_label.config(text=result)
    return selected_pos


result_label = tkinter.Label(window, text="")
result_label.grid()


file_label = tkinter.Label(window, text='файл:')
color_label = tkinter.Label(window, text='цвет:')
width_label = tkinter.Label(window, text='ширина:')
height_label = tkinter.Label(window, text='высота:')
words_label = tkinter.Label(window, text='количество слов:')
color_square = tkinter.Canvas(window, width=50, height=50, bg='#ffffff')
file_button = tkinter.Button(window, text='выбрать файл', command=select_file)
color_button = tkinter.Button(window,
                              text='выбрать цвет',
                              command=select_color
                              )
words_ammount = tkinter.Entry(window)
width = tkinter.Entry(window)
height = tkinter.Entry(window)
make_wordcloud = tkinter.Button(window, text='создать', command=run)


file_label.grid(column=0, row=0)
file_button.grid(column=1, row=0)
color_label.grid(column=0, row=1, rowspan=3, ipadx=4, ipady=6)
color_button.grid(column=1, row=2, rowspan=2, ipadx=4, ipady=6)
color_square.grid(column=2, row=3, padx=10,)
width_label.grid(column=0, row=4, pady=15)
width.grid(column=1, row=4, padx=15)
height_label.grid(column=0, row=5, pady=15)
height.grid(column=1, row=5)
words_label.grid(column=0, row=6, pady=15)
words_ammount.grid(column=1, row=6)

col = -1
row = 7

# Create checkbuttons for each POS tag
for pos in pos_tags:
    if col != 2:
        col += 1
    else:
        col = 0
        row += 1
    pos_states[pos] = tkinter.IntVar()
    pos_checkbutton = tkinter.Checkbutton(window,
                                          text=pos,
                                          variable=pos_states[pos]
                                          )
    pos_checkbutton.grid(column=col, row=row)


make_wordcloud.grid(pady=15, columnspan=3, rowspan=3, sticky='we', ipady=15)


window.mainloop()
