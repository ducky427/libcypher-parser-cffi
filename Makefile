
all:
	/usr/bin/clang -shared -undefined dynamic_lookup -I/usr/local/Cellar/libcypher-parser/0.1.0/include -L/usr/local/Cellar/libcypher-parser/0.1.0/lib -lcypher-parser -o libparse.so parse.c

run:
	/usr/bin/clang parse.c -I/usr/local/Cellar/libcypher-parser/0.1.0/include -L/usr/local/Cellar/libcypher-parser/0.1.0/lib -lcypher-parser -o parse