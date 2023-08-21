from tkinter import *
from tkinter import ttk


def main():
    w = Tk()
    w.geometry("1000x500")
    heading = "Lodo List"

    m = Label(w, text=heading, font=("Arial", 14))

    m.place(x=20, y=20)

    l1 = Label(w, text="Add Items", font=("Arial", 14), fg="blue")
    e1 = Entry(w, font=("Arial", 20), fg="blue", width=15)
    e1.place(x=20, y=100)

    l1.place(x=20, y=60)

    def Edit():
        pass

    def Delete():
        pass

    def submit():
        content = e1.get()

        l2 = Label(w, text=content, font=("Arial", 14))
        l2.pack(padx=10, pady=20)

        b2 = Button(w, text="Edit", font=("Arial", 10), fg="blue", command=Edit
                    )
        b2.place(x=220, y=180)
        b3 = Button(w, text="Delete", font=("Arial", 10), fg="blue", command=Delete
                    )
        b3.place(x=270, y=180)

        l2.place(x=20, y=180)

    b1 = Button(w, text="submit", font=("Arial", 14), fg="blue", command=submit
                )
    b1.place(x=260, y=97)

    x = Label(w, text="tasks", font=("Arial", 14))

    x.pack()
    x.place(x=20, y=150)
    w.mainloop()


main()
