	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"


	.text
	.globl b1
	.type b1, @function
b1:
	pushq %rbp
	movq %rsp, %rbp
	movq $1, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq $1, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl b2
	.type b2, @function
b2:
	pushq %rbp
	movq %rsp, %rbp
	movq $2, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	call b1
	movq %rax, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl b3
	.type b3, @function
b3:
	pushq %rbp
	movq %rsp, %rbp
	movq $3, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	call b1
	movq %rax, %rdi
	pushq %rdi
	subq $8, %rsp
	call b2
	movq %rax, %rsi
	addq $8, %rsp
	popq %rdi
	addq %rdi, %rsi
	movq %rsi, %rax
	leave
	ret
	.text
	.globl b4
	.type b4, @function
b4:
	pushq %rbp
	movq %rsp, %rbp
	movq $4, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	call b1
	movq %rax, %rdi
	pushq %rdi
	subq $8, %rsp
	call b2
	movq %rax, %rsi
	addq $8, %rsp
	popq %rdi
	addq %rdi, %rsi
	pushq %rsi
	subq $8, %rsp
	call b3
	movq %rax, %rdi
	addq $8, %rsp
	popq %rsi
	addq %rsi, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl main
	.type main, @function
main:
	pushq %rbp
	movq %rsp, %rbp
	call b1
	movq %rax, %rdi
	pushq %rdi
	subq $8, %rsp
	call b2
	movq %rax, %rsi
	addq $8, %rsp
	popq %rdi
	addq %rdi, %rsi
	pushq %rsi
	subq $8, %rsp
	call b3
	movq %rax, %rdi
	addq $8, %rsp
	popq %rsi
	addq %rsi, %rdi
	pushq %rdi
	subq $8, %rsp
	call b4
	movq %rax, %rsi
	addq $8, %rsp
	popq %rdi
	addq %rdi, %rsi
	movq %rsi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	leave
	ret
