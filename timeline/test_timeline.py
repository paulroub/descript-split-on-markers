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

def test_first_clip_start():
    xml_fn = 'test_data/full.xml'
    clips = timeline.get_clips(xml_fn)

    assert clips[0]['start'] == 0.0

def test_first_clip_end():
    xml_fn = 'test_data/full.xml'
    clips = timeline.get_clips(xml_fn)

    assert clips[0]['end'] == 739.0

def test_second_clip_times():
    xml_fn = 'test_data/full.xml'
    clips = timeline.get_clips(xml_fn)

    assert clips[0]['start'] == 0.0
    assert clips[0]['end'] == 739.0
    assert clips[1]['start'] == 739.0
    assert clips[1]['end'] == 789.0

def test_multi_part_clips():
    xml_fn = 'test_data/clip-across-edits.xml'
    clips = timeline.get_clips(xml_fn)

    assert clips[0]['start'] == 0.0
    assert clips[0]['end'] == 357.0

    assert len(clips[0]['parts']) == 5
