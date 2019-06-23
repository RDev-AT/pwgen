# imports
import os

from tests.base import Base
from pwgen.const import Const
from pwgen.config import Config

# set root-directory for this run
Const.ROOTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


class Test(Base):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        # config: default
        c1_dictionary_file = "tests/assets/csv_file_1.csv"
        c1 = Config(dictionary_file=c1_dictionary_file)

        self.assertTrue(c1.dictionary_type == c1.dictionary_type_default)
        self.assertTrue(c1.dictionary_type in c1.dictionary_type_available)

        self.assertTrue(c1.dictionary_encoding == c1.dictionary_encoding_default)
        self.assertTrue(c1.dictionary_encoding in c1.dictionary_encoding_available)

        self.assertTrue(c1.special_charlist == c1.special_charlist_default)

        self.assertTrue(c1.random_charlist == c1.random_charlist_default)

        self.assertTrue(c1.passphrase_compose == c1.passphrase_compose_default)

        self.assertTrue(c1.lookalikes_charlist == c1.lookalikes_charlist_default)

        # config: custom
        c2_dictionary_file = "tests/assets/csv_file_1.csv"
        c2_dictionary_type = "text"
        c2_dictionary_encoding = "utf8"
        c2_special_charlist = Config().ascii_charlist_lower
        c2_random_charlist = Config().ascii_charlist_lower
        c2_passphrase_compose = [['d', 3]]
        c2_lookalikes_charlist = ['a', 'b', 'c']
        c2 = Config(c2_dictionary_file,
                    c2_dictionary_type,
                    c2_dictionary_encoding,
                    c2_special_charlist,
                    c2_random_charlist,
                    c2_passphrase_compose,
                    c2_lookalikes_charlist)

        self.assertTrue(c2.dictionary_type == c2_dictionary_type)
        self.assertTrue(c2.dictionary_type in c2.dictionary_type_available)

        self.assertTrue(c2.dictionary_encoding == c2_dictionary_encoding)
        self.assertTrue(c2.dictionary_encoding in c2.dictionary_encoding_available)

        self.assertTrue(c2.special_charlist == c2_special_charlist)

        self.assertTrue(c2.random_charlist == c2_random_charlist)

        self.assertTrue(c2.passphrase_compose == c2_passphrase_compose)

        self.assertTrue(c2.lookalikes_charlist == c2_lookalikes_charlist)

    def test_export(self):
        c1 = Config()
        self.assertTrue(isinstance(c1.export(), dict))

    def test_exporthr(self):
        c1 = Config()
        self.assertTrue(isinstance(c1.exporthr(), str))
