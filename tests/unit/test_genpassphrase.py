# imports
from tests.base import Base

from pwgen.config import Config
from pwgen.generators.gen import Gen


class Test(Base):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_process(self):
        # config: dictionary test
        c1 = Config(value_validation=False, passphrase_compose=[['d', 5]])
        l1 = 5
        r1 = Gen(c1).process()
        self.assertTrue(len(r1) == l1)
        self.assertTrue(isinstance(r1, str))

        # config: random test
        c2 = Config(value_validation=False, passphrase_compose=[['r', 5]])
        l2 = 5
        r2 = Gen(c2).process()
        self.assertTrue(len(r2) == l2)
        self.assertTrue(isinstance(r2, str))

        # config: special test
        c3 = Config(value_validation=False, passphrase_compose=[['s', 5]])
        l3 = 5
        r3 = Gen(c3).process()
        self.assertTrue(len(r3) == l3)
        self.assertTrue(isinstance(r3, str))

        # config: custom complete
        c4 = Config(value_validation=False, passphrase_compose=[['d', 5], ['r', 5], ['s', 5]])
        l4 = 15
        r4 = Gen(c4).process()
        self.assertTrue(len(r4) == l4)
        self.assertTrue(isinstance(r4, str))

        # config: custom complete multiple
        c5 = Config(value_validation=False, passphrase_compose=[['d', 5], ['r', 5], ['s', 5],
                                                                ['d', 5], ['r', 5], ['s', 5]])
        l5 = 30
        r5 = Gen(c5).process()
        self.assertTrue(len(r5) == l5)
        self.assertTrue(isinstance(r5, str))

    def test_processlist(self):
        # config: dictionary test
        c1 = Config(value_validation=False, passphrase_compose=[['d', 5]])
        a1 = 3
        l1 = 5
        r1 = Gen(c1).process_list(a1)
        self.assertTrue(len(r1) == a1)
        self.assertTrue(len(r1[0]) == l1)
        self.assertTrue(isinstance(r1, list))

        # config: random test
        c2 = Config(value_validation=False, passphrase_compose=[['r', 5]])
        a2 = 3
        l2 = 5
        r2 = Gen(c2).process_list(a2)
        self.assertTrue(len(r2) == a2)
        self.assertTrue(len(r2[0]) == l2)
        self.assertTrue(isinstance(r2, list))

        # config: special test
        c3 = Config(value_validation=False, passphrase_compose=[['s', 5]])
        a3 = 3
        l3 = 5
        r3 = Gen(c3).process_list(a3)
        self.assertTrue(len(r3) == a3)
        self.assertTrue(len(r3[0]) == l3)
        self.assertTrue(isinstance(r3, list))

        # config: custom complete
        c4 = Config(value_validation=False, passphrase_compose=[['d', 5], ['r', 5], ['s', 5]])
        a4 = 3
        l4 = 15
        r4 = Gen(c4).process_list(a4)
        self.assertTrue(len(r4) == a4)
        self.assertTrue(len(r4[0]) == l4)
        self.assertTrue(isinstance(r4, list))

        # config: custom complete multiple
        c5 = Config(value_validation=False, passphrase_compose=[['d', 5], ['r', 5], ['s', 5],
                                                                ['d', 5], ['r', 5], ['s', 5]])
        a5 = 3
        l5 = 30
        r5 = Gen(c5).process_list(a5)
        self.assertTrue(len(r5) == a5)
        self.assertTrue(len(r5[0]) == l5)
        self.assertTrue(isinstance(r5, list))
