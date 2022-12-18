from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename


class PyNotePad:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Bloco de notas")

        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)

        menubar = Menu(self.root)
        MENUarquivo = Menu(menubar)

        MENUarquivo.add_command(label="Salvar", command=self.salvar)

        MENUarquivo.add_command(label="Abrir", command=self.abrir)

        menubar.add_cascade(label="Arquivo", menu=MENUarquivo)

        MENUajuda = Menu(menubar)
        MENUajuda.add_command(label="Sobre", command=self.sobre)

        menubar.add_cascade(label="Ajuda", menu=MENUajuda)
        self.root.config(menu=menubar)

        self.text = Text(self.root)
        self.text.pack(expand=YES, fill=BOTH)
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        self.root.mainloop()

    def salvar(self):

        fileName = asksaveasfilename()

        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def abrir(self):

        fileName = askopenfilename()

        try:
            file= open(fileName, 'r')
            contents = file.read()

            self.text.delete(0.0, END)
            self.text.insert(0.0, contents)
        except:
            pass

    def sobre(self):

        root = Tk()

        root.wm_title("Sobre")

        texto=("Bloco de notas em Python: Versão 1.0")
        textONlabel = Label(root, text=texto)
        textONlabel.pack()


PyNotePad()