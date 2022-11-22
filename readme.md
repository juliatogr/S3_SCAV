# S3_SCAV

## Statement

1) Remember you have the BBB video converted into these? (If not, do it now!)
720p
480p
360x240
160x120

- Convert them into VP8, VP9, h265 & AV1. You can use the script that allows you to transform, or create a new script. If not, you can do it manually
- Try to create a new video as the one of the 4 videos at the same time we saw in class, and please analyze by yourself and comment how these codecs work at each bitrate

2) Once you did the last exercise. Let’s create a video converter program! You can use ‘tkinter’ or any other framework.
Create something ‘visual’ which has 4 buttons for each of the codecs mentioned below. When you click on them, there should be able to do conversion operations.

From here… you can fly whenever you want!
You just need to deliver something with a user interface that enables these conversions. Feel free to interpret this or add anything as you want!

## Comments

All videos from exercise 1 are located inside the `videos` folder, organised in different folders depending on its codec (VP8, VP9, h265 & AV1), or if they are the originals. The collages are inside the `collages`folder.

I created a GUI where you can write the path to the video (Ex. ./videos/originals/bbb_480x480.mp4) and choose the format you want to convert it selecting the corresponding button. The output file will be located at the main project folder, with the name "output.{extension}". The GUII looks like this:
<p align="center">
<img src=https://user-images.githubusercontent.com/72571435/203330869-a35851ee-488f-4921-842f-cd7b379f0b83.png width="120" height="120" />
</p>

Finally, if you want to quit the application, you can just press the "Quit" button.

To execute the GUI, please locate the Ubuntu terminal at the main project folder and execute `python3 ./Scripts/GUI.py"

I also included a script used for creating all collages. To execute it, `python3 ./Scripts/mix_videos.py`

## Observations from Exercise 1


## Util links

- *AV1 Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/AV1
- *H.265/HEVC Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/H.265
- *VP8 Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/VP8
- *VP9 Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/VP9
- *create a mosaic out of several input videos:* https://trac.ffmpeg.org/wiki/Create%20a%20mosaic%20out%20of%20several%20input%20videos
- *Botón (Button) en Tcl/Tk (tkinter):* https://recursospython.com/guias-y-manuales/boton-button-en-tkinter/
- *Entry Widgets in Tkinter:* https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
- *Getting a TKinter input stored into a string variable in the next function?:* https://stackoverflow.com/questions/26414868/getting-a-tkinter-input-stored-into-a-string-variable-in-the-next-function
