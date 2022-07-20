import unittest
from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf, \
    append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc,\
    directories, documents

class Test_main(unittest.TestCase):
    def test_check_document_existance(self):
        self.assertEqual(check_document_existance('2207 876234'), True)

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('2207 876234'), "Василий Гупкин")

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(),set(["Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"]))

    def test_remove_doc_from_shelf(self):
        self.assertEqual(remove_doc_from_shelf('2207 876234'), directories)

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('4'), ('4', True))

    def test_append_doc_to_shelf(self):
        self.assertEqual(append_doc_to_shelf('12345', 3), directories)

    def test_delete_doc(self):
        self.assertEqual(delete_doc('2207 876234'), ('2207 876234', True))

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('2207 876234'), '1')

    def test_move_doc_to_shelf(self):
        self.assertEqual(move_doc_to_shelf('2207 876234', '2'), directories)

    def test_show_document_info(self):
        self.assertEqual(show_document_info(documents[0]), 'passport, 2207 876234, Василий Гупкин')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('123456', 'passport', 'Анатолий Павлов', '3'), documents[3])