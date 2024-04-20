import video as vd
import os
from ascii import imgtoascii
import cv2
import shutil

og_video_path = input("Enter the path of the video: ").replace("\\", "/")
if(os.path.exists("./.temp")):
    shutil.rmtree('./.temp')
os.makedirs("./.temp/frames")
os.makedirs("./.temp/asciiframes")
vd.vdtoframes(og_video_path)

for e in os.listdir("./.temp/frames"):
    imgtoascii(os.path.join(os.path.join(os.getcwd(),"./.temp/frames"),e),int(e.split("_")[0]))
    print(e,"is converted to ascii")

fps=cv2.VideoCapture(og_video_path).get(cv2.CAP_PROP_FPS)
vd.framestovd("./.temp/asciiframes",'./.temp/ascii_video.mp4',fps)
vd.extract_audio(og_video_path,'./.temp/original_audio.wav')
vd.merge('./.temp/ascii_video.mp4','./.temp/original_audio.wav',fps)

shutil.rmtree('./.temp')

