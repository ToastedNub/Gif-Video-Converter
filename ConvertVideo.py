import os
from moviepy.editor import VideoFileClip

def convert_videos_to_gifs_and_extract_audio():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    videos_dir = os.path.join(script_dir, "VIDEOS")
    output_dir = os.path.join(script_dir, "GIFS")
    audio_dir = os.path.join(script_dir, "AUDIO")

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    video_files = [f for f in os.listdir(videos_dir) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    if not video_files:
        print("No video files found in the VIDEOS directory.")
        return

    for video_file in video_files:
        input_path = os.path.join(videos_dir, video_file)
        output_path = os.path.join(output_dir, os.path.splitext(video_file)[0] + ".gif")
        audio_output_path = os.path.join(audio_dir, os.path.splitext(video_file)[0] + ".mp3")

        try:
            print(f"Processing {video_file}...")

            clip = VideoFileClip(input_path)

            audio = clip.audio
            audio.write_audiofile(audio_output_path, codec='mp3')

            clip.write_gif(output_path, program="ffmpeg", fps=clip.fps, verbose=True)

            print(f"Saved GIF: {output_path}")
            print(f"Saved Audio: {audio_output_path}")
        except Exception as e:
            print(f"Failed to process {video_file}: {e}")

if __name__ == "__main__":
    convert_videos_to_gifs_and_extract_audio()
