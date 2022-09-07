from unittest import TestCase
import pytest


@pytest.mark.usefixtures("serial")
class BaseTestCase(TestCase):
    pass
