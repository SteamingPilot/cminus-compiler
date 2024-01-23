	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"

.comm a, 8, 8
.comm b, 8, 8
.float0:	.float 7.3

	.text
	.globl decls
	.type decls, @function
decls:
	pushq %rbp
	movq %rsp, %rbp
	movq a(%rip), %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq a(%rip), %rdi
	movq $0, %rsi
	cmp %rsi, %rdi
	mov $0, %rdi
	mov $1, %rsi
	cmovg %rsi, %rdi
	cmp $1, %rdi
	jne .L0
	movq a(%rip), %rdi
	movq $1, %rsi
	subq %rsi, %rdi
	movq %rdi, a(%rip)
	call decls
	movq %rax, %rdi
	movq %rdi, %rax
	jmp .L1
.L0:
	movq $0, %rdi
	movq %rdi, a(%rip)
	movq a(%rip), %rdi
	movq %rdi, %rax
	jmp .L1
.L1:
	leave
	ret
	.text
	.globl foo
	.type foo, @function
foo:
	pushq %rbp
	movq %rsp, %rbp
	movq a(%rip), %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq b(%rip), %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
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
	leaq a(%rip), %rsi
	leaq .int_rformat(%rip), %rdi
	movq $0, %rax
	call scanf
	call decls
	movq %rax, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq $10, %rdi
	movq %rdi, b(%rip)
	call foo
	movss %xmm0, %xmm0
	cvtss2sd %xmm0, %xmm0
	leaq .float_wformat(%rip), %rdi
	movq $1, %rax
	call printf
	leave
	ret
