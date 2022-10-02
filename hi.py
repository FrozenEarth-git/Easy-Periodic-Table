from tkinter import *
import random

window = Tk()
window.geometry("600x400")
window.title("Workout History")

def initializeWindowLayout():
    global history_labelFrame
    global flavor_labelFrame
    global scrollBar
    global canvas
    global secondFrame
    
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=0)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=0)
    
    history_labelFrame = LabelFrame(window, text="Workout History")
    history_labelFrame.grid(row=0, column=0, padx=8, pady=5, sticky="nsew")
    
    flavor_labelFrame = LabelFrame(window, text="Message of the Refresh")
    flavor_labelFrame.grid(row=1, column=0, padx=8, pady=(0, 5), sticky="nsew")
    
    
    Label(flavor_labelFrame, text= getRandomFlavor() ).pack(anchor="w", padx=10)
    
    reverseSortButton = Button(history_labelFrame, text="Sort Oldest/Newest", command=reverseSort)
    reverseSortButton.pack()
    
    canvas = Canvas(history_labelFrame)
    canvas.pack(side = LEFT, fill = BOTH, expand = True)
    
    scrollBar = Scrollbar(history_labelFrame, orient=VERTICAL, command=canvas.yview)
    scrollBar.pack(side = RIGHT, fill = Y)
    
    canvas.configure(yscrollcommand = scrollBar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    
    secondFrame = Frame(canvas)
    canvas.create_window((0,0), window=secondFrame, anchor="nw")


def populateHistory(w_history):
    
    secondFrame.columnconfigure(3, weight=10)
    
    Label(secondFrame, text="Date").grid(row=0, column=0, sticky="EW")
    Label(secondFrame, text="Name").grid(row=0, column=1, sticky="EW")
    Label(secondFrame, text="Duration").grid(row=0, column=2, sticky="EW")
    Label(secondFrame, text="Exercises").grid(row=0, column=3, sticky="EW")
    
    i = 1
    for workout in workout_history:
        Label(secondFrame, text=workout["date"]).grid(row=i, column=0, padx=5, pady=5)
        Label(secondFrame, text=f"{workout['duration']} minutes").grid(row=i, column=2, padx=5, pady=5)
        
        exercises = ""
        for exercise in workout["exercises"]:
            if isinstance(exercise, str):
                Label(secondFrame, text=exercise).grid(row=i, column=1, padx=5, pady=5)
                continue;
                
            else:
                exercises += f"{exercise[0]} (Reps: {exercise[1]}, Sets: {exercise[2]})\n"
        else:
            exercises = exercises[0:-1]
        exercisesLabel = Label(secondFrame, text=exercises)
        exercisesLabel.grid(row=i, column=3, padx=5)
        i += 1

def reverseSort():
    for widget in window.winfo_children():
        widget.destroy()
    initializeWindowLayout()
    populateHistory(workout_history.reverse())
    
def getRandomFlavor():
    flavorTexts = [
        "Keep up the good work!",
        "You exercised!",
        "Being healthy is good!",
        "IP: 124.105.6.187",
        "So cool!",
        "You rock!",
        ]
    return random.choice(flavorTexts)
        
workout_history = [ 
    {"exercises": [ "Short Workout", ["Push Ups", 8, 4] ], "duration": 10, "date": "September 16, 2022"},
    {"exercises": [ "Short Workout", ["Push Ups", 8, 4] ], "duration": 10, "date": "September 22, 2022"},
    {"exercises": [ "Impromptu Workout", ["Squats", 15, 2] ], "duration": 15, "date": "September 28, 2022"},
    {"exercises": [ "Regular Workout", ["Push Ups", 10, 3], ["1-Minute Plank", 5, 2], ["Half-Mile Jog", 1, 1]], "duration": 25, "date": "September 30, 2022"},
    {"exercises": [ "Short Workout", ["Push Ups", 8, 4] ], "duration": 10, "date": "October 1, 2022"},
    {"exercises": [ "Crunch Time", ["Crunches", 20, 5], ["Crunches", 10, 5] ], "duration": 40, "date": "October 2, 2022"} 
    ]
    
initializeWindowLayout()
populateHistory(workout_history)
window.mainloop()
