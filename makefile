DataAlbum.pdf : graph.py datos.txt
	python graph.py

datos.txt : album
	./album > datos.txt

album : 
	c++ album.cpp -o album
	
