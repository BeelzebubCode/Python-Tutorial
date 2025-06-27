from moviepy.editor import VideoFileClip

gif_path = r"C:\Python\output_hd.gif"
mp4_path = "output_hd01.mp4"

clip = VideoFileClip(gif_path)
clip.write_videofile(mp4_path, codec="libx264")
