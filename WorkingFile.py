#!/usr/bin/env python3
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import TextFormatter

from pathlib import Path

formatter = TextFormatter()

ts = YouTubeTranscriptApi.get_transcript('BI4z30nfv6k')

text_formatted = formatter.format_transcript(ts)
#create variable for filename
#open text file
text_file = open("C:\\Users\\jenny\\OneDrive\\Desktop\\Men & Lupus Work\\transcripts\\ThisIsLupus.txt", "w")
 
#write string to file
text_file.write(text_formatted)
 
#close file
text_file.close()
