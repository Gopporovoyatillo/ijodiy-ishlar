# @OLLIT_DEV
from moviepy.editor import VideoFileClip
clip=VideoFileClip("armon.mp4")
clip.write_gif("armonligif.gif",fps=10)
