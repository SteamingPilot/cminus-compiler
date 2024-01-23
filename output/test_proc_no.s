	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"

.comm c, 8, 8

	.text
	.globl b
	.type b, @function
b:
	pushq %rbp
	movq %rsp, %rbp
	movq $4, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	leave
	ret
	.text
	.globl main
	.type main, @function
main:
	pushq %rbp
	movq %rsp, %rbp
	call b
	leave
	ret
