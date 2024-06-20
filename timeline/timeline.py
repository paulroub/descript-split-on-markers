import xml.etree.ElementTree as ET


def get_clips(xml_fn):
    tree = ET.parse(xml_fn)

    markers = tree.findall('.//marker')
    clip_items = tree.findall('.//video/track/clipitem')
    files = tree.findall('.//video/track/clipitem/file')

    clips = []
    files_by_id = {}
    last_clip = None

    for file in files:
        file_id = file.get('id')

        if file_id not in files_by_id:
            files_by_id[file_id] = {
                'source_file': file.find('pathurl').text
            }

    for marker in markers:
        in_point = float(marker.find('in').text)

        clip = {
            'start': float(in_point),
            'end': -1.0,
            'parts': [],
        }

        if last_clip:
            last_clip['end'] = float(in_point)

        clips.append(clip)
        last_clip = clip

    for clip in clips:
        for item in clip_items:
            item_start = float(item.find('start').text)
            item_end = float(item.find('end').text)
            item_in = float(item.find('in').text)
            item_out = float(item.find('out').text)

            file_id = item.find('file').get('id')
            item_source = files_by_id[file_id]['source_file']

            if item_start >= clip['start'] and item_start < clip['end']:
                clip['parts'].append({
                    'start': item_start,
                    'end': item_end,
                    'in': item_in,
                    'out': item_out,
                    'source_file': item_source,
                })

    return clips[:-1]
