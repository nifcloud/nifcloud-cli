from awscli.customizations import commands
from awscli.customizations.configure import set

from nifcloudcli.constants import AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND
from nifcloudcli.customizations.commands import BasicDocHandler


class ConfigureSetCommand(set.ConfigureSetCommand):
    DESCRIPTION = """
Set a configuration value from the config file.

The ``nifcloud configure set`` command can be used to set a single configuration
value in the NIFCLOUD config file.  The ``set`` command supports both the
*qualified* and *unqualified* config values documented in the ``get`` command
(see ``nifcloud configure get help`` for more information).

To set a single value, provide the configuration name followed by the
configuration value.

If the config file does not exist, one will automatically be created.  If the
configuration value already exists in the config file, it will updated with the
new configuration value.

Setting a value for the ``nifcloud_access_key_id``, ``nifcloud_secret_access_key``
will result in the value being writen to the shared credentials file
(``~/.nifcloud/credentials``).  All other values will be written to the
config file (default location is ``~/.nifcloud/config``).
"""
    SYNOPSIS = set.ConfigureSetCommand.SYNOPSIS.replace(
        AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND)
    EXAMPLES = ""

    def create_help_command(self):
        command_help_table = {}
        if self.SUBCOMMANDS:
            command_help_table = self.create_help_command_table()
        return commands.BasicHelp(self._session,
                                  self,
                                  command_table=command_help_table,
                                  arg_table=self.arg_table,
                                  event_handler_class=BasicDocHandler)
