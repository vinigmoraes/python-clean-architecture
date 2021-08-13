run:
	poetry export --without-hashes -f requirements.txt > requirements.txt
	docker-compose up --build -d
	rm -f requirements.txt

