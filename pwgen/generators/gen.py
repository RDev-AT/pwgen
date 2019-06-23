# imports
from pwgen.config import Config
from pwgen.generators.genhelper import GenHelper
from pwgen.generators.modules.gendictionary import GenDictionary
from pwgen.generators.modules.genspecial import GenSpecial
from pwgen.generators.modules.genrandom import GenRandom


class Gen(GenHelper):
    config = None

    obj_gendictionary = None
    obj_genspecial = None
    obj_genrandom = None

    def __init__(self, config: Config) -> None:
        super().__init__(config)

        self.config = config

        self.obj_gendictionary = GenDictionary(self.config)
        self.obj_genspecial = GenSpecial(self.config)
        self.obj_genrandom = GenRandom(self.config)

    # process a single data
    def process(self) -> str:
        result = ""

        for ppc in self.config.passphrase_compose:
            # passphrase_compose: extract values
            ppc_type = ppc[0]
            ppc_length = ppc[1]

            if ppc_type == 'd':
                result += self.obj_gendictionary.get_random(ppc_length)

            elif ppc_type == 's':
                result += self.obj_genspecial.get_random(ppc_length)

            elif ppc_type == 'r':
                result += self.obj_genrandom.get_random(ppc_length)

        return result

    def process_list(self, amount: int) -> list:
        result = []

        for i in range(amount):
            result.append(self.process())

        return result
