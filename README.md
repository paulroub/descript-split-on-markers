# Split Descript Export by Markers

After using [Descript][descript] to trim out and pinpoint a sequence of speaker clips I'd like to pull from the composition, I wanted a way to quickly export those clips to separate video files.

This fits my typical workflow, but could definitely be generalized.

The expected composition structure at export-from-Descript time:

_stuff I don't want_  
**marker naming the first clip**  
_first clip_  
**marker naming the second clip**  
_second clip_  
_etc..._  
**end marker**  
_stuff I don't want_  

## A Painfully Simple Example

Using [this clip][supsource] of an old Max Fleischer Superman cartoon, I mark the clips I want to pull:

[![screenshot of a Descript composition with "Superman", "Lois" and "End" markers][markerimage]][markerimage]

I export the composition, being sure to include the markers as chapters:

[![Descript video export, with "metadata" and "Include markers as chapters" enabled][exportimage]][exportimage]

Run the `chapter_cuts.py` script:[^1]

```sh
$ python3 chapter_cuts.py superman-composition.mp4
1 - Superman.mp4
2 - Lois.mp4
```

And now we have our clips:

[![Finder listing of three video files, two named as in the above shell output][clipsimage]][clipsimage]

To give some breathing room when using these clips latter, each starts one second earlier and ends one second later than the exact marker point. The extra second at the beginning is silenced, and the extra second at the end fades out. These are, again, what works best for my typical needs. You can modify `PADDING_SECONDS` in the script to alter this behavior.

[supsource]: https://archive.org/details/40sSupermanCartoonCopiedInskyCaptainAndTheWorldOfTomorrow
[descript]: https://www.descript.com/
[dsmarkers]: https://help.descript.com/hc/en-us/articles/10164735239693-Using-markers
[markerimage]: i/markers.png
[exportimage]: i/export.png
[clipsimage]: i/clips.png

[^1]: No external modules are needed with stock macOS or Homebrew Python 3, at least, so while a virtual environment would be fine, it's not strictly necessary.
