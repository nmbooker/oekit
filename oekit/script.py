
"""Utility code for building scripts.
"""

import argparse
from .config.argparse import add_login_args, ArgsConfig
from .config.chained import OEConfigChain
from .config.env import EnvConfig

class OdooScript(object):
    """
    """

    @property
    def oe(self):
        if not (hasattr(self, '_oe') and self._oe):
            self._oe = self.get_client_factory().connect(self.config())
        return self._oe

    def parse_options(self):
        arg_parser = argparse.ArgumentParser(description=self.description())
        self.add_arguments(arg_parser)
        self.add_extra_arguments(arg_parser)
        self.options = arg_parser.parse_args()

    def add_arguments(self, parser):
        add_login_args(parser)

    def add_extra_arguments(self, arg_parser):
        pass

    def config(self):
        return OEConfigChain(configs=[ArgsConfig(self.options), EnvConfig()])

    def main(self):
        self.parse_options()
        self._main()

    def description(self):
        raise NotImplementedError()

    def get_client_factory(self):
        raise NotImplementedError()

    def _main(self):
        pass    # script does nothing by default, just like an empty Python script
