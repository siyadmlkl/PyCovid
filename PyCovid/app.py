import tkinter as tk
import requests


def formatData(cases):
    try:
        total_cases = cases['cases']
        today_cases = cases['todayCases']
        active = cases['active']
        today_recovered = cases['todayRecovered']
        today_death = cases['todayDeaths']
        population = cases['population']
        case_per_million = cases['casesPerOneMillion']
        one_case_per = cases['oneCasePerPeople']
        death_per_people = cases['oneDeathPerPeople']
        text1 = 'Total Cases\t\t: %s\nToday Cases\t: %s\nActive Cases\t: %s\nTodays Recovered\t: %s\nToday Death\t: %s' % (
            total_cases, today_cases, active, today_recovered, today_death)
        text2 = '\n\nTotal Population\t: %s\nCases Per Million\t: %s\nCase/No. of People\t: %s\nDeath/No.of People\t: %s' % (
            population, case_per_million, one_case_per, death_per_people)
        formatted_text = text1+text2
    except:
        formatted_text = 'Invalid Entry....'
    return formatted_text


def enterEntry(event):
    getData(entry.get())


def getData(country):
    url = 'https://disease.sh/v3/covid-19/countries/' + country
    cases = requests.get(url).json()
    label.config(text=formatData(cases))


root = tk.Tk()
root.title = 'Corona Tracker'

canvas = tk.Canvas(root, height=600, width=400)
canvas.pack()

font = ('Berlin Sans FB', 15)

entry = tk.Entry(canvas, bg='white', font=font)
entry.place(relheight=0.05, relwidth=0.5, relx=0.1, rely=0.1)
entry.bind('<Return>', enterEntry)
entry.focus()

button = tk.Button(canvas, text='Fetch', font=font,
                   command=lambda: getData(entry.get()))
button.place(relheight=0.05, relwidth=0.3, relx=0.6, rely=0.1)


label = tk.Label(canvas, bg='white', fg='#000080',
                 font=font, anchor='nw', justify='left', padx=10, pady=5)
label.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.25)


root.mainloop()
