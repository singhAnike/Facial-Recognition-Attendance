
from SourceCode import *
from tkinter import *
from os import *
from PIL import ImageTk, Image
import webbrowser
from tkinter import filedialog as fd
# from PIL import ImageTk, Image
# GUI Implementation for Automatted Attendance System
win = Tk()

width = win.winfo_screenwidth()
height = win.winfo_screenheight()

# Fix tkinter window size
win.geometry("%dx%d" % (width, height))

# Set Background Image
# win.geometry("700x450")
# Open the Image File
bg = ImageTk.PhotoImage(file="Backg-images/face-recognition.jpg")

# Create a Canvas
canvas = Canvas(win, width=750, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window


def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("Backg-images/face-recognition.jpg")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')

    # welcome
    canvas_id = canvas.create_text(100, 250, anchor="nw")
    canvas.itemconfig(
        canvas_id, text="Welcome To The Automated Attendance System\n\nLet's gets Started"*1, width=780,)
    canvas.itemconfig(canvas_id, font=("courier", 16), fill='#4343CD')
    canvas.insert(canvas_id, 16, "")

    # heding
    canvas_h = canvas.create_text(300, 50, anchor="nw")
    canvas.itemconfig(
        canvas_h, text="Face-Recogination Automated Attendance System"*1, width=800)
    canvas.itemconfig(canvas_h, font=(
        "Times New Roman bold", 25), fill='#BCBC8F')
    canvas.insert(canvas_h, 16, "")


# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)
# Title of this application
win.title("Automated Attendance System")
# # Hadder of this application
# label=Label(win, text="Welcome To The Real-Time Automated Attendance System", font=("Times New Roman",20),bg="white",fg="Blue")
# label.pack(pady=15)

# Add text
canvas.create_text(200, 250, text="Welcome")
# Creating buttons
# Creating The Button For Taking Attendace
button1 = Button(win, text="Take Attendance",
                 command=TakeAttendance, bg='DodgerBlue4', fg='white', height='2', width='15', border='5', font=("Times New Roman", 11))
button1.pack(pady='10')

# Creating The Button To show Attendance
button2 = Button(win, bg="DodgerBlue4", fg="white", text="View Attendance",
                 command=showAttendance, height='2', width='15', border='5', font=("Times New Roman", 11))
button2.pack(pady='10')


# New student registration function
def new_registration():
    file=fd.askopenfilename(initialdir="C:/Users/immra/OneDrive/Pictures")
    fob=read(file,'r')
    
    # print("hello my name is aniket singh from oriental univrsity indore")
# Button for Add new student
button3 = Button(win, bg="DodgerBlue4", fg="white", text="Click to register a new student",
                 border='5', height='2', width='25', font=("Times New Roman", 11),command=lambda:new_registration())
button3.pack()

#Function defination
def Help():
    webbrowser.open("https://forms.gle/NkFb5ASxxyZSvM426")

# Button for Help 
button4 = Button(win, bg="DodgerBlue4", fg="white", text="Get Help",
                 height='2', width='8', border='5', font=("Times New Roman", 11),command=Help)
button4.pack()


def exit():
    win.destroy()


# Button for Exit From window
button5 = Button(win, bg="DodgerBlue4", fg="white", text="Exit", height='2',
                 width='8', border='5', command=exit, font=("Times New Roman", 11))
button5.pack()

# Display image
canvas.create_image(0, 0, image=bg,
                    anchor="nw")

# Display Buttons
button1_canvas = canvas.create_window(100, 550,
                                      anchor="nw",
                                      window=button1)

button2_canvas = canvas.create_window(300, 550,
                                      anchor="nw",
                                      window=button2)

button3_canvas = canvas.create_window(680, 550, anchor="nw",
                                      window=button3)

button4_canvas = canvas.create_window(950, 550, anchor="nw",
                                      window=button4)

button5_canvas = canvas.create_window(1100, 550, anchor="nw",
                                      window=button5)

# put on screen
win.mainloop()
