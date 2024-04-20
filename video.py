
import cv2
from ascii import imgtoascii
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips


def vdtoframes(path):
  vidcap = cv2.VideoCapture(path)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite("./.temp/frames/%d_frame.jpg" % count, image)
    print("%d_frame.jpg generated"%count)       
    success,image = vidcap.read()
    count += 1

def extract_audio(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)

def framestovd(inputpath,outpath,fps):
    image_files = [file for file in os.listdir(inputpath)]
    image_files.sort(key=lambda x: int(x.split("_")[0]))
    frame = cv2.imread(os.path.join(inputpath, image_files[0]))
    ih, iw, il = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(outpath, fourcc, fps, (iw, ih))
    for image in image_files:
        img_path = os.path.join(inputpath, image)
        video.write(cv2.imread(img_path))

    video.release()

def merge(outpath,output_audio_path,fps):
    ascii_video = VideoFileClip(outpath)
    original_audio = AudioFileClip(output_audio_path)
    final_video = ascii_video.set_audio(original_audio)
    final_video.write_videofile("./final_ascii_video_with_audio.mp4", codec="libx264", fps=fps)

