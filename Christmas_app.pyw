from tkinter import *
from tkinter import ttk
from random import choice
import os
import shutil

class ChristmasPresents:

       
    def __init__(self, root):

        root.title("Christmas Presents")

        mframe = ttk.Frame(root, padding=10, width=400, height=400)
        mframe.grid(column=0, row=0, sticky=(W, S, E, N))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.info2_var = StringVar()       
        self.text_var = ""
        self.text_field = Text(mframe, width=40, height=40)
        self.text_field.grid(column=1, row=1, sticky=(W, S, E, N))

        self.info1_label = Label(mframe, text="Do pola tekstowego proszę wpisać listę osób biorących udział w losowaniu jeden pod drugim.\nKażda osoba może wystąpić tylko raz. Pomiędzy osobami nie może być pustej linii.", borderwidth=5)
        self.info1_label.grid(column=1,columnspan=2, row=0, sticky=W)

        self.button_draw = ttk.Button(mframe, text="Losowanie", command=self.start_draw)
        self.button_draw.grid(row=1, column=2, sticky=W)

        self.info2_label = Label(mframe, textvariable=self.info2_var, borderwidth=5)
        self.info2_label.grid(column=1,columnspan=2, row=3, sticky=W)



    def format_var(self, str_to_format):
        str_to_format = str_to_format.strip("\n")
        end_list = str_to_format.split("\n")
        return end_list

    def draw(self, buyer, getter):
        if buyer in getter:
            getter.remove(buyer)
        return choice(getter)

    def drawing_program(self, drawing_list):
        buyers = drawing_list
        getters = buyers.copy()
        end_res = {}



        for person in buyers:
            if len(getters)==2 and buyers[-1] in getters:
                end_res[person] = getters[1]
                end_res[buyers[-1]] = getters[0]
                break
            end_res[person] = self.draw(person,getters.copy())
            getters.remove(end_res[person])
        return end_res

    def make_files(self, buyers, pair):
        try:
            shutil.rmtree("Prezenty")
        except:
            pass
        
        try:
            os.mkdir("Prezenty")
        except:
            pass
        
        for person in buyers:
            with open("Prezenty/"+person+".txt","w") as file:
                file.write(person+", osoba, którą wylosowałeś/aś to: "+pair[person])

        
    def start_draw(self):
        self.text_var = self.format_var(self.text_field.get("1.0","end"))
        end_res =  self.drawing_program(self.text_var)
        self.make_files(self.text_var, end_res)
        self.info2_var.set("Skończyłem. Wyniki są w plikach tekstowych w folderze \"Prezenty\".")
        
    
        

root = Tk()
ChristmasPresents(root)
root.mainloop()
