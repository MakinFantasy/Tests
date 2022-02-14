import builtins
import unittest
from unittest import mock
from unittest.mock import patch, Mock

import app
from app import get_doc_shelf, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, add_new_doc, documents, directories


class TestDocFunctions(unittest.TestCase):
    def test_add_doc_normal_flow(self):
        # Patch dictionary in target scope
        with patch.dict(directories, {}, clear=True), \
                patch.object(app, documents, []), \
                patch('builtins.input', side_effect=['1', 'passport', 'Test Owner', '1']):
            add_new_doc()
        pass

    def test_get_shelf(self):
        pass

    def test_get_owner(self):
        pass

    def test_get_all(self):
        pass

    def test_remove_doc(self):
        pass
