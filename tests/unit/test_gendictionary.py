# imports
import os

from tests.base import Base
from pwgen.const import Const
from pwgen.config import Config
from pwgen.generators.modules.gendictionary import GenDictionary

# set root-directory for this run
Const.ROOTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


class Test(Base):
    assets_csv1 = os.path.join(os.getcwd(), "assets/csv_file_1.csv")
    assets_csv2 = os.path.join(os.getcwd(), "assets/csv_file_2.csv")
    assets_csv3 = os.path.join(os.getcwd(), "assets/csv_file_3.csv")
    assets_json1 = os.path.join(os.getcwd(), "assets/json_file_1.json")
    assets_text1 = os.path.join(os.getcwd(), "assets/text_file_1.txt")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dictionary_type_csv(self):
        # csv: separated by ","
        c1 = Config(value_validation=False, dictionary_file=self.assets_csv1, dictionary_type='csv')
        a1 = 6
        l1 = 3
        o1 = GenDictionary(c1)
        r1 = o1.get_random(l1)
        self.assertTrue(len(r1) == l1)
        self.assertTrue(isinstance(r1, str))
        self.assertTrue(len(o1.data_memcache) == a1)

        # csv: separated by ";"
        c2 = Config(value_validation=False, dictionary_file=self.assets_csv2, dictionary_type='csv')
        a2 = 6
        l2 = 3
        o2 = GenDictionary(c1)
        r2 = o2.get_random(l2)
        self.assertTrue(len(r2) == l2)
        self.assertTrue(isinstance(r2, str))
        self.assertTrue(len(o2.data_memcache) == a2)

        # csv: separated by " "
        c3 = Config(value_validation=False, dictionary_file=self.assets_csv3, dictionary_type='csv')
        a3 = 6
        l3 = 3
        o3 = GenDictionary(c1)
        r3 = o3.get_random(l3)
        self.assertTrue(len(r3) == l3)
        self.assertTrue(isinstance(r3, str))
        self.assertTrue(len(o3.data_memcache) == a3)

    def test_dictionary_type_json(self):
        c1 = Config(value_validation=False, dictionary_file=self.assets_json1, dictionary_type='json')
        a1 = 6
        l1 = 3
        o1 = GenDictionary(c1)
        r1 = o1.get_random(l1)
        self.assertTrue(len(r1) == l1)
        self.assertTrue(isinstance(r1, str))
        self.assertTrue(len(o1.data_memcache) == a1)

    def test_dictionary_type_text(self):
        c1 = Config(value_validation=False, dictionary_file=self.assets_text1, dictionary_type='text')
        a1 = 6
        l1 = 3
        o1 = GenDictionary(c1)
        r1 = o1.get_random(l1)
        self.assertTrue(len(r1) == l1)
        self.assertTrue(isinstance(r1, str))
        self.assertTrue(len(o1.data_memcache) == a1)

