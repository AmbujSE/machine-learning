from pytube import YouTube
import os
import assemblyai as aai


def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            print("Downloading:", yt.title)
            stream.download("./media")
            print("Download completed!")
        else:
            print("No progressive stream available.")
    except Exception as e:
        print("An error occurred:", str(e))


def download_audio(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file


def get_transcription(link):
    audio_file = download_audio(link)
    aai.settings.api_key = ""

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    print(transcript.text)
    return transcript.text


if __name__ == "__main__":
    video_url = input("Enter the YouTube video.py URL: ")
    # download_video(video_url)
    # download_audio(video_url)
    get_transcription(video_url)
