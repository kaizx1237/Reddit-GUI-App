# Reddit GUI Application designed and programmed by Tarun Giridhar


# imports important libraries, such as the reddit api
import tkinter as tk
from tkinter import *
import praw
import webbrowser
import time

# Declares variables that keep track of the subreddit, posts, and time
sub = ""
sort = ""
by = ""
count = int()
seco = None
minu = None
hours = None
check1 = 0

# Defines the GUI Window for the application using tkinter
class redditgui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Creates the Starting Page of the app, including the labels and buttons that show on screen
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        menuFrame = Frame(self)
        timerFrame = Frame(self)
        label = tk.Label(self, text="Enter a Subreddit:")
        label.pack(pady=10, padx=10)
        E1 = Entry(self, bd=2)
        E1.pack()
        label = tk.Label(self, text="How Many Posts Should Be Shown (Enter an Integer):")
        label.pack(pady=10, padx=10)
        E2 = Entry(self, bd=2)
        E2.pack()
        mb1 = Menubutton(self, text="Choose sort method", bg='#0052cc', fg='#ffffff', font="Helvetica 10 bold")
        m1 = Menu(mb1, tearoff=0)
        mb2 = Menubutton(self, text="Choose Time Period", bg='#0052cc', fg='#ffffff', font="Helvetica 10 bold")

        # Sets the filter type chosen by the user to the variables "sort" and "by"
        def setFilter():
            global sort
            global by

            if b1.get() == "Top":
                sort = "Top"
                print("top test")
            elif b1.get() == "Best":
                sort = "Best"
                print("best test")
            elif b1.get() == "Hot":
                sort = "Hot"
                print("hot test")
            elif b1.get() == "New":
                sort = "New"
                print("new test")
            elif b1.get() == "Rising":
                sort = "Rising"
                print("rising test")

            if b2.get() == "all":
                by = "all"
                print("all test")

            elif b2.get() == "year":
                by = "year"
                print("year test")

            elif b2.get() == "month":
                by = "month"
                print("month test")

            elif b2.get() == "week":
                by = "week"
                print("week test")

            elif b2.get() == "day":
                by = "day"
                print("day test")

            elif b2.get() == "hour":
                by = "hour"
                print("Hour test")

        # Creates the dropdown menu options that the user selects to choose the filter type
        b1 = StringVar()
        b2 = StringVar()

        m1.add_radiobutton(label="Top", variable=b1, value="Top")
        m1.add_radiobutton(label="Best", variable=b1, value="Best")
        m1.add_radiobutton(label="Hot", variable=b1, value="Hot")
        m1.add_radiobutton(label="New", variable=b1, value="New")
        m1.add_radiobutton(label="Rising", variable=b1, value="Rising")
        mb1["menu"] = m1

        m2 = Menu(mb2, tearoff=0)
        m2.add_radiobutton(label="All Time", variable=b2, value="all")
        m2.add_radiobutton(label="Year", variable=b2, value="year")
        m2.add_radiobutton(label="Month", variable=b2, value="month")
        m2.add_radiobutton(label="Week", variable=b2, value="week")
        m2.add_radiobutton(label="Day", variable=b2, value="day")
        m2.add_radiobutton(label="Hour", variable=b2, value="hour")
        mb2["menu"] = m2

        menuFrame.pack(expand=True)
        mb1.pack(in_=menuFrame, padx=10, side=LEFT)
        mb2.pack(in_=menuFrame, padx=10, side=RIGHT)

        # Creates a checkbox for if the user wants to set a refresh timer
        check = IntVar()
        c1 = tk.Checkbutton(self, text='Set a refresh timer?', variable=check, onvalue=1, offvalue=0, font="Helvetica 10 bold")
        c1.pack()

        sec = StringVar()
        mins = StringVar()
        hrs = StringVar()

        timerFrame.pack(expand=True)

        # storing seconds
        E3 = Entry(self, textvariable=sec, width=2, font='arial 12')
        sec.set('00')
        E3.pack(in_=timerFrame, padx=2, side=RIGHT)

        # storing minutes
        E4 = Entry(self, textvariable=mins, width=2, font='arial 12')
        mins.set('00')
        E4.pack(in_=timerFrame, padx=2, side=RIGHT)

        # storing hours
        E5 = Entry(self, textvariable=hrs, width=2, font='arial 12')
        hrs.set('00')
        E5.pack(in_=timerFrame, padx=2, side=LEFT)

        button = tk.Button(self, text="Continue", bg='#0052cc', fg='#ffffff', font="Helvetica 12 bold",
                           command=lambda: [setsub(), controller.show_frame(PageOne)])
        button.pack(side=BOTTOM)

        # Sets the subreddit and amount of posts that the user chooses
        def setsub():
            global sub
            global count
            sub = E1.get()
            count = int(E2.get())
            global seco
            seco = sec
            global minu
            minu = mins
            global hours
            hours = hrs
            global check1
            check1 = check.get()
            setFilter()
            print(sub)
            print(count)
            print(sort)
            print(by)
            print(b1.get())
            print(b2.get())
            print(check.get())
            print(seco.get())
            print(seco)

