import sublime, sublime_plugin, os
import subprocess

class SublimeArtisanKeyGenerateCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php", "artisan", "key:generate"],
			"shell" : False,
			"working_dir" : folder})

class SublimeArtisanMigrateCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php", "artisan", "migrate"],
			"shell" : False,
			"working_dir" : folder})


class SublimeArtisanMigrateRollbackCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php", "artisan", "migrate:rollback"],
			"shell" : False,
			"working_dir" : folder})

class SublimeArtisanMigrateResetCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php", "artisan", "migrate:reset"],
			"shell" : False,
			"working_dir" : folder})

class SublimeArtisanHelpCommandsCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php", "artisan", "help:commands"],
			"shell" : False,
			"working_dir" : folder})

class SublimeArtisanSessionTableCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)

			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "session:table"],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanMigrateMakeCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Filename:", "", self.on_done, None, None)

	def on_done(self, filename):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", "migrate:make", filename],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanMigrateApplicationCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)

			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "migrate", "application"],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanMigrateBundleCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)

			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "migrate", "bundle"],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanBundleInstallCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Bundle Name:", "", self.on_done, None, None)

	def on_done(self, bundle):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", "bundle:install", bundle],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanBundleInstallCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Bundle Name:", "", self.on_done, None, None)

	def on_done(self, bundle):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", "bundle:install", bundle],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanBundleUpgradeCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Bundle Name:", "", self.on_done, None, None)

	def on_done(self, bundle):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", "bundle:upgrade", bundle],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanBundleUpgradeAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)

			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "bundle:upgrade"],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanBundlePublishCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Bundle Name:", "", self.on_done, None, None)

	def on_done(self, bundle):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", "bundle:publish", bundle],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanBundlePublishAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)

			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "bundle:publish"],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanCallTaskCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Task name w/o args:", "", self.on_done, None, None)

	def on_done(self, task):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", task],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanRunApplicationTestsCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)

			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "test"],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanRunBundleTestsCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Bundle name:", "", self.on_done, None, None)

	def on_done(self, bundle):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", "test", bundle],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass

class SublimeArtisanRouteCallCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Route w/o restful:", "get api/user/1", self.on_done, None, None)

	def on_done(self, route):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", "route:call", route],
				"shell" : False,
				"working_dir" : folder})

		except ValueError:
			pass
