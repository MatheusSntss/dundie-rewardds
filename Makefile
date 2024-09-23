.PHONY:install virtualenv ipython

nstall:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -r requirements.dev.txt

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython	