"""configuration system."""

import os

from abc import ABC

from typing import List, Type


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(ABC):
    """Base of Configuration."""

    CONFIG_NAME = "base"
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Develop configuration."""

    CONFIG_NAME = "dev"
    INPUT_FILE = "files/input/input.txt"
    OUTPUT_FILE = "files/output/output.txt"
    DEBUG = True
    TESTING = False
    TIME_OUT = 5000


class TestingConfig(BaseConfig):
    """Test configuration."""

    CONFIG_NAME = "test"
    INPUT_FILE = "tests/files/test_input/test_file.txt"
    OUTPUT_FILE = "tests/files/test_output/test_output.txt"
    DEBUG = True
    TESTING = True
    TIME_OUT = 5000


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
