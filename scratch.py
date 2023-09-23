from youtube_transcript_api import YouTubeTranscriptApi

# Video URL or video ID
video_id = '2QF52jLYkNo?si=z6yGnh9ho8pv2KXL'

try:
    # Get the transcript for the video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Create or overwrite the "subtitles.txt" file
    with open("subtitles.txt", "w", encoding="utf-8") as f:
        for entry in transcript:
            # Write each entry in the transcript to the file
            text = entry["text"]
            f.write(f"{text}\n")

    print("Transcript has been saved to 'subtitles.txt'")
except Exception as e:
    print(f"An error occurred: {str(e)}")


