	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"

.comm x, 8, 8
.comm y, 8, 8

	.text
	.globl gcd
	.type gcd, @function
gcd:
	pushq %rbp
	movq %rsp, %rbp
	movq %rdi, -8(%rbp)
	movq %rsi, -16(%rbp)
	sub $8, %rsp
	sub $8, %rsp
	movq -16(%rbp), %rdi
	movq $0, %rsi
	cmp %rsi, %rdi
	mov $0, %rdi
	mov $1, %rsi
	cmove %rsi, %rdi
	cmp $1, %rdi
	jne .L0
	movq -8(%rbp), %rdi
	movq %rdi, %rax
	jmp .L1
.L0:
	movq -8(%rbp), %rdi
	movq %rdi, -24(%rbp)
	movq -16(%rbp), %rdi
	movq %rdi, -8(%rbp)
	movq -24(%rbp), %rdi
	movq -16(%rbp), %rsi
	movq -24(%rbp), %rcx
	movq -16(%rbp), %rbx
	movq %rcx, %rax
	cltd
	idivq %rbx
	movq %rax, %r8
	movq %rsi, %rax
	cltd
	imulq %r8
	movq %rax, %rcx
	subq %rcx, %rdi
	movq %rdi, -16(%rbp)
	movq -8(%rbp), %rdi
	movq -16(%rbp), %rsi
	movq %rdi, %rdi
	movq %rsi, %rsi
	call gcd
	movq %rax, %rdi
	movq %rdi, %rax
	jmp .L1
.L1:
	leave
	ret
	.text
	.globl main
	.type main, @function
main:
	pushq %rbp
	movq %rsp, %rbp
	leaq x(%rip), %rsi
	leaq .int_rformat(%rip), %rdi
	movq $0, %rax
	call scanf
	leaq y(%rip), %rsi
	leaq .int_rformat(%rip), %rdi
	movq $0, %rax
	call scanf
.L2:
	movq x(%rip), %rdi
	movq $0, %rsi
	cmp %rsi, %rdi
	mov $0, %rdi
	mov $1, %rsi
	cmovne %rsi, %rdi
	movq y(%rip), %rsi
	movq $0, %rcx
	cmp %rcx, %rsi
	mov $0, %rsi
	mov $1, %rcx
	cmovne %rcx, %rsi
	movq $0, %rcx
	movq $1, %rbx
	cmpq $0, %rdi
	cmovne %rbx, %rcx
	cmpq $0, %rsi
	cmovne %rbx, %rcx
	cmp $1, %rcx
	jne .L3
	movq x(%rip), %rdi
	movq y(%rip), %rsi
	movq %rdi, %rdi
	movq %rsi, %rsi
	call gcd
	movq %rax, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	leaq x(%rip), %rsi
	leaq .int_rformat(%rip), %rdi
	movq $0, %rax
	call scanf
	leaq y(%rip), %rsi
	leaq .int_rformat(%rip), %rdi
	movq $0, %rax
	call scanf
	jmp .L2
.L3:
	leave
	ret
