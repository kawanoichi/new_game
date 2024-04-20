help:
	@echo "ゲームを開始する"
	@echo " $$ make start"
start:
	poetry run python3 game.py
zikken:
	poetry run python3 zikken.py