# Creates Page One of the app, which is where the posts and countdown timer are shown
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame2 = Frame(self)
        frame2.pack()
        hStack = Frame(self)
        vStack = Frame(self)
        timerFrame = Frame(self)
        bottomframe = Frame(self)
        bottomframe.pack(side=BOTTOM)

        hStack.pack(expand=True)
        startButton = tk.Button(self, text="Start Timer", bg='#0052cc', fg='#ffffff', font="Helvetica 9 bold",
                                command=lambda: [startTimer()])

        startButton.pack(in_=hStack, padx=5, side=LEFT)

        vStack.pack(in_=hStack, expand=True, padx=3, side=RIGHT)
        label1 = tk.Label(self, text="Timer:", font="Helvetica 12 bold")
        label1.pack(in_=vStack, pady=5)

        # storing seconds
        timerFrame.pack(in_=vStack, expand=True, pady=5)

        E6 = Entry(self, textvariable=seco, width=2, font='arial 12')

        E6.pack(in_=timerFrame, padx=2, side=RIGHT)

        # storing minutes
        E7 = Entry(self, textvariable=minu, width=2, font='arial 12')

        E7.pack(in_=timerFrame, padx=2, side=RIGHT)

        # storing hours
        E8 = Entry(self, textvariable=hours, width=2, font='arial 12')

        E8.pack(in_=timerFrame, padx=2, side=LEFT)

        # Starts the countdown timer when the start button is pressed, and refreshes the page after the timer completes
        def startTimer():
            global seco
            global minu
            global hours
            times = int(hours.get()) * 3600 + int(minu.get()) * 60 + int(seco.get())
            print(check1)
            while check1 == 1:
                times1 = times
                while times1 > -1:
                    minute, second = (times1 // 60, times1 % 60)

                    hour = 0
                    if minute > 60:
                        hour, minute = (minute // 60, minute % 60)

                    E6.delete(0, END)
                    E6.insert(0, second)
                    E7.delete(0, END)
                    E7.insert(0, minute)
                    E8.delete(0, END)
                    E8.insert(0, hour)

                    self.update()
                    time.sleep(1)

                    if (times == 0):
                        seco.set('00')
                        minu.set('00')
                        hours.set('00')
                    times1 -= 1
                showresults()

        button = tk.Button(self, text="Get Results", bg='#0052cc', fg='#ffffff', font="Helvetica 12 bold",
                           command=lambda: [showresults()])
        button.pack()

        # Obtains posts from reddit by following the filters the user chose on the Start Page
        def showresults():
            label = tk.Label(self, text="Showing Results From " + sub + ":", font=("Impact", 15))
            label.pack()

            buttons = []
            if sort == "Top":
                for submission in reddit.subreddit(sub).top(by, limit=count):
                    button2 = tk.Button(self, text=submission.title, command=lambda j=submission.url: onclick(j))
                    button2.pack(pady=10, padx=10)
                    buttons.append(button2)
                    button1.pack(side=BOTTOM)
            elif sort == "Best":
                for submission in reddit.subreddit(sub).best(limit=count):
                    button2 = tk.Button(self, text=submission.title, command=lambda j=submission.url: onclick(j))
                    button2.pack(pady=10, padx=10)
                    buttons.append(button2)
                    button1.pack(side=BOTTOM)
            elif sort == "Hot":
                for submission in reddit.subreddit(sub).hot(limit=count):
                    button2 = tk.Button(self, text=submission.title, command=lambda j=submission.url: onclick(j))
                    button2.pack(pady=10, padx=10)
                    buttons.append(button2)
                    button1.pack(side=BOTTOM)
            elif sort == "New":
                for submission in reddit.subreddit(sub).new(limit=count):
                    button2 = tk.Button(self, text=submission.title, command=lambda j=submission.url: onclick(j))
                    button2.pack(pady=10, padx=10)
                    buttons.append(button2)
                    button1.pack(side=BOTTOM)
            elif sort == "Rising":
                for submission in reddit.subreddit(sub).rising(limit=count):
                    button2 = tk.Button(self, text=submission.title, command=lambda j=submission.url: onclick(j))
                    button2.pack(pady=10, padx=10)
                    buttons.append(button2)
                    button1.pack(side=BOTTOM)
            else:
                for submission in reddit.subreddit(sub).top("all", limit=count):
                    button2 = tk.Button(self, text=submission.title, command=lambda j=submission.url: onclick(j))
                    button2.pack(pady=10, padx=10)
                    buttons.append(button2)
                    button1.pack(side=BOTTOM)

            def onclick(j):
                webbrowser.open(j, new=2)

        label2 = tk.Label(self, text="")
        label2.pack()

        button1 = tk.Button(self, text="Choose a Different Sub", bg='#0052cc', fg='#ffffff', font="Helvetica 12 bold",
                            command=lambda: [controller.show_frame(StartPage)])
        button1.pack(side=BOTTOM)

# Authenticates the app to reddit using my credentials, have to remove before uploading to GitHub
reddit = praw.Reddit(
    client_id=" My Client ID goes here, but it and the client secret are sensetive information that must be removed",
    client_secret="Have to remove ID and secret as it gains access to my reddit account",
    # Placeholder name of the application
    user_agent="python reddit test by u/kaizx1237"
)

# Sets the app to read only mode
reddit.read_only = True

# Runs the Graphical Interface
app = redditgui()

app.mainloop()
