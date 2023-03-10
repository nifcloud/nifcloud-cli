import os
import sys

import awscli.help
from awscli import (EnvironmentVariables, argparser, clidocs, clidriver,
                    handlers, topictags)
from awscli.argprocess import ParamShorthandParser
from awscli.customizations.globalargs import register_parse_global_args
from awscli.customizations.streamingoutputarg import add_streaming_output_arg
from awscli.paramfile import register_uri_param_handler
from awscli.plugin import load_plugins
from botocore import __version__ as botocore_version
from botocore import loaders
from nifcloud import session

from nifcloudcli import __version__ as nifcloud_version
from nifcloudcli.constants import (AWS_CLI_COMMAND, AWS_SERVICE_NAME,
                                   NIFCLOUD_CLI_COMMAND, NIFCLOUD_SERVICE_NAME)
from nifcloudcli.customizations.configure import configure
from nifcloudcli.customizations.waiters import register_add_waiters
from nifcloudcli.link import get_document_site_url

argparser.USAGE = argparser.USAGE.replace(
    "\r" + argparser.AWS_CLI_V2_MESSAGE + "\n\nusage:", "")
argparser.USAGE = argparser.USAGE.replace(AWS_CLI_COMMAND,
                                          NIFCLOUD_CLI_COMMAND)
clidriver.USAGE = argparser.USAGE

root_dir = os.path.dirname(os.path.abspath(__file__))


class ProviderDocumentEventHandler(clidocs.ProviderDocumentEventHandler):

    def doc_title(self, help_command, **kwargs):
        doc = help_command.doc
        doc.style.new_paragraph()
        doc.style.h1(help_command.name)

    def doc_relateditems_start(self, help_command, **kwargs):
        pass

    def doc_relateditem(self, help_command, related_item, **kwargs):
        pass


ProviderHelpCommand = awscli.help.ProviderHelpCommand
ProviderHelpCommand.EventHandlerClass = ProviderDocumentEventHandler


class ServiceDocumentEventHandler(clidocs.ServiceDocumentEventHandler):

    def doc_breadcrumbs(self, help_command, **kwargs):
        pass

    def doc_title(self, help_command, **kwargs):
        doc = help_command.doc
        doc.style.new_paragraph()
        doc.style.h1(help_command.name)


ServiceHelpCommand = awscli.help.ServiceHelpCommand
ServiceHelpCommand.EventHandlerClass = ServiceDocumentEventHandler


class TopicTagsDB(topictags.TopicTagDB):

    TOPIC_DIR = os.path.join(root_dir, 'topics')
    JSON_INDEX = os.path.join(TOPIC_DIR, 'topic-tags.json')

    def __init__(self, tag_dictionary=None, index_file=None, topic_dir=None):
        index_file = (TopicTagsDB.JSON_INDEX
                      if index_file is None else index_file)
        topic_dir = TopicTagsDB.TOPIC_DIR if topic_dir is None else topic_dir
        super(TopicTagsDB, self).__init__(tag_dictionary, index_file,
                                          topic_dir)


class TopicListerDocumentEventHandler(clidocs.TopicListerDocumentEventHandler):

    DESCRIPTION = (clidocs.TopicListerDocumentEventHandler.DESCRIPTION.replace(
        AWS_SERVICE_NAME,
        NIFCLOUD_SERVICE_NAME).replace(AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND))

    def __init__(self, *args, **kwargs):
        super(TopicListerDocumentEventHandler, self).__init__(*args, **kwargs)
        self._topic_tag_db = TopicTagsDB()
        self._topic_tag_db.load_json_index()

    def doc_title(self, help_command, **kwargs):
        doc = help_command.doc
        doc.style.new_paragraph()
        doc.style.h1('NIFCLOUD CLI Topic Guide')


TopicListerCommand = awscli.help.TopicListerCommand
TopicListerCommand.EventHandlerClass = TopicListerDocumentEventHandler


class TopicDocumentEventHandler(clidocs.TopicDocumentEventHandler):

    def __init__(self, *args, **kwargs):
        super(TopicDocumentEventHandler, self).__init__(*args, **kwargs)
        self._topic_tag_db = TopicTagsDB()
        self._topic_tag_db.load_json_index()


TopicHelpCommand = awscli.help.TopicHelpCommand
TopicHelpCommand.EventHandlerClass = TopicDocumentEventHandler


