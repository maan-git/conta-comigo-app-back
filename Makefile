
install:
	@echo "--> Installing requirements"
	pip install -r requirements-dev.txt
	@echo "--> Installing black"
	pip install black
	@echo "--> Installing pre-commit"
	pip install pre-commit
	pre-commit install
	@echo ""

lint:
	@echo "--> Running flake8"
	@echo "Funcionalidade ainda não implementada.."
	@echo ""

safety:
	@echo "--> Running safety"
	safety check
	@echo ""

test:
	@echo "--> Running tests"
	@echo "Funcionalidade ainda não implementada.."
	@echo ""

clean:
	@echo "--> Removing .pyc and __pycache__"
	find . | grep -E "__pycache__|.pyc$$" | xargs rm -rf
	@echo ""
	@echo "--> Removing coverage data"
	@echo "Funcionalidade ainda não implementada.."
	@echo ""

lint-fix:
	@echo "--> Auto fix lint errors "
	autopep8 --in-place --recursive .
	black .
	@echo ""

run:
	@echo "--> Running"
	python manage.py runserver 0.0.0.0:8000