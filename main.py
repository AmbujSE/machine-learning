# import sys
# import pandas as pd
# print(f"version of python: {sys.version}")
from pytube import YouTube
import assemblyai as aai
import os
# from googletrans import Translator


# def download_video(url):
#     try:
#         yt = YouTube(url)
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#         if stream:
#             print("Downloading:", yt.title)
#             stream.download()
#             print("Download completed!")
#         else:
#             print("No progressive stream available.")
#     except Exception as e:
#         print("An error occurred:", str(e))


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


def translate(text):

    # Define text to translate and output filename
    text_to_translate = get_transcription(text)
    print(text_to_translate)
    output_filename = "translated_text.txt"

    # Create a translator object
    translator = Translator()

    # Translate the text to Hindi
    translated_text = translator.translate(text_to_translate, dest='hi').text

    # Open the output file in write mode
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        # Write the translated text to the file
        output_file.write(translated_text)

    print(f"Text translated to Hindi and saved to {output_filename}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video.py URL: ")
    translate(video_url)

