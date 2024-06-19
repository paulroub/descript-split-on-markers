import xml.etree.ElementTree as ET


def get_clips(xml_fn):
    tree = ET.parse(xml_fn)

    files = tree.findall('.//file/pathurl')
    markers = tree.findall('.//marker')

    clips = []
    last_clip = None

    for marker in markers:
        in_point = float(marker.find('in').text)

        clip = {
            'source_file': files[0].text,
            'start': float(in_point),
        }

        if last_clip:
            last_clip['end'] = float(in_point)

        clips.append(clip)
        last_clip = clip

    return clips[:-1]
