import tkinter
from tkinter import filedialog as fd
from tkinter import colorchooser
import analyser


window = tkinter.Tk()
window.title('test')
window.geometry('350x700')


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
    analyser.TextAnalyser(source_file=file,
                          parts_of_speech=["NOUN", "VERB"],
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
    print(selected_pos)


result_label = tkinter.Label(window, text="")
result_label.pack()


file_label = tkinter.Label(window, text='файл')
color_label = tkinter.Label(window, text='цвет')
width_label = tkinter.Label(window, text='ширина')
height_label = tkinter.Label(window, text='высота')
words_label = tkinter.Label(window, text='количество слов')
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
make_wordcloud.pack()
# Create checkbuttons for each POS tag
for pos in pos_tags:
    pos_states[pos] = tkinter.IntVar()
    pos_checkbutton = tkinter.Checkbutton(window,
                                          text=pos,
                                          variable=pos_states[pos]
                                          )
    pos_checkbutton.pack()


window.mainloop()
