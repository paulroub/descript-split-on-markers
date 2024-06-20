import xml.etree.ElementTree as ET


def get_clips(xml_fn):
    tree = ET.parse(xml_fn)

    files = tree.findall('.//file/pathurl')
    markers = tree.findall('.//marker')
    clip_items = tree.findall('.//video/track/clipitem')

    clips = []
    last_clip = None

    for marker in markers:
        in_point = float(marker.find('in').text)

        clip = {
            'source_file': files[0].text,
            'start': float(in_point),
            'parts': [],
        }

        if last_clip:
            last_clip['end'] = float(in_point)

        clips.append(clip)
        last_clip = clip

    for clip in clips[:-1]:
        for item in clip_items:
            item_start = float(item.find('start').text)
            item_end = float(item.find('end').text)
            item_in = float(item.find('in').text)
            item_out = float(item.find('out').text)

            if item_start >= clip['start'] and item_end <= clip['end']:
                clip['parts'].append({
                    'start': item_start,
                    'end': item_end,
                    'in': item_in,
                    'out': item_out,
                })

    return clips[:-1]
