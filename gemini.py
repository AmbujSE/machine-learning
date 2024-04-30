import os
import assemblyai as aai


# Function to inform users about AssemblyAI API key requirement
def get_transcription(link):
    audio_file = download_audio(link)
    aai.settings.api_key = ""

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    print(transcript)
    return transcript.text


def download_audio(link):

    from pytube import YouTube

    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file


# Function to download audio from YouTube (without audio extraction)
# def download_video(link):
#     from pytube import YouTube
#
#     try:
#         yt = YouTube(link)
#         video.py = yt.streams.first()  # Download the entire video.py for safety
#         out_file = video.py.download()
#         print(f"Video downloaded to: {out_file}")
#         return out_file
#     except Exception as e:
#         print(f"Error downloading video.py: {e}")
#         return None  # Indicate download failure


# Function to get user input for translation language
def get_target_language():
    while True:
        language = input("Enter the language to translate to (e.g., 'hi' for Hindi): ")
        if language:
            return language.lower()
        else:
            print("Please enter a valid language code.")


# Function to translate text to the specified language
def translate(text, target_language):
    from googletrans import Translator

    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_language).text

        # Open the output file in write mode (without AssemblyAI)
        with open("translated_text.txt", 'w', encoding='utf-8') as output_file:
            output_file.write(translated_text)

        print(f"Text translated to {target_language} and saved to translated_text.txt")
    except Exception as e:
        print(f"Error translating text: {e}")


if __name__ == "__main__":
    # Inform user about AssemblyAI key requirement
    # assemblyai_key_reminder()

    # Get YouTube video.py URL and inform user about safety limitation
    video_url = input("Enter the YouTube video.py URL (Downloading entire video.py for safety): ")
    print("**Warning:** This code downloads the entire video.py for safety reasons. Consider alternative methods for larger videos.")

    # Download the video.py
    downloaded_file = get_transcription(video_url)

    if downloaded_file:
        # User can manually transcribe the downloaded video.py using preferred methods
        text_to_translate = input("Enter the transcribed text or provide your own text to translate: ")
        target_language = get_target_language()
        translate(text_to_translate, target_language)
