# Tkinter will be used
# Image Logo
# Some extra stuff to choose resolution
# I'm gonna be working in this one whereas I learn CSS and HTML once again


from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
from pytube import *
from tkinter import filedialog
import datetime
import threading



# MainWindow
root = Tk()
root.title("YTDownloader")


mainCanvas = Canvas(root, width=720, height=480, bg="white")
mainCanvas.pack()

# progressbar function
# ProgressBarWindow

yt = None


def downloadCallback(stream, chunk, file_handle, bytes_remaining):
    fileSize = yt.streams.get_highest_resolution().filesize
    bytes_downloaded = fileSize - bytes_remaining
    percentage = round((bytes_downloaded / fileSize) * 100, 2)
    print(f"{percentage}% Downloaded", end="\r")



# functions


def download():
    url = inputField.get()
    

    if url == "":
        messagebox.showinfo(
            "Warning!", message="Please insert a valid YouTube URL!")

    else:
        yt = YouTube(url, on_progress_callback=downloadCallback)

        if YouTube.check_availability != None:
            ytSeconds = yt.length
            ytMinutes = str(datetime.timedelta(seconds=ytSeconds))
            exportFilePath = filedialog.asksaveasfilename(
                initialfile = yt.title, title="Save your file", filetypes=[("Video Files", "*.mp4")])

            if exportFilePath == "":
                messagebox.showinfo(
                    "Warning!", message="You should specific a valid directory!")
            else:
                
                try:
                    print(f"The title of your video is: {yt.title}")
                    print(f"The author of your video is: {yt.author}")
                    print(f"The number of views of  your video is: {yt.views}")
                    print(f"The lenght of your video is: {ytMinutes}")
                    

                    video = yt.streams.get_highest_resolution()
                    
                
                    print(video)
                    """  video.download(exportFilePath) """
                    print("Download finished!")
                    messagebox.showinfo("Congratulations",
                                        message="Successfully downloaded!")
                except:
                    messagebox.showinfo(
                        "Error", message="Something went wrong, check your network connection!")


""" def closing():
    messagebox.askquestion(
        "Exit application", "Are you sure you want to exit?")
    exit


    if messagebox.askquestion == "yes":
        root.destroy()
        print("Proccess finished")
        quit()
     """

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
                    borderwidth=0, highlightthickness=0, command=lambda: threading.Thread(target=download).start())


convertBtn.place(x=510, y=300)
convertBtn.config()

""" exitImage = PhotoImage(file=r"Exit.png")
destroyButton = Button(root,command=closing, text="Exit", image=exitImage, borderwidth=0, highlightthickness=0, bd=0)
destroyButton.place(x= 600, y=0)  
 """


root.mainloop()

#
