	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"

.comm A, 80, 8

	.text
	.globl main
	.type main, @function
main:
	pushq %rbp
	movq %rsp, %rbp
	sub $8, %rsp
	sub $8, %rsp
	movq $2, %rdi
	movq %rdi, -8(%rbp)
	movq $1, %rdi
	leaq (,%rdi,8), %rsi
	leaq A(%rip), %rdi
	addq %rsi, %rdi
movq %rdi, %rsi
	leaq .int_rformat(%rip), %rdi
	movq $0, %rax
	call scanf
	movq -8(%rbp), %rsi
	leaq (,%rsi,8), %rcx
	leaq A(%rip), %rsi
	addq %rcx, %rsi
	movq %rsi, %rcx
movq %rsi, %rsi
	leaq .int_rformat(%rip), %rdi
	movq $0, %rax
	call scanf
	movq %rcx, %rsi
	movq $1, %rsi
	leaq (, %rsi,8), %rbx
	leaq A(%rip), %rsi
	movq (%rbx,%rsi), %rsi
	movq %rsi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	movq -8(%rbp), %rsi
	leaq (, %rsi,8), %rbx
	leaq A(%rip), %rsi
	movq (%rbx,%rsi), %rsi
	movq %rsi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	leave
	ret
