from awscli.customizations import commands

from nifcloudcli.constants import NIFCLOUD_CLI_COMMAND, NIFCLOUD_SERVICE_NAME
from nifcloudcli.link import get_document_site_url


class BasicDocHandler(commands.BasicDocHandler):

    NIFCLOUD_DOC_BASE = 'https://pfs.nifcloud.com/api'

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
