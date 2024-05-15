from timeline import timeline


def test_no_markers_no_clips():
    xml_fn = 'test_data/no_markers.xml'
    clips = timeline.get_clips(xml_fn)

    assert len(clips) == 0

def test_full_has_two_clips():
    xml_fn = 'test_data/full.xml'
    clips = timeline.get_clips(xml_fn)

    assert len(clips) == 2

def test_correct_source_file_name():
    xml_fn = 'test_data/full.xml'
    clips = timeline.get_clips(xml_fn)

    assert clips[0]['source_file'] == 'Superman.mp4'
