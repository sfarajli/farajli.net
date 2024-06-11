all:

install:
	rsync -vrP --delete-after src/ root@farajli.xyz:/var/www/homepage

