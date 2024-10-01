.PHONY:install virtualenv ipython

nstall:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -r requirements.dev.txt

virtualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython	

test:
	@.venv/bin/pytest -vv -s 
watch:
	# @@.venv/bin/ptw -- -vv -s 
	@ls **/*.py | entr pytest     