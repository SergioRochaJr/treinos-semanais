uml:
	@poetry run pyreverse -o png src/training_exercises/*.py
prof:
	@poetry run pytest --profile-svg && \
		poetry run python -m snakeviz prof/combined.prof
complexity:
	@poetry run complexipy .
