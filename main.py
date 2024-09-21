import os
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import sys
import logging
import re

logger = logging.getLogger(__name__)

load_dotenv()

if len(sys.argv) > 1 and sys.argv[1] == "-l" and len(sys.argv) > 2:
    url = sys.argv[2]
else:
    url = input("Please enter the YouTube URL: ")

lang = os.getenv("YOUTUBE_LANG")
if lang is None:
    raise EnvironmentError("YOUTUBE_LANG variable not set in the environment")

model = os.getenv("OPENAI_MODEL")
if model is None:
    raise EnvironmentError("OPENAI_MODEL variable not set in the environment")

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise EnvironmentError("OPENAI_API_KEY variable not set in the environment")
client = OpenAI(api_key=openai_api_key)

system_input = os.getenv("SYSTEM_INPUT")
if system_input is None:
    raise EnvironmentError("SYSTEM_INPUT variable not set in the environment")


def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    """
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")


def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("YOUTUBE_LANG: %s", lang)
    logger.info("URL: %s", url)

    video_id = extract_video_id(url)
    logger.info("Video ID: %s", video_id)

    transcript = YouTubeTranscriptApi.get_transcript(
        video_id=video_id, languages=[lang]
    )
    logger.info("len(transcript): %s", len(transcript))

    input = ""
    for t in transcript:
        input += t["text"]

    completion = client.chat.completions.create(
        model=model,  # type: ignore # because it will be not None here
        messages=[
            {
                "role": "system",
                "content": system_input,
            },  # type: ignore # because it will be not None here
            {"role": "user", "content": input},
        ],
    )

    logger.info(completion.choices[0].message.content)

    logger.info("API USAGE: %s", completion.usage)


if __name__ == "__main__":
    main()
