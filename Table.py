from customtkinter import *

class Table:
    def __init__(self, root, Headers, Entries):
        rows = len(Entries)
        cols = len(Entries[0])
        for i in range(cols):
            self.e = CTkButton(root, text=Headers[i])
            self.e.grid(row=0, column=i, padx=2, pady=2)
            
        for i in range(rows):
            for j in range(cols):
                self.e = CTkEntry(root, justify='center')
                self.e.grid(row = i+1, column = j, padx=2, pady=2)
                self.e.insert(END, Entries[i][j])
                self.e.configure(state='disabled')

headers = ["SR No", "Name", "City", "Age"]

List = [(1,'Raj','Mumbai',19),
        (2,'Aaryan','Pune',18),
        (3,'Vaishnavi','Mumbai',20),
        (4,'Rachna','Mumbai',21),
        (5,'Shubham','Delhi',21)]


root = CTk()
table = Table(root, headers, List)
root.mainloop()
