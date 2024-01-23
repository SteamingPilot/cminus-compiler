	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"

.comm i, 8, 8
.comm j, 8, 8
.comm k, 8, 8
.comm l, 8, 8

	.text
	.globl a1
	.type a1, @function
a1:
	pushq %rbp
	movq %rsp, %rbp
	movq $1, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq $0, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl a2
	.type a2, @function
a2:
	pushq %rbp
	movq %rsp, %rbp
	call a1
	movq %rax, %rdi
	movq %rdi, j(%rip)
	movq $2, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq $0, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl a3
	.type a3, @function
a3:
	pushq %rbp
	movq %rsp, %rbp
	call a1
	movq %rax, %rdi
	movq %rdi, i(%rip)
	call a2
	movq %rax, %rdi
	movq %rdi, j(%rip)
	movq $3, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq $0, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl a4
	.type a4, @function
a4:
	pushq %rbp
	movq %rsp, %rbp
	call a1
	movq %rax, %rdi
	movq %rdi, i(%rip)
	call a2
	movq %rax, %rdi
	movq %rdi, j(%rip)
	call a3
	movq %rax, %rdi
	movq %rdi, k(%rip)
	movq $4, %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq $0, %rdi
	movq %rdi, %rax
	leave
	ret
	.text
	.globl main
	.type main, @function
main:
	pushq %rbp
	movq %rsp, %rbp
	call a1
	movq %rax, %rdi
	movq %rdi, i(%rip)
	call a2
	movq %rax, %rdi
	movq %rdi, j(%rip)
	call a3
	movq %rax, %rdi
	movq %rdi, k(%rip)
	call a4
	movq %rax, %rdi
	movq %rdi, l(%rip)
	leave
	ret
