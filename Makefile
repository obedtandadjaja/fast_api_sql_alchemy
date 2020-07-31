start:
	uvicorn app.main:app --reload

seed:
	python3 seed.py
