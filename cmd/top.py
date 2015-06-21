from base import Command
from subprocess import check_output

class TopCommand(Command):
	def _run_command(self, params=[]):
		result = check_output(['top', '-l', '1', '-n', '5', '-o', 'cpu', '-stats', 'pid,command,cpu,th,pstate'])
		return result