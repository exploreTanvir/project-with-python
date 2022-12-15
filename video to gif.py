# import necessary library
from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

# open file for load video
video = askopenfilename()

# load file in a variable
clip = VideoFileClip(video)

# Make GIF of Uploaded Video
clip.write_gif("Water Fall GIF.gif", fps=60)


