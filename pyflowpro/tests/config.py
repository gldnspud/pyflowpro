"""Configuration loader for tests."""

from ConfigParser import ConfigParser
import os


_TEST_DIR = os.path.abspath(os.path.dirname(__file__))
_TEST_INI = os.path.join(_TEST_DIR, 'test.ini')


# Set attributes of module based on the configuration file.
_parser = ConfigParser()
_parser.read(_TEST_INI)
host = _parser.get('payflowpro', 'host')
partner = _parser.get('payflowpro', 'partner')
vendor = _parser.get('payflowpro', 'vendor')
user = _parser.get('payflowpro', 'user')
password = _parser.get('payflowpro', 'password')
