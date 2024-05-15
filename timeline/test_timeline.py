from timeline import timeline


def test_no_markers_no_clips():
    xml_fn = 'test_data/no_markers.xml'
    clips = timeline.get_clips(xml_fn)

    assert len(clips) == 0
