import datetime
import json
import locale
import subprocess
import time

xmlfn = "Superman again.mp4"

# Run ffprobe command to get chapter list
command = [
    "ffprobe",
    "-i",
    xmlfn,
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


def secs_to_time_str(secs):
    return str(datetime.timedelta(seconds=secs))


for i in range(len(real_chapters)):
    output_filename = f"{i + 1} - {real_chapters[i]['title']}.mp4"

    initial_start = real_chapters[i]["start"]
    initial_end = real_chapters[i]["end"]
    padding_seconds = 1
    padded_start = initial_start - 1
    padded_end = initial_end + 1

    silence_1_start = padded_start
    silence_1_end = initial_start
    silence_2_start = initial_end
    silence_2_end = padded_end

    af_param = f"volume=enable='between(t,{silence_1_start},{silence_1_end})':volume=0,afade=type=out:start_time={silence_2_start}:duration={padding_seconds}"

    # af_param = f"volume=enable='between(t,{silence_1_start},{silence_1_end})':volume=0,afade=type=out:start_time={silence_2_start}:duration={padding_seconds}"

    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        xmlfn,
        "-ss",
        secs_to_time_str(padded_start),
        "-to",
        secs_to_time_str(padded_end),
        "-af",
        af_param,
        output_filename,
    ]

    print(command)

    print(output_filename)
    processes.append(subprocess.Popen(command))

for process in processes:
    process.wait()
