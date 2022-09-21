##
## EPITECH PROJECT, 2022
## 304pacman
## File description:
## Makefile
##

all:
	cp 304pacman.py 304pacman
	chmod +x 304pacman

clean:

tests_run:
	cd test/ && python -m coverage run -m unittest && python -m coverage report

fclean: clean
	rm 304pacman

re: fclean all

.PHONY: all clean fclean re
