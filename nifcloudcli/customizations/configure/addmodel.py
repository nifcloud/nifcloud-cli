from awscli.customizations import commands
from awscli.customizations.configure import addmodel

from nifcloudcli.constants import AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND
from nifcloudcli.customizations.commands import BasicDocHandler


class AddModelCommand(addmodel.AddModelCommand):
    DESCRIPTION = addmodel.AddModelCommand.DESCRIPTION.replace(
        AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND)

    def create_help_command(self):
        command_help_table = {}
        if self.SUBCOMMANDS:
            command_help_table = self.create_help_command_table()
        return commands.BasicHelp(self._session,
                                  self,
                                  command_table=command_help_table,
                                  arg_table=self.arg_table,
                                  event_handler_class=BasicDocHandler)
