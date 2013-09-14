import os
import shlex
import subprocess
import sublime
import sublime_plugin

class Laravel4ArtisanCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(Laravel4ArtisanCommand, self).__init__(*args, **kwargs)
        settings = sublime.load_settings('Laravel 4 Artisan.sublime-settings')
        self.php_path = settings.get('php_path')

    def run(self, *args, **kwargs):
        try:
            # The first folder needs to be the Laravel Project
            self.PROJECT_PATH = self.window.folders()[0]
            self.args = [self.php_path, os.path.join(self.PROJECT_PATH, 'artisan')]

            if os.path.isfile("%s" % os.path.join(self.PROJECT_PATH, 'artisan')):
                self.command = kwargs.get('command', None)
                self.fill_in_accept = kwargs.get('fill_in', False)
                self.fill_in_label = kwargs.get('fill_in_lable', 'Enter the resource name')
                self.fields_accept = kwargs.get('fields', False)
                self.fields_label = kwargs.get('fields_label', 'Enter the fields')
                self.args = [self.php_path, os.path.join(self.PROJECT_PATH, 'artisan')]
                if self.command is None:
                    self.window.show_input_panel('Command name w/o args:', '', self.on_command_custom, None, None)
                else:
                    self.on_command(self.command)
            else:
                sublime.status_message("Artisan not found")
        except IndexError:
            sublime.status_message("Please open a Laravel Project")

    def on_command(self, value):
        self.args.append(value)
        if self.fill_in_accept is True:
            self.window.show_input_panel(self.fill_in_label, "", self.on_fill_in, None, None)
        else:
            self.on_done()

    def on_fill_in(self, value):
        self.args.extend(shlex.split(str(value)))

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

    def on_command_custom(self, command):
        self.command = command
        self.args.extend(shlex.split(str(self.command)))
        self.on_done()

    def on_done(self):
        if os.name != 'posix':
            self.args = subprocess.list2cmdline(self.args)
        try:
            self.window.run_command("exec", {
                "cmd": self.args,
                "shell": False,
                "working_dir": self.PROJECT_PATH})
        except IOError:
            sublime.status_message('IOError - command aborted')
