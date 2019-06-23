# imports
from tests.base import Base

from pwgen.config import Config
from pwgen.generators.modules.genspecial import GenSpecial


class Test(Base):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getrandom_length(self):
        # config: special_charlist = default
        c1 = Config(value_validation=False)
        l1 = 15
        r1 = GenSpecial(c1).get_random(l1)
        self.assertTrue(len(r1) == l1)
        self.assertTrue(isinstance(r1, str))

        # config: special_charlist = custom
        c2 = Config(special_charlist=['!', '§', '$', '%', '&', '&'], value_validation=False)
        l2 = 15
        r2 = GenSpecial(c2).get_random(l2)
        self.assertTrue(len(r2) == l2)
        self.assertTrue(isinstance(r2, str))
