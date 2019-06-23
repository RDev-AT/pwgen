# imports
import re
import random

from pwgen.config import Config
from pwgen.generators.genhelper import GenHelper


class GenRandom(GenHelper):
    config = None

    def __init__(self, config: Config) -> None:
        super().__init__(config)

        self.config = config

    """
    TODO:   Disable quality-check on small / insufficient charactar containing charlists.
            This bug can lead to infinity-loops.
    """
    def get_random(self, length: int) -> str:
        result = ""

        while True:
            tmp = random.SystemRandom().choice(self.config.random_charlist)
            if not self.contains_lookalikes(tmp):
                result += tmp

            # random-string: quality check disabled
            if len(result) == length < 4:
                return result

            # random-string: quality check enabled
            if len(result) == length >= 4:
                if re.match(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)", result):
                    return result
                else:
                    result = ""
