

import main
import pytest


def test_transform_data():
    hw_data = main.load_json_test_file('testdata/hardware.golden')
    parsed_data = main.parse_hw_data(hw_data)
    assert parsed_data == main.load_json_test_file('testdata/parsed.golden')

def test_out_text():
    parsed_data = main.load_json_test_file('testdata/parsed.golden')
    out_text = main.to_output_text(parsed_data)
    assert out_text == main.load_test_file('testdata/out_text.golden')

def test_out_json():
    parsed_data = main.load_json_test_file('testdata/parsed.golden')
    out_json = main.output_format_json(parsed_data)
    assert out_json == main.load_test_file('testdata/out_json.golden')