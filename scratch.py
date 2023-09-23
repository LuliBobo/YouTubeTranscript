from youtube_transcript_api import YouTubeTranscriptApi
from translate import Translator

try:
    # Get the video URL or video ID from the user
    video_url = input("Enter the YouTube video URL or video ID: ")

    # Get the transcript for the video
    transcript = YouTubeTranscriptApi.get_transcript(video_url)

    # Create or overwrite the "subtitles.txt" file
    with open("subtitles.txt", "w", encoding="utf-8") as f:
        for entry in transcript:
            # Translate the text to Slovak
            text = entry["text"]
            translator = Translator(to_lang="sk")
            translated_text = translator.translate(text)

            # Write the translated text to the file
            f.write(f"{translated_text}\n")

    print("Transcript has been translated to Slovak and saved to 'subtitles.txt'")
except Exception as e:
    print(f"An error occurred: {str(e)}")



