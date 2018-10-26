

import main
import pytest


def test_transform_data():
    hw_data = main.load_json_test_file('testdata/hardware.golden')
    transformed_data = main.transform_hw_data_1(hw_data)
    assert transformed_data == main.load_json_test_file('testdata/transformed.golden')


def test_pretty_data():
    transformed_data = main.load_json_test_file('testdata/transformed.golden')
    pretty_data = main.prettify_transformed_data(transformed_data)
    assert pretty_data == main.load_test_file('testdata/pretty.golden')