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

All videos from exercise 1 are located inside the `videos` folder, organised in different folders depending on its codec (VP8, VP9, h265 & AV1), or if they are the originals. The collages are inside the `collages`folder. Each collage has the next visualization:

- **upper-left:** H265
- **upper-right:** VP8
- **lower-left:** VP9
- **lower-right:** AV1

I created a GUI where you can write the path to the video (Ex. ./videos/originals/bbb_480x480.mp4) and choose the format you want to convert it selecting the corresponding button. The output file will be located at the main project folder, with the name "output.{extension}". The GUI looks like this:
<p align="center">
<img src=https://user-images.githubusercontent.com/72571435/203330869-a35851ee-488f-4921-842f-cd7b379f0b83.png />
</p>

Finally, if you want to quit the application, you can just press the "Quit" button.

To execute the GUI, please locate the Ubuntu terminal at the main project folder and execute `python3 ./Scripts/GUI.py"

I also included a script used for creating all collages. To execute it, `python3 ./Scripts/mix_videos.py`

## Observations from Exercise 1

I got the next sizes on the files:

| resolution | Original | H265 | VP8 | VP9 | AV1 |
| --- | --- | --- | --- | --- | --- |
| 160x120| 330 KB | 274 KB | 744 KB | 1.181 KB | 218 KB |
| 360x240 | 516 KB | 346 KB | 1.536 KB | 1.197 KB | 320 KB |
| 480x480| 865 KB | 483 KB | 1.555 KB | 1.516 KB | 512 KB |
| 720x720 | 1.599 KB | 753 KB | 1.536 KB | 1.713 KB | 906 KB |

We can notice how the H265 and AV1 codecs are the unique ones which really decrease the size of the original size. 

Watching the different exported collages, we can see more differences between codecs for the smallest resolution of 160x120 pixels. 

## Util links

- *AV1 Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/AV1
- *H.265/HEVC Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/H.265
- *VP8 Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/VP8
- *VP9 Video Encoding Guide:* https://trac.ffmpeg.org/wiki/Encode/VP9
- *create a mosaic out of several input videos:* https://trac.ffmpeg.org/wiki/Create%20a%20mosaic%20out%20of%20several%20input%20videos
- *Botón (Button) en Tcl/Tk (tkinter):* https://recursospython.com/guias-y-manuales/boton-button-en-tkinter/
- *Entry Widgets in Tkinter:* https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
- *Getting a TKinter input stored into a string variable in the next function?:* https://stackoverflow.com/questions/26414868/getting-a-tkinter-input-stored-into-a-string-variable-in-the-next-function
