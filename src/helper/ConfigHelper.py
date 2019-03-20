import os
from configparser import ConfigParser
from configparser import NoOptionError


def get_config(files='config.conf'):
    """
    :param files: String
    :return config: ConfigParser
    """
    try:
        config = ConfigParser()
        config.read(os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            files
        ))
        return config
    except NoOptionError as e:  # pragma: no cover
        raise NoOptionError(e)