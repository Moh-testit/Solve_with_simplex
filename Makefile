## File description:
## Makefile
##

NAME	=	307multigrains

all:	$(NAME)

$(NAME):
		ln -s 307multigrains.py $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf *~
		rm -rf __pycache__

fclean:	clean
		rm -rf $(NAME)

re:	fclean all
