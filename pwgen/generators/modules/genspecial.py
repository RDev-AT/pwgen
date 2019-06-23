# imports
import random

from pwgen.config import Config
from pwgen.generators.genhelper import GenHelper


class GenSpecial(GenHelper):
    config = None

    def __init__(self, config: Config) -> None:
        super().__init__(config)

        self.config = config

    def get_random(self, length: int) -> str:
        result = ""

        while len(result) != length:
            tmp = random.SystemRandom().choice(self.config.special_charlist)
            if not self.contains_lookalikes(tmp):
                result += tmp

        return result
