setup: venv
	. .venv/bin/activate && python -m pip install --upgrade pip
	. .venv/bin/activate && pip install -r requirements.txt

setup-win: venv
	. .venv/Scripts/activate && python -m pip install --upgrade pip
	. .venv/Scripts/activate && pip install -r requirements.txt

venv:
	test -d .venv || python -m venv .venv

clean: clean-pyc
	rm -rf .venv

clean-pyc:
	find . -name "*.pyc" -exec rm -f {} + 
	find . -name "*.pyo" -exec rm -f {} +
	find . -name "*~" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -fr {} +

tests: 
	. .venv/bin/activate && pytest --cov=src --cov-report=term-missing
	make clean-pyc > /dev/null

tests-win:
	. .venv/Scripts/activate && pytest --cov=src --cov-report=term-missing
	make clean-pyc > /dev/null


# entrypoints
main:
	. .venv/bin/activate && python src/main.py

main-win:
	. .venv/Scripts/activate && python src/main.py

executable:
	./binding_cpp_root/build/bin/binding

executable-win:
	binding_cpp_root/build/bin/binding.exe
