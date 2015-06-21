


class Command:

	def execute(self, params=[]):
		result = self._run_command(params)
		return result

	def _run_command(self, params=[]):
		return 'Overwrite this method to do something useful :-)'