from customtkinter import *

def report():
    print('Report')
    
def incident():
    print('Incident')

def donate():
    print('Donate')

def resource():
    print('Resources')


window = CTk()

mainFrame = CTkFrame(window)
mainFrame.pack(padx = 20, pady = 20)

titleField = CTkLabel(mainFrame, text = "Natural Disaster Management", width = 100, font=CTkFont(size=25, weight="bold"))
titleField.grid(padx = 10, pady = (25, 10), row = 0, column = 0, columnspan=2)

reportBtn = CTkButton(mainFrame, text = "Report Natural Disaster", command=report, width=150, height=50)
reportBtn.grid(padx = 30, pady = 20, row = 1, column = 0)

reportBtn = CTkButton(mainFrame, text = "View Incident Log", command=incident, width=150, height=50)
reportBtn.grid(padx = 30, pady = 20, row = 1, column = 1)

reportBtn = CTkButton(mainFrame, text = "Donate Resources", command=donate, width=150, height=50)
reportBtn.grid(padx = 30, pady = (15, 30), row = 2, column = 0)

reportBtn = CTkButton(mainFrame, text = "Check Resource Availability", command=resource, width=150, height=50)
reportBtn.grid(padx = 30, pady = (15, 30), row = 2, column = 1)

window.mainloop()