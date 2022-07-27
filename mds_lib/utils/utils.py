import pathlib
import re
from typing import Optional

import click


def get_version() -> Optional[str]:  # pragma: no cover
    """
      Method for getting the version of the library from the init file
    :requirements: version must be specified separately
        :good: __version__ = '0.0.1'
        :bad: __version__, __any_variable__ = '0.0.1', 'any_value'
    :return: version lib
    """
    root_lib = pathlib.Path(__file__).parent.parent
    txt = (root_lib / "__init__.py").read_text("utf-8")
    txt = txt.replace("'", '"')
    try:
        version = re.findall(r'^__version__ = "([^"]+)"\r?$', txt, re.M)[0]
        return version
    except IndexError:
        raise RuntimeError("Unable to determine version.")


class GroupWithCommandOptions(click.Group):  # pragma: no cover
    """Allow application of options to group with multi command"""

    def add_command(self, cmd, name=None):
        click.Group.add_command(self, cmd, name=name)

        # add the group parameters to the command
        for param in self.params:
            cmd.params.append(param)

        # hook the commands invoke with our own
        cmd.invoke = self.build_command_invoke(cmd.invoke)
        self.invoke_without_command = True

    def build_command_invoke(self, original_invoke):
        def command_invoke(ctx):
            """insert invocation of group function"""

            # separate the group parameters
            ctx.obj = dict(_params=dict())
            for param in self.params:
                name = param.name
                ctx.obj["_params"][name] = ctx.params[name]
                del ctx.params[name]

            # call the group function with its parameters
            params = ctx.params
            ctx.params = ctx.obj["_params"]
            self.invoke(ctx)
            ctx.params = params

            # now call the original invoke (the command)
            original_invoke(ctx)

        return command_invoke
