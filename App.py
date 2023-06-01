from customtkinter import *

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

def report():
    def submitReport():
        pass

    homeFrame.pack_forget()

    reportFrame = CTkFrame(window)
    reportFrame.pack(padx = 20, pady = 20)

    reportField = CTkLabel(reportFrame, text = "Report Natural Disaster", font=CTkFont(size=15, weight="bold"))
    reportField.grid(padx = 10, pady = 10, row = 0, column = 0, columnspan=2)

    disasterTypeField = CTkLabel(reportFrame, text = "Natural Disaster Type: ")
    disasterTypeField.grid(padx = 10, pady = 10, row = 1, column = 0)

    disasterTypeInput = CTkEntry(reportFrame, placeholder_text = "Earthquake", width=200)
    disasterTypeInput.grid(padx = 10, pady = 10, row = 1, column = 1)

    disasterLocationField = CTkLabel(reportFrame, text = "Natural Disaster Location: ")
    disasterLocationField.grid(padx = 10, pady = 10, row = 2, column = 0)

    disasterLocationInput = CTkEntry(reportFrame, placeholder_text = "Japan", width=200)
    disasterLocationInput.grid(padx = 10, pady = 10, row = 2, column = 1)

    disasterMagnitudeField = CTkLabel(reportFrame, text = "Natural Disaster Severity: ")
    disasterMagnitudeField.grid(padx = 10, pady = 10, row = 3, column = 0)

    disasterMagnitudeInput = CTkEntry(reportFrame, placeholder_text = "Low, Moderate, High, Extreme", width=200)
    disasterMagnitudeInput.grid(padx = 10, pady = 10, row = 3, column = 1)

    submitReportBtn = CTkButton(reportFrame, text = "Submit Report", command=submitReport)
    submitReportBtn.grid(padx = 10, pady = 10, row = 4, column = 0, columnspan=2)
    
def incident():
    print('Incident')

def donate():
    print('Donate')

def donations():
    print('Resources')


window = CTk()

homeFrame = CTkFrame(window)
homeFrame.pack(padx = 20, pady = 20)

titleField = CTkLabel(homeFrame, text = "Natural Disaster Management", font=CTkFont(size=25, weight="bold"))
titleField.grid(padx = 10, pady = (25, 10), row = 0, column = 0, columnspan=2)

reportBtn = CTkButton(homeFrame, text = "Report Natural Disaster", command=report, width=150, height=50)
reportBtn.grid(padx = 30, pady = 20, row = 1, column = 0)

incidentBtn = CTkButton(homeFrame, text = "View Incident Log", command=incident, width=150, height=50)
incidentBtn.grid(padx = 30, pady = 20, row = 1, column = 1)

donateBtn = CTkButton(homeFrame, text = "Donate Resources", command=donate, width=150, height=50)
donateBtn.grid(padx = 30, pady = (15, 30), row = 2, column = 0)

resourceBtn = CTkButton(homeFrame, text = "Check Resource Availability", command=donations, width=150, height=50)
resourceBtn.grid(padx = 30, pady = (15, 30), row = 2, column = 1)

window.mainloop()