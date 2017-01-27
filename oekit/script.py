
"""Utility code for building scripts.
"""

import argparse
from .config.argparse import add_login_args, ArgsConfig
from .config.chained import OEConfigChain
from .config.env import EnvConfig

class OdooScript(object):
    """Base class for an Odoo script.
    """

    @property
    def oe(self):
        """The connection created by the client factory.
        """
        if not (hasattr(self, '_oe') and self._oe):
            self._oe = self.get_client_factory().connect(self.config())
        return self._oe

    def parse_options(self):
        arg_parser = argparse.ArgumentParser(description=self.description())
        add_login_args(arg_parser)
        self.add_extra_arguments(arg_parser)
        self.options = arg_parser.parse_args()

    def add_extra_arguments(self, arg_parser):
        """Put your calls to arg_parser.add_argument() here
        """
        pass

    def config(self):
        """Return the standard configuration objects."""
        return OEConfigChain(configs=[ArgsConfig(self.options), EnvConfig()])

    def main(self):
        """Call this from your if __name__ == "__main__" block"""
        self.parse_options()
        self._main()

    def description(self):
        """This is passed to the constructor of ArgumentParser.

        It should be the description of what your script does.
        """
        raise NotImplementedError()

    def get_client_factory(self):
        """Return an instance of a client factory that will build your self.oe object"""
        raise NotImplementedError()

    def _main(self):
        """Put your script in here.  self.oe and self.options will be available.
        """
        pass    # script does nothing by default, just like an empty Python script
