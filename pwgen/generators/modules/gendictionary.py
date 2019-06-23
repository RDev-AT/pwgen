# imports
import re
import json
import random

from pwgen.config import Config
from pwgen.generators.genhelper import GenHelper


class GenDictionary(GenHelper):
    config = None
    data_memcache = []

    def __init__(self, config: Config) -> None:
        super().__init__(config)

        self.config = config

        # file: content processing
        try:
            with open(config.dictionary_file, 'r', encoding=config.dictionary_encoding) as fh:
                if config.dictionary_type == 'text':
                    self.dictionary_type_text(fh)

                elif config.dictionary_type == 'json':
                    self.dictionary_type_json(fh)

                elif config.dictionary_type == 'csv':
                    self.dictionary_type_csv(fh)

            # file: cleaning things up
            self.data_memcache = list(map(str.strip, self.data_memcache))
        except FileExistsError as e:
            print("error: path to dictionary-file seems not valid. " + str(e))
            exit(0)

    def dictionary_type_text(self, fh) -> None:
        for l in fh.readlines():
            self.data_memcache.append(l)

    def dictionary_type_json(self, fh) -> None:
        self.data_memcache = json.loads(fh.read())

    def dictionary_type_csv(self, fh) -> None:
        delimiter_available = [",", ";", " "]

        # file: read
        file_content = fh.read()

        # (c)sv type: autodetection
        delimiter_datasets = list(map(lambda e: len(file_content.split(e)), delimiter_available))
        delimiter_auto = delimiter_available[delimiter_datasets.index(max(delimiter_datasets))]

        self.data_memcache = file_content.split(delimiter_auto)

    def get_random(self, length: int) -> str:
        if len(self.data_memcache) == 0:
            print("error: no dictionary loaded. Exit now...")
            exit(1)

        if len(self.data_memcache) < 100000:
            print("warning: critical low amount of dictionary words!")

        while True:
            tmp = random.SystemRandom().choice(self.data_memcache)
            if len(tmp) == length and re.match(r"^[a-zA-Z]+$", tmp) and not self.contains_lookalikes(tmp):
                return tmp
