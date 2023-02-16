import os

from awscli.customizations import commands
from awscli.customizations.configure import configure

from nifcloudcli.constants import (AWS_CLI_COMMAND, AWS_SERVICE_NAME,
                                   NIFCLOUD_CLI_COMMAND, NIFCLOUD_SERVICE_NAME)
from nifcloudcli.customizations.commands import BasicDocHandler
from nifcloudcli.customizations.configure.addmodel import AddModelCommand
from nifcloudcli.customizations.configure.get import ConfigureGetCommand
from nifcloudcli.customizations.configure.list import ConfigureListCommand
from nifcloudcli.customizations.configure.set import ConfigureSetCommand


class ConfigureCommand(configure.ConfigureCommand):
    DESCRIPTION = (
        'Configure NIFCLOUD CLI options. If this command is run with no'
        'arguments you will be prompted for configuration values such as'
        'your NIFCLOUD Access Key Id and your NIFCLOUD Secret Access Key.'
        'You can configure a named profile using the ``--profile`` argument.'
        'If your config file does not exist (the default location is'
        '``~/.nifcloud/config``), the NIFCLOUD CLI will create it for you. To'
        'keep an existing value, hit enter when prompted for the value. when'
        'you are prompted for information, the current value will be displayed'
        'in ``[brackets]``.  If the config item has no value, it be displayed'
        'as ``[None]``.  Note that the ``configure`` command only works with'
        'values from the config file.  It does not use any configuration'
        'values from environment variables.'
        ''
        'Note: the values you provide for the NIFCLOUD Access Key ID and the'
        'NIFCLOUD Secret Access Key will be written to the shared credentials'
        'file (``~/.nifcloud/credentials``).')
    SYNOPSIS = configure.ConfigureCommand.SYNOPSIS.replace(
        AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND)
    EXAMPLES = configure.ConfigureCommand.EXAMPLES.replace(
        AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND).replace(AWS_SERVICE_NAME,
                                                       NIFCLOUD_SERVICE_NAME)
    SUBCOMMANDS = [
        {
            'name': 'list',
            'command_class': ConfigureListCommand
        },
        {
            'name': 'get',
            'command_class': ConfigureGetCommand
        },
        {
            'name': 'set',
            'command_class': ConfigureSetCommand
        },
        {
            'name': 'add-model',
            'command_class': AddModelCommand
        },
    ]
    VALUES_TO_PROMPT = [
        ('nifcloud_access_key_id', "NIFCLOUD Access Key ID"),
        ('nifcloud_secret_access_key', "NIFCLOUD Secret Access Key"),
        ('region', "Default region name"),
        ('output', "Default output format"),
    ]

    def _write_out_creds_file_values(self, new_values, profile_name):
        creds_file_values = {}
        if 'nifcloud_access_key_id' in new_values:
            creds_file_values['nifcloud_access_key_id'] = new_values.pop(
                'nifcloud_access_key_id')
        if 'nifcloud_secret_access_key' in new_values:
            creds_file_values['nifcloud_secret_access_key'] = new_values.pop(
                'nifcloud_secret_access_key')
        if creds_file_values:
            if profile_name is not None:
                creds_file_values['__section__'] = profile_name
            shared_credentials_filename = os.path.expanduser(
                self._session.get_config_variable('credentials_file'))
            self._config_writer.update_config(creds_file_values,
                                              shared_credentials_filename)

    def create_help_command(self):
        command_help_table = {}
        if self.SUBCOMMANDS:
            command_help_table = self.create_help_command_table()
        return commands.BasicHelp(self._session,
                                  self,
                                  command_table=command_help_table,
                                  arg_table=self.arg_table,
                                  event_handler_class=BasicDocHandler)
