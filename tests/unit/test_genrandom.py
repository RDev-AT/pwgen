# imports
from tests.base import Base

from pwgen.config import Config
from pwgen.generators.modules.genrandom import GenRandom


class Test(Base):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getrandom(self):
        # config: special_charlist = default
        c1 = Config(value_validation=False)
        l1 = 15
        r1 = GenRandom(c1).get_random(l1)
        self.assertTrue(len(r1) == l1)
        self.assertTrue(isinstance(r1, str))

        # config: special_charlist = custom < 4 chars
        c2 = Config(random_charlist=['a', 'A', '?', '1', 'e', '2'], value_validation=False)
        l2 = 2
        r2 = GenRandom(c2).get_random(l2)
        self.assertTrue(len(r2) == l2)
        self.assertTrue(isinstance(r2, str))

        # config: special_charlist = custom > 4 chars
        c3 = Config(random_charlist=['a', 'A', '?', '1', 'e', '2'], value_validation=False)
        l3 = 15
        r3 = GenRandom(c3).get_random(l3)
        self.assertTrue(len(r3) == l3)
        self.assertTrue(isinstance(r3, str))
