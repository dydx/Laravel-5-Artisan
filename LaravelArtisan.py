import sublime, sublime_plugin, os
import subprocess

class Laravel4ArtisanCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(Laravel4ArtisanCommand, self).__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        self.command = kwargs.get('command', None)
        self.fill_in_accept = kwargs.get('fill_in', False)
        self.fill_in_label = kwargs.get('fill_in_lable', 'Enter the resource name')
        self.fields_accept = kwargs.get('fields', False)
        self.fields_label = kwargs.get('fields_label', 'Enter the fields')
        self.args = ["php", "artisan"]
        if self.command is None:
            self.window.show_input_panel("Command name w/o args:", "", self.on_custom_command, None, None)
        else:
            self.on_command(self.command)

    def on_command(self, value):
        self.args.append(value)
        if self.fill_in_accept is True:
            self.window.show_input_panel(self.fill_in_label, "", self.on_fill_in, None, None)
        else:
            self.on_done()

    def on_fill_in(self, value):
        self.args.append(value)

        if self.fields_accept is True:
            self.window.show_input_panel(self.fields_label, "", self.on_fields, None, None)
        else:
            self.on_done()

    def on_fields(self, value):
        if value != '':
            self.args.append('--fields=')
            self.args.append(value)
            self.on_done()
        else:
            self.on_done()

    def on_custom_command(self, value):
        self.args.append(value)
        sublime.status_message("%a" % self.args)
        self.on_done()

    def on_done(self):
        try:
            folder = self.window.folders()[0]
            os.chdir(folder)

            self.window.run_command("exec", {
                "cmd" : self.args,
                "shell" : False,
                "working_dir" : folder})

        except ValueError:
            pass