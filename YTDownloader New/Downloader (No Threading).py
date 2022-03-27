# Tkinter will be used
# Image Logo
# Some extra stuff to choose resolution
# I'm gonna be working in this one whereas I learn CSS and HTML once again


from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
from Functions import *
from pytube import *
from tkinter import filedialog
import datetime



# MainWindow
root = Tk()

mainCanvas = Canvas(root, width=720, height=480, bg="white")
mainCanvas.pack()

# progressbar function
# ProgressBarWindow




""" def progressBar():
    secondWindow = Toplevel(root)
    secondWindow.geometry("300x300")
    secondWindow.title("Progress Bar")

def destroyBar():
    secondWindow = Toplevel(root)
    secondWindow.geometry("300x300")
    secondWindow.title("Progress Bar")
    secondWindow.destroy() """


    

# functions
def download():
    url = inputField.get()
    print(url.find)
    if url == "":
        messagebox.showinfo(
            "Warning!", message="Please insert a valid YouTube URL!")

    else:
        yt = YouTube(url)
        if YouTube.check_availability != None:
            ytSeconds = yt.length
            ytMinutes = str(datetime.timedelta(seconds=ytSeconds))
            exportFilePath = filedialog.asksaveasfile(title="Select Folder", filetypes=[("mp4 Video File", ".mp4")])
                      
            

            if exportFilePath == None:
                messagebox.showinfo(
                    "Warning!", message="You should specific a valid directory and a file name of your preference, otherwise the program won't run!")

            else:
                try:
                    print(f"The title of your videos is: {yt.title}")
                    print(f"The lenght of your video is: {ytMinutes}")
                    """ progressBar() """
                    video = yt.streams.get_highest_resolution()
                    video.download(exportFilePath)
                    messagebox.showinfo("Congratulations",
                                        message="Successfully downloaded!")

                except:
                    messagebox.showinfo(
                        message="Something went wrong, check your network connection!")
                    """ destroyBar() """


def closing():
    messagebox.askquestion(
        "Exit application", "Are you sure you want to exit?")
    if messagebox.askquestion == "yes":
        root.destroy()
        print("Proccess finished")


inputField = Entry(root, width=50, background="#F5F5F5", borderwidth=0)
mainCanvas.create_window(350, 310, window=inputField)


logo = Image.open("Logo.png")
logo = ImageTk.PhotoImage(logo)
photoConvert = PhotoImage(file=r"convert3.png")
mainCanvas.create_image(0, -20, anchor=NW, image=logo)

converterFont = font.Font(family="Times New Roman", size=8)

converterText = Label(root, text="Download", borderwidth=0,
                      foreground="black", bg="white", font=converterFont)
converterText.pack()
converterText.place(x=535, y=302)

convertBtn = Button(root, image=photoConvert, bd=0,
                    borderwidth=0, command=download, highlightthickness=0)
convertBtn.place(x=510, y=300)
convertBtn.config()

""" exitImage = PhotoImage(file=r"Exit.png")
destroyButton = Button(root,command=closing, text="Exit", image=exitImage, borderwidth=0, highlightthickness=0, bd=0)
destroyButton.place(x= 600, y=0)  
 """


root.mainloop()

#
