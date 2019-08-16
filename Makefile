install:
	@pipenv install -e .
	@pipenv install --dev -e .

test:
	@pipenv run pytest --cov=. --cov-report=html
	@rm coverage.svg
	@pipenv run coverage-badge -o coverage.svg

black:
	@pipenv run black .

patch:
	@pipenv run bumpversion patch
