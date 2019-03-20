import pytest
from src.helper.ConfigHelper import get_config
from configparser import NoOptionError


@pytest.fixture
def get_fixtures():
    return [
        ('testing1', 'get_value_1'),
        ('testing2', 'get_value_2'),
        ('testing3', 'get_value_3'),
        ('testing4', 'exception'),
        ('testing5', 'exception')
    ]


def test_get_config(get_fixtures):
    config = get_config('test/helper/ConfigHelper/sample-config.conf')
    for data in get_fixtures:
        key = data[0]
        expected = data[1]

        if expected != 'exception':
            assert config.get('default', key) == expected
        else:
            with pytest.raises(Exception):
                config.get('default', key)


def test_if_data_not_available():
    config = get_config('test/helper/ConfigHelper/sample-config.conf')
    with pytest.raises(NoOptionError) as e:
        config.get('default', 'not found')

    assert e.value.message == "No option 'not found' in section: 'default'"

