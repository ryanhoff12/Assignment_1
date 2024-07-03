VENV_DIR?=.venv-Assignment_1
VENV_ACTIVATE=$(VENV_DIR)/bin/activate
WITH_VENV=. $(VENV_ACTIVATE);

.PHONY: venv
venv: $(VENV_ACTIVATE)

$(VENV_ACTIVATE): requirements.txt
	test -f $@ || python -m venv $(VENV_DIR)
	$(WITH_VENV) pip install -r requirements.txt
	touch $@
