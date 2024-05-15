import xml.etree.ElementTree as ET


def get_clips(xml_fn):
    tree = ET.parse(xml_fn)

    markers = tree.findall('.//marker')

    return markers[:-1]