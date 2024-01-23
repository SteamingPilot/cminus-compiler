	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"

.float0:	.float 7.3

	.text
	.globl decls
	.type decls, @function
decls:
	pushq %rbp
	movq %rsp, %rbp
	movq $7, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl foo
	.type foo, @function
foo:
	pushq %rbp
	movq %rsp, %rbp
	movss .float0(%rip), %xmm0
	movss %xmm0, %xmm0
	leave
	ret
	.text
	.globl main
	.type main, @function
main:
	pushq %rbp
	movq %rsp, %rbp
	call decls
	movq %rax, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	call foo
	movss %xmm0, %xmm0
	cvtss2sd %xmm0, %xmm0
	leaq .float_wformat(%rip), %rdi
	movq $1, %rax
	call printf
	leave
	ret
