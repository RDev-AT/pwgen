# imports
import os
from pwgen.const import Const


class Config(object):
    # ascii charlist
    ascii_charlist_lower = list(map(chr, range(97, 122)))
    ascii_charlist_upper = list(map(chr, range(65, 90)))
    ascii_charlist_number = list(map(chr, range(48, 57)))
    ascii_charlist_special = list(map(chr, [33, 35, 36, 37, 38, 43, 45, 46, 58, 59, 61, 95]))

    # dictionary
    dictionary_file = None
    dictionary_file_default = os.path.join(Const.ROOTDIR, "sources/german.txt")

    dictionary_type = None
    dictionary_type_default = "text"
    dictionary_type_available = ['text', 'json', 'csv']

    dictionary_encoding = None
    dictionary_encoding_default = "utf8"
    dictionary_encoding_available = ['utf8', 'utf-8', 'utf_8']

    # special
    special_charlist = None
    special_charlist_default = ascii_charlist_special

    # random
    random_charlist = None
    random_charlist_default = (ascii_charlist_lower +
                               ascii_charlist_upper +
                               ascii_charlist_number +
                               ascii_charlist_special)

    # passphrase
    passphrase_compose = None
    passphrase_compose_default = [['d', 3], ['d', 4], ['d', 5], ['r', 4]]
    # passphrase_compose_type_available = ['d', 'r', 's']     # dictionary, random, special

    # lookalikes
    lookalikes_charlist = None
    lookalikes_charlist_default = ['1', 'l', 'I', '|', '0', 'O']

    def export(self) -> dict:
        return self.__dict__

    def exporthr(self) -> None:
        result = ""

        for v in self.__dict__:
            result += (str(v) + " - " + str(self.__dict__[v]))

        return result

    def __init__(self,
                 dictionary_file=None,
                 dictionary_type=None,
                 dictionary_encoding=None,
                 special_charlist=None,
                 random_charlist=None,
                 passphrase_compose=None,
                 lookalikes_charlist=None,
                 value_validation=True) -> None:

        self.dictionary_file = dictionary_file
        self.dictionary_type = dictionary_type
        self.dictionary_encoding = dictionary_encoding
        self.special_charlist = special_charlist
        self.random_charlist = random_charlist
        self.passphrase_compose = passphrase_compose
        self.lookalikes_charlist = lookalikes_charlist

        # dictionary_*: fallback default
        # # dictionary_file: not given
        if self.dictionary_file is None:
            self.dictionary_file = self.dictionary_file_default
        self.dictionary_file = os.path.join(Const.ROOTDIR, self.dictionary_file)
        # # dictionary_type: not given
        if self.dictionary_type is None:
            self.dictionary_type = self.dictionary_type_default
        # # dictionary_encoding: not given
        if self.dictionary_encoding is None:
            self.dictionary_encoding = self.dictionary_encoding_default
        if value_validation:
            # dictionary_*: value check
            # # dictionary_file: exists
            if not os.path.exists(self.dictionary_file):
                raise Exception("var dictionary_file refers to a not existing file path!")
            # # dictionary_type: in list
            if self.dictionary_type not in self.dictionary_type_available:
                raise Exception("var dictionary_type is not set to a valid value!")
            # # dictionary_encoding: in list
            if self.dictionary_encoding not in self.dictionary_encoding_available:
                raise Exception("var dictionary_encoding is not set to a valid value!")

        # special_*: fallback default
        # # special_charlist: not given
        if self.special_charlist is None:
            self.special_charlist = self.special_charlist_default
        if value_validation:
            # special_*: value check
            # # special_charlist: not set
            if len(self.special_charlist) == 0:
                raise Exception("var special_charlist can not be empty!")

        # random_*: fallback default
        # # random_charlist: not given
        if self.random_charlist is None:
            self.random_charlist = self.random_charlist_default
        if value_validation:
            # random_*: value check
            # # random_charlist: not set
            if len(self.random_charlist) == 0:
                raise Exception("var random_charlist can not be empty!")

        # passphrase_*: fallback default
        # # passphrase_compose: not given
        if self.passphrase_compose is None:
            self.passphrase_compose = self.passphrase_compose_default
        if value_validation:
            # passphrase_*: value check
            # # passphrase_compose: not set
            if len(self.passphrase_compose) == 0:
                raise Exception("var passphrase_compose can not be empty!")

        # lookalikes_*: fallback default
        # # lookalikes_charlist: not given
        if self.lookalikes_charlist is None:
            self.lookalikes_charlist = self.lookalikes_charlist_default
        # lookalikes_*: value check
        # # lookalike_charlist: not set
        # nothing to do here
