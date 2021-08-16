import tkinter as tk
from tkinter import *
import praw

sub = ""
count = int()
oldcount = int()

class SeaofBTCapp(tk.Tk):

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


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter a Subreddit:")
        label.pack(pady=10, padx=10)
        E1 = Entry(self, bd=2)
        E1.pack()
        label = tk.Label(self, text="How Many Post Titles Should Be Shown (Enter an Integer):")
        label.pack(pady=10, padx=10)
        E2 = Entry(self, bd=2)
        E2.pack()
        button = tk.Button(self, text="Continue",
                           command=lambda: [setsub(), controller.show_frame(PageOne)])
        button.pack()
        def setsub():
            global sub
            global count
            sub = E1.get()
            count = int(E2.get())
            print(sub)
            print(count)







class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame2 = Frame(self)
        frame2.pack()
        bottomframe = Frame(self)
        bottomframe.pack(side=BOTTOM)



        button = tk.Button(self, text="Get Results",
                           command=lambda: [showresults()])
        button.pack()

        def showresults():
            label = tk.Label(self, text = "Showing Results From " + sub + ":", font = ("Impact", 20))
            label.pack()
            for submission in reddit.subreddit(sub).top("all", limit=count):
                label2 = tk.Label(self, text=submission.title)
                label2.pack(pady=10, padx=10)
                print(submission.title)
                button1.pack(side=BOTTOM)

        label2 = tk.Label(self, text="")
        label2.pack()

        button1 = tk.Button(self, text="Choose a Different Sub",
                            command=lambda: [controller.show_frame(StartPage), setold()])
        button1.pack(side=BOTTOM)

        def setold():
            global oldcount
            oldcount = count


reddit = praw.Reddit(
    client_id="7yMi_lww1mUJvQ",
    client_secret="SbRGpMHcJIhiJbpR6Swb5hoHVQAHEg",
    user_agent="python reddit test by u/kaizx1237"
)
reddit.read_only = True

app = SeaofBTCapp()


app.mainloop()
