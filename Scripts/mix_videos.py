import subprocess as sp


sp.call(["ffmpeg",
         "-i", "./videos/h265/bbb_160x120.mkv",
         "-i", "./videos/vp8/bbb_160x120.webm",
         "-i", "./videos/vp9/bbb_160x120.webm",
         "-i", "./videos/av1/bbb_160x120.mkv",
         "-filter_complex",
         f"nullsrc=size=320x240[base]; [0:v] setpts=PTS-STARTPTS, "
         f"scale=160x120 [upperleft]; [1:v] setpts=PTS-STARTPTS, "
         f"scale=160x120 [upperright]; [2:v] setpts=PTS-STARTPTS, "
         f"scale=160x120 [lowerleft]; [3:v] setpts=PTS-STARTPTS, "
         f"scale=160x120 [lowerright]; "
         f"[base][upperleft] overlay=shortest=1 [tmp1]; "
         f"[tmp1][upperright] overlay=shortest=1:x=160 [tmp2]; "
         f"[tmp2][lowerleft] overlay=shortest=1:y=120 [tmp3]; "
         f"[tmp3][lowerright] overlay=shortest=1:x=160:y=120",
         "-c:v", "libx264",
         "-crf", "30",
         "./videos/collages/bbb_160x120.mkv"])

sp.call(["ffmpeg",
         "-i", "./videos/h265/bbb_360x240.mkv",
         "-i", "./videos/vp8/bbb_360x240.webm",
         "-i", "./videos/vp9/bbb_360x240.webm",
         "-i", "./videos/av1/bbb_360x240.mkv",
         "-filter_complex",
         f"nullsrc=size=720x480[base]; [0:v] setpts=PTS-STARTPTS, "
         f"scale=360x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, "
         f"scale=360x240 [upperright]; [2:v] setpts=PTS-STARTPTS, "
         f"scale=360x240[lowerleft]; [3:v] setpts=PTS-STARTPTS, "
         f"scale=360x240 [lowerright]; "
         f"[base][upperleft] overlay=shortest=1 [tmp1]; "
         f"[tmp1][upperright] overlay=shortest=1:x=360 [tmp2]; "
         f"[tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; "
         f"[tmp3][lowerright] overlay=shortest=1:x=360:y=240",
         "-c:v", "libx264",
         "-crf", "30",
         "./videos/collages/bbb_360x240.mkv"])


sp.call(["ffmpeg",
         "-i", "./videos/h265/bbb_480x480.mkv",
         "-i", "./videos/vp8/bbb_480x480.webm",
         "-i", "./videos/vp9/bbb_480x480.webm",
         "-i", "./videos/av1/bbb_480x480.mkv",
         "-filter_complex",
         f"nullsrc=size=960x960[base]; [0:v] setpts=PTS-STARTPTS, "
         f"scale=480x480 [upperleft]; [1:v] setpts=PTS-STARTPTS, "
         f"scale=480x480 [upperright]; [2:v] setpts=PTS-STARTPTS, "
         f"scale=480x480 [lowerleft]; [3:v] setpts=PTS-STARTPTS, "
         f"scale=480x480 [lowerright]; "
         f"[base][upperleft] overlay=shortest=1 [tmp1]; "
         f"[tmp1][upperright] overlay=shortest=1:x=480 [tmp2]; "
         f"[tmp2][lowerleft] overlay=shortest=1:y=480 [tmp3]; "
         f"[tmp3][lowerright] overlay=shortest=1:x=480:y=480",
         "-c:v", "libx264",
         "-crf", "30",
         "./videos/collages/bbb_480x480.mkv"])

sp.call(["ffmpeg",
         "-i", "./videos/h265/bbb_720x720.mkv",
         "-i", "./videos/vp8/bbb_720x720.webm",
         "-i", "./videos/vp9/bbb_720x720.webm",
         "-i", "./videos/av1/bbb_720x720.mkv",
         "-filter_complex",
         "nullsrc=size=1440x1440[base]; [0:v] setpts=PTS-STARTPTS, "
         f"scale=720x720 [upperleft]; [1:v] setpts=PTS-STARTPTS, "
         f"scale=720x720 [upperright]; [2:v] setpts=PTS-STARTPTS, "
         f"scale=720x720 [lowerleft]; [3:v] setpts=PTS-STARTPTS, "
         f"scale=720x720 [lowerright]; "
         f"[base][upperleft] overlay=shortest=1 [tmp1]; "
         f"[tmp1][upperright] overlay=shortest=1:x=720 [tmp2]; "
         f"[tmp2][lowerleft] overlay=shortest=1:y=720 [tmp3]; "
         f"[tmp3][lowerright] overlay=shortest=1:x=720:y=720",
         "-c:v", "libx264",
         "-crf", "30",
         "./videos/collages/bbb_720x720.mkv"])

