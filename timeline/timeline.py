import xml.etree.ElementTree as ET


def get_clips(xml_fn):
    tree = ET.parse(xml_fn)

    files = tree.findall('.//file/pathurl')
    markers = tree.findall('.//marker')

    clips = []

    for marker in markers[:-1]:
        clip = {
            'source_file': files[0].text,
        }

        clips.append(clip)

    return clips