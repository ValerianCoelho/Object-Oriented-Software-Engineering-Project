import sqlite3
from customtkinter import *
import datetime

connect = sqlite3.connect('Natural_Disaster_Management.db')
cursor = connect.cursor()
currentTime = datetime.datetime.now()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Table:
    def __init__(self, root, Headers, Entries):
        rows = len(Entries)
        cols = len(Entries[0])
        for i in range(cols):
            self.e = CTkButton(root, text=Headers[i], width=180)
            self.e.grid(row=1, column=i, padx=2, pady=2)
            
        for i in range(rows):
            for j in range(cols):
                self.e = CTkEntry(root, justify='center', width=180)
                self.e.grid(row = i+2, column = j, padx=2, pady=2)
                self.e.insert(END, Entries[i][j])
                self.e.configure(state='disabled')

def report():
    def submitReport():
        disasterType = disasterTypeInput.get()
        disasterLocation = disasterLocationInput.get()
        disasterMagnitude = disasterMagnitudeInput.get()
        year = currentTime.year
        month = months[currentTime.month-1]
        day = currentTime.day

        cursor.execute(f"""INSERT INTO disaster (Type, Location, Severity, Year, Month, Day)
                           VALUES ('{disasterType}', '{disasterLocation}', '{disasterMagnitude}', {year}, '{month}', {day});
                        """)
        connect.commit()
        reportFrame.pack_forget()
        homeFrame.pack(padx = 20, pady = 20)

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
    def back():
        incidentFrame.pack_forget()
        homeFrame.pack(padx = 20, pady = 20)

    cursor.execute("SELECT * FROM disaster")
    homeFrame.pack_forget()

    incidentFrame = CTkFrame(window)
    incidentFrame.pack(padx = 20, pady = 20)

    disasterField = CTkLabel(incidentFrame, text = "Natural Disasters", font=CTkFont(size=15, weight="bold"))
    disasterField.grid(padx = 10, pady = 10, row = 0, column = 0, columnspan=7)

    table = Table(incidentFrame, ['ID', 'Type', 'Location', 'Severity', 'Year', 'Month', 'Day'], cursor.fetchall())

    backBtn = CTkButton(incidentFrame, text = "Back", command=back)
    backBtn.grid(padx = 10, pady = 10, columnspan=7)

def donate():
    def submitDonate():
        name = nameInput.get()
        email = emailInput.get()
        amount = amountInput.get()
        country = countryInput.get()

        cursor.execute(f"""INSERT INTO donations (Name, Email, Amount, Country)
                           VALUES ('{name}', '{email}', {amount}, '{country}');
                        """)
        connect.commit()

        donateFrame.pack_forget()
        homeFrame.pack(padx = 20, pady = 20)

    homeFrame.pack_forget()

    donateFrame = CTkFrame(window)
    donateFrame.pack(padx = 20, pady = 20)

    donateField = CTkLabel(donateFrame, text = "Support Disaster Victims", font=CTkFont(size=15, weight="bold"))
    donateField.grid(padx = 10, pady = 10, row = 0, column = 0, columnspan=2)

    nameField = CTkLabel(donateFrame, text = "Name: ")
    nameField.grid(padx = 10, pady = 10, row = 1, column = 0)

    nameInput = CTkEntry(donateFrame, placeholder_text = "John Doe", width=200)
    nameInput.grid(padx = 10, pady = 10, row = 1, column = 1)

    emailField = CTkLabel(donateFrame, text = "Email: ")
    emailField.grid(padx = 10, pady = 10, row = 2, column = 0)

    emailInput = CTkEntry(donateFrame, placeholder_text = "johndoe@example.com", width=200)
    emailInput.grid(padx = 10, pady = 10, row = 2, column = 1)

    amountField = CTkLabel(donateFrame, text = "Amount: ")
    amountField.grid(padx = 10, pady = 10, row = 3, column = 0)

    amountInput = CTkEntry(donateFrame, placeholder_text = "$20", width=200)
    amountInput.grid(padx = 10, pady = 10, row = 3, column = 1)

    countryField = CTkLabel(donateFrame, text = "Country: ")
    countryField.grid(padx = 10, pady = 10, row = 4, column = 0)

    countryInput = CTkEntry(donateFrame, placeholder_text = "India", width=200)
    countryInput.grid(padx = 10, pady = 10, row = 4, column = 1)

    submitDonateBtn = CTkButton(donateFrame, text = "Donate", command=submitDonate)
    submitDonateBtn.grid(padx = 10, pady = 10, row = 5, column = 0, columnspan=2)

def donations():
    def back():
        donationsFrame.pack_forget()
        homeFrame.pack(padx = 20, pady = 20)

    cursor.execute("SELECT * FROM donations")
    homeFrame.pack_forget()

    donationsFrame = CTkFrame(window)
    donationsFrame.pack(padx = 20, pady = 20)

    disasterField = CTkLabel(donationsFrame, text = "Donations", font=CTkFont(size=15, weight="bold"))
    disasterField.grid(padx = 10, pady = 10, row = 0, column = 0, columnspan=5)

    table = Table(donationsFrame, ['ID', 'Name', 'Email', 'Amount', 'Country'], cursor.fetchall())

    backBtn = CTkButton(donationsFrame, text = "Back", command=back)
    backBtn.grid(padx = 10, pady = 10, columnspan=5)


window = CTk()

homeFrame = CTkFrame(window)
homeFrame.pack(padx = 20, pady = 20)

titleField = CTkLabel(homeFrame, text = "Natural Disaster Management", font=CTkFont(size=25, weight="bold"))
titleField.grid(padx = 10, pady = (25, 10), row = 0, column = 0, columnspan=2)

reportBtn = CTkButton(homeFrame, text = "Report Natural Disaster", command=report, width=150, height=50)
reportBtn.grid(padx = (30, 10), pady = 20, row = 1, column = 0)

incidentBtn = CTkButton(homeFrame, text = "View Incident Log", command=incident, width=150, height=50)
incidentBtn.grid(padx = (10, 30), pady = 20, row = 1, column = 1)

donateBtn = CTkButton(homeFrame, text = "Donate Resources", command=donate, width=150, height=50)
donateBtn.grid(padx = (30, 10), pady = (15, 30), row = 2, column = 0)

resourceBtn = CTkButton(homeFrame, text = "Check Resource Availability", command=donations, width=150, height=50)
resourceBtn.grid(padx = (10, 30), pady = (15, 30), row = 2, column = 1)

window.mainloop()
