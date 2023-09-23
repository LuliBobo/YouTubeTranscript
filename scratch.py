from youtube_transcript_api import YouTubeTranscriptApi

try:
    # Get the video URL or video ID from the user
    video_url = input("Enter the YouTube video URL or video ID: ")

    # Get the transcript for the video
    transcript = YouTubeTranscriptApi.get_transcript(video_url)

    # Create or overwrite the "subtitles.txt" file
    with open("subtitles.txt", "w", encoding="utf-8") as f:
        for entry in transcript:
            # Write each entry in the transcript to the file
            text = entry["text"]
            f.write(f"{text}\n")

    print("Transcript has been saved to 'subtitles.txt'")
except Exception as e:
    print(f"An error occurred: {str(e)}")
