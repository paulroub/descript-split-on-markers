import datetime
import json
import locale
import os
import subprocess
import sys

PADDING_SECONDS = 1


def secs_to_time_str(secs):
    return str(datetime.timedelta(seconds=secs))


if len(sys.argv) != 2:
    print("Usage: python chapter_cuts.py <video_file>")
    sys.exit(1)

video_fn = sys.argv[1]
dest_dir = os.path.dirname(video_fn)

if not os.path.isfile(video_fn):
    print(f"Error: Video file {video_fn} does not exist.")
    sys.exit(1)

# Run ffprobe command to get chapter list
command = [
    "ffprobe",
    "-i",
    video_fn,
    "-print_format",
    "json",
    "-show_chapters",
    "-loglevel",
    "error",
]
output = subprocess.check_output(command)

# Parse the output as JSON
chapter_list = json.loads(output)

chapters = []

for chapter in chapter_list["chapters"][1:]:
    new_chapter = {
        "title": chapter["tags"]["title"],
        "start": locale.atof(chapter["start_time"]),
        "end": 0,
    }

    chapters.append(new_chapter)

for i in range(len(chapters) - 1):
    chapters[i]["end"] = chapters[i + 1]["start"]

real_chapters = chapters[:-1]
processes = []


for i, chapter in enumerate(real_chapters):
    output_filename = os.path.join(dest_dir, f"{i + 1} - {chapter['title']}.mp4")

    initial_start = chapter["start"]
    initial_end = chapter["end"]
    padded_start = initial_start - PADDING_SECONDS
    padded_end = initial_end + PADDING_SECONDS

    silence_1_start = padded_start
    silence_1_end = initial_start
    silence_2_start = initial_end
    silence_2_end = padded_end

    af_param = f"volume=enable='between(t,{silence_1_start},{silence_1_end})':volume=0,afade=type=out:start_time={silence_2_start}:duration={PADDING_SECONDS}"

    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        video_fn,
        "-ss",
        secs_to_time_str(padded_start),
        "-to",
        secs_to_time_str(padded_end),
        "-af",
        af_param,
        output_filename,
    ]

    print(output_filename)
    subprocess.run(command, check=True)
