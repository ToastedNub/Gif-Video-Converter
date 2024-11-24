import os
from moviepy.editor import VideoFileClip, AudioFileClip

gif_directory = os.path.join(os.getcwd(), 'GIFS')
audio_directory = os.path.join(os.getcwd(), 'AUDIO')
output_directory = os.path.join(os.getcwd(), 'VIDEOS')

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def convert_gif_to_video(gif_path, output_path, audio_path=None):
    clip = VideoFileClip(gif_path)

    if audio_path:
        audio = AudioFileClip(audio_path)
        clip = clip.set_audio(audio.set_duration(clip.duration))

    clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

gif_files = [f for f in os.listdir(gif_directory) if f.lower().endswith('.gif')]

for gif_file in gif_files:
    gif_path = os.path.join(gif_directory, gif_file)
    output_file = os.path.splitext(gif_file)[0] + '.mp4'
    output_path = os.path.join(output_directory, output_file)

    audio_file = os.path.splitext(gif_file)[0] + '.mp3'
    audio_path = os.path.join(audio_directory, audio_file)

    if os.path.exists(audio_path):
        convert_gif_to_video(gif_path, output_path, audio_path)
        print(f"Converted {gif_file} to video with audio and saved it as {output_file}")
    else:
        convert_gif_to_video(gif_path, output_path)
        print(f"Converted {gif_file} to video without audio and saved it as {output_file}")
