from awscli.customizations import commands
from awscli.customizations.configure import list

from nifcloudcli.constants import (AWS_CLI_COMMAND, AWS_SERVICE_NAME,
                                   NIFCLOUD_CLI_COMMAND, NIFCLOUD_SERVICE_NAME)
from nifcloudcli.customizations.commands import BasicDocHandler


class ConfigureListCommand(list.ConfigureListCommand):
    DESCRIPTION = list.ConfigureListCommand.DESCRIPTION.replace(
        AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND).replace(AWS_SERVICE_NAME,
                                                       NIFCLOUD_SERVICE_NAME)
    SYNOPSIS = list.ConfigureListCommand.SYNOPSIS.replace(
        AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND)
    EXAMPLES = list.ConfigureListCommand.EXAMPLES.replace(
        AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND).replace(AWS_SERVICE_NAME,
                                                       NIFCLOUD_SERVICE_NAME)

    def create_help_command(self):
        command_help_table = {}
        if self.SUBCOMMANDS:
            command_help_table = self.create_help_command_table()
        return commands.BasicHelp(self._session,
                                  self,
                                  command_table=command_help_table,
                                  arg_table=self.arg_table,
                                  event_handler_class=BasicDocHandler)
