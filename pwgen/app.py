# imports
import os
from pwgen.const import Const
from pwgen.config import Config
from pwgen.modules.export import Export
from pwgen.generators.gen import Gen

# set root-directory for this run
Const.ROOTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

if __name__ == "__main__":
    # passphrase_compose
    # d = dictionary words
    # r = random chars
    # s = special chars
    # example #1 :
    # config :      passphrase_compose = [['d', 4], ['s', 2]]
    # result :      dude+!

    # example #2 :
    # config :      passphrase_compose = [['r', 4], ['s', 1]]
    # result :      pwxi+
    passphrase_compose = []

    # dictionary_file
    # dictionary_file = path/to/custom/source.txt
    dictionary_file = "sources/german.txt"

    # dictionary_type
    # options :
    # text = text file (one word on one line)
    # json = json file
    # csv  = csv file
    dictionary_type = "text"

    # dictionary_encoding
    # options :
    # utf-8 (default)
    dictionary_encoding = "utf-8"

    # provide a basic config
    c = Config(dictionary_file=dictionary_file,
               dictionary_type=dictionary_type,
               dictionary_encoding=dictionary_encoding,
               passphrase_compose=[['d', 4], ['d', 7], ['r', 4], ['d', 4]])

    # generate n passwords. In this case 100 pwds will be created.
    g = Gen(c).process_list(amount=100)

    # export generated passwords to text
    r = Export().export_text(data=g, seperator="\n")

    # stdout generated
    print("\n" + r)
