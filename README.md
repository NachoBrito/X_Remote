# X_Remote
A simple python framework for remote command execution via XMPP (Jabber, GTalk/Hangouts, etc.). Just configure user credentials for it to log in to the xmpp server and setup a simple ACL structure to define who can execute each command.

A command is a Python class that extends cmd.base.Command, and implements a _run_command method.

This is project is in a very early stage. Use it carefully, and of course, any help will be appreciated :-)
