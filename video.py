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
    output_filename = "audio_file.name.txt"
    aai.settings.api_key = "9f1b8c5ed3a5410b8ff252798d4a4b6f"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    print(transcript.text)
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        # Write the translated text to the file
        output_file.write(transcript.text)


if __name__ == "__main__":
    video_url = input("Enter the YouTube video.py URL: ")
    ans = input("'v' for Video, 't' for transcription.")
    if ans == 'v':
        download_video(video_url)
        # get_transcription(video_url)

    else:
        # download_audio(video_url)
        get_transcription(video_url)
