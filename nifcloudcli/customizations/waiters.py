from awscli.customizations import waiters
from awscli.customizations.commands import BasicHelp

from nifcloudcli.customizations.commands import BasicDocHandler


def register_add_waiters(cli):
    cli.register('building-command-table', add_waiters)


def add_waiters(command_table, session, command_object, **kwargs):
    # Check if the command object passed in has a ``service_object``. We
    # only want to add wait commands to top level model-driven services.
    # These require service objects.
    service_model = getattr(command_object, 'service_model', None)
    if service_model is not None:
        # Get a client out of the service object.
        waiter_model = waiters.get_waiter_model_from_service_model(
            session, service_model)
        if waiter_model is None:
            return
        waiter_names = waiter_model.waiter_names
        # If there are waiters make a wait command.
        if waiter_names:
            command_table['wait'] = WaitCommand(session, waiter_model,
                                                service_model)


waiters.add_waiters = add_waiters


class WaitCommand(waiters.WaitCommand):

    def _run_main(self, parsed_args, parsed_globals):
        if parsed_args.subcommand is None:
            raise ValueError(
                "usage: nifcloud [options] <command> <subcommand> "
                "[parameters]\nnifcloud: error: too few arguments")

    def create_help_command(self):
        return BasicHelp(self._session,
                         self,
                         command_table=self.subcommand_table,
                         arg_table=self.arg_table,
                         event_handler_class=WaiterCommandDocHandler)


class WaiterCommandDocHandler(BasicDocHandler):

    def doc_breadcrumbs(self, help_command, **kwargs):
        pass

    def doc_title(self, help_command, **kwargs):
        doc = help_command.doc
        doc.style.new_paragraph()
        doc.style.h1(help_command.name)

    def doc_synopsis_start(self, help_command, **kwargs):
        pass

    def doc_synopsis_option(self, arg_name, help_command, **kwargs):
        pass

    def doc_synopsis_end(self, help_command, **kwargs):
        pass

    def doc_options_start(self, help_command, **kwargs):
        pass

    def doc_options_end(self, help_command, **kwargs):
        pass

    def doc_option(self, arg_name, help_command, **kwargs):
        pass
