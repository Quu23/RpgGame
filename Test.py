import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispImage(path):
    newImage = PIL.Image.open(path).resize((50,50))
    imgData =PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imgData)
    imageLabel.image = imgData

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispImage(fpath)

#GUIテスト
root = tk.Tk()
imageLabel=tk.Label()
btn = tk.Button(text="test",command= openFile)
btn.pack()
imageLabel.pack()
root.geometry("200x100")
tk.mainloop()

