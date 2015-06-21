import importlib
import sys
import config
import types
import traceback
import collections


def run_command(cmd, from_peer):
	try:
		#process input
		parts = cmd.split(' ')
		cmd_name = '%sCommand' % parts[0].capitalize()
		cmd_params = parts[1:]

		check_permissions(cmd_name, from_peer)

		#Find command
		module = importlib.import_module('cmd.top')
		class_ = getattr(module, cmd_name)
		instance = class_()
		#Execute command
		result = instance.execute(cmd_params)		
	except:
		print(traceback.format_exc())
		result = sys.exc_info()[0]

	return "Command received from %s: %s. Result:\n==========\n%s" % (from_peer, cmd, result)

def check_permissions(cmd_name, from_peer):	
	if from_peer in config.peers_acl:
		permissions = config.peers_acl[from_peer]
		if isinstance(permissions, types.StringTypes) and permissions == '*':
			return True
		if isinstance(permissions, collections.Iterable):
			if cmd_name not in permissions:
				raise CommandNotAllowed
	raise PeerNotRecognized




class PeerNotRecognized(Exception):
	pass
class CommandNotAllowed(Exception):
	pass