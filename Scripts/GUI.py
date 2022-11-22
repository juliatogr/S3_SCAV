from tkinter import *
from tkinter import ttk, StringVar
import subprocess as sp


def video_to_av1():
    sp.call(["ffmpeg",
             "-i", path.get(),
             "-c:v", "libaom-av1",
             "-crf", "30",
             "output.mkv"])
    print("converted to AV1")


def video_to_h265():
    sp.call(["ffmpeg",
             "-i", path.get(),
             "-c:v", "libx265",
             "-preset", "fast",
             "-c:a", "aac",
             "-b:a", "128k",
             "output.mkv"])
    print("converted to H265")


def video_to_vp8():
    sp.call(["ffmpeg",
             "-i", path.get(),
             "-c:v", "libvpx",
             "-b:v", "1M",
             "-c:a", "libvorbis",
             "output.webm"])
    print("converted to VP8")


def video_to_vp9():
    sp.call(["ffmpeg",
             "-i", path.get(),
             "-c:v", "libvpx-vp9",
             "-b:v", "1M",
             "output.webm"])
    print("converted to VP9")


def get_entry():
    print(ent.get())


root = Tk()
root.title("Seminar 3 - SCAV")
frm = ttk.Frame(root, padding=10)
frm.grid()

path = StringVar()

ttk.Label(frm, text="Introduce path to file").grid(column=0, row=0)
ent = ttk.Entry(frm, textvariable=path)
ent.grid(column=1, row=0)
ttk.Button(frm, text="Enter", command=get_entry).grid(column=2, row=0)

ttk.Label(frm, text="Convert to").grid(column=0, row=1)
ttk.Button(frm, text="AV1", command=video_to_av1)\
    .grid(column=1, row=1)
ttk.Button(frm, text="H265", command=video_to_h265)\
    .grid(column=2, row=1)
ttk.Button(frm, text="VP8", command=video_to_vp8)\
    .grid(column=3, row=1)
ttk.Button(frm, text="VP9", command=video_to_vp9)\
    .grid(column=4, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

root.mainloop()