class OperationDocumentEventHandler(clidocs.OperationDocumentEventHandler):

    def doc_breadcrumbs(self, help_command, **kwargs):
        pass

    def doc_title(self, help_command, **kwargs):
        doc = help_command.doc
        doc.style.new_paragraph()
        doc.style.h1(help_command.name)

    def _add_top_level_args_reference(self, help_command):
        help_command.doc.writeln('')
        help_command.doc.write("See ")
        help_command.doc.style.internal_link(title="'%s help'" %
                                             NIFCLOUD_CLI_COMMAND,
                                             page='/reference/index')
        help_command.doc.writeln(' for descriptions of global parameters.')

    def _add_webapi_crosslink(self, help_command):
        doc = help_command.doc
        operation_model = help_command.obj
        service_model = operation_model.service_model
        service_id = service_model.service_id
        if service_id is None:
            # If there's no service_id in the model, we can't
            # be certain if the generated cross link will work
            # so we don't generate any crosslink info.
            return
        doc.style.new_paragraph()
        doc.write("See also: ")
        link = get_document_site_url(service_id, operation_model.name)
        doc.style.external_link(title="%s API Documentation" %
                                NIFCLOUD_SERVICE_NAME,
                                link=link)
        doc.writeln('')


OperationHelpCommand = awscli.help.OperationHelpCommand
OperationHelpCommand.EventHandlerClass = OperationDocumentEventHandler
awscli.clidriver.OperationHelpCommand = OperationHelpCommand


class ProviderHelpCommand(awscli.help.ProviderHelpCommand):

    def __init__(self, session, command_table, arg_table, description,
                 synopsis, usage):
        super(ProviderHelpCommand,
              self).__init__(session, command_table, arg_table, description,
                             synopsis, usage)
        self._related_items = ['%s help topics' % NIFCLOUD_CLI_COMMAND]
        self._topic_tag_db = TopicTagsDB()

    @property
    def event_class(self):
        return NIFCLOUD_CLI_COMMAND

    @property
    def name(self):
        return NIFCLOUD_CLI_COMMAND


LOG = clidriver.LOG


class CLIDriver(clidriver.CLIDriver):

    def create_help_command(self):
        cli_data = self._get_cli_data()
        return ProviderHelpCommand(self.session, self._get_command_table(),
                                   self._get_argument_table(),
                                   cli_data.get('description', None),
                                   cli_data.get('synopsis', None),
                                   cli_data.get('help_usage', None))

    def _show_error(self, msg):
        msg = msg.replace(AWS_CLI_COMMAND, NIFCLOUD_CLI_COMMAND)
        LOG.debug(msg, exc_info=True)
        sys.stderr.write(msg)
        sys.stderr.write('\n')

    def _create_parser(self, command_table):
        # Also add a 'help' command.
        command_table['help'] = self.create_help_command()
        cli_data = self._get_cli_data()
        parser = argparser.MainArgParser(command_table,
                                         self.session.user_agent(),
                                         cli_data.get('description', None),
                                         self._get_argument_table(),
                                         prog=NIFCLOUD_CLI_COMMAND)
        return parser


clidriver.CLIDriver = CLIDriver

loaders.Loader.BUILTIN_DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'data')

# Delete awscli data path from botocore's search path
_cli_data_path = []
if 'NIFCLOUD_DATA_PATH' in os.environ:
    for path in os.environ['NIFCLOUD_DATA_PATH'].split(os.pathsep)[:-1]:
        path = os.path.expandvars(path)
        path = os.path.expanduser(path)
        _cli_data_path.append(path)
os.environ['NIFCLOUD_DATA_PATH'] = os.pathsep.join(_cli_data_path)


def awscli_initialize(event_handlers):

    event_handlers.register('session-initialized', register_uri_param_handler)
    param_shorthand = ParamShorthandParser()
    event_handlers.register('process-cli-arg', param_shorthand)
    register_parse_global_args(event_handlers)
    event_handlers.register('building-argument-table.*',
                            add_streaming_output_arg)
    register_add_waiters(event_handlers)
    event_handlers.register('building-command-table.main',
                            configure.ConfigureCommand.add_command)


handlers.awscli_initialize = awscli_initialize


def main():
    driver = create_clidriver()
    rc = driver.main()

    return rc


def create_clidriver():
    nifcloud_session = session.Session(EnvironmentVariables)
    _set_user_agent_for_session(nifcloud_session)
    load_plugins(nifcloud_session.full_config.get('plugins', {}),
                 event_hooks=nifcloud_session.get_component('event_emitter'))
    driver = clidriver.CLIDriver(session=nifcloud_session)
    return driver


def _set_user_agent_for_session(session):
    session.user_agent_name = 'nifcloud-cli'
    session.user_agent_version = nifcloud_version
    session.user_agent_extra = 'botocore/%s' % botocore_version
