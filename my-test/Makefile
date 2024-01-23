all: t.c
	gcc -g -o ./t ./t.c

run: t
	./t

asm: t.c
	gcc -fno-stack-protector -S ./t.c

rm:
	rm -f ./t ./t.s+
