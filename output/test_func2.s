	 .section .rodata

.char_wformat: .string "%c\n"
.int_wformat: .string "%d\n"
.float_wformat: .string "%f\n"
.str_wformat: .string "%s\n"
.char_rformat: .string "%c"
.int_rformat: .string "%ld"
.float_rformat: .string "%f"

.comm c, 8, 8
.float0:	.float 2.0

	.text
	.globl b
	.type b, @function
b:
	pushq %rbp
	movq %rsp, %rbp
	movq %rdi, -8(%rbp)
	movq %rsi, -16(%rbp)
	movss %xmm2, -24(%rbp)
	movq -8(%rbp), %rdi
	movq -16(%rbp), %rsi
	addq %rdi, %rsi
	pxor %xmm0, %xmm0
	cvtsi2ss %rsi, %xmm0
	movss -24(%rbp), %xmm1
	addss %xmm0, %xmm1
	movss %xmm1, %xmm0
	leave
	ret
	.text
	.globl main
	.type main, @function
main:
	pushq %rbp
	movq %rsp, %rbp
	movq $1, %rdi
	movq $1, %rsi
	movss .float0(%rip), %xmm0
	movq %rdi, %rdi
	movq %rsi, %rsi
	movss %xmm0, %xmm2
	call b
	movss %xmm0, %xmm0
	cvttss2si %xmm0, %rdi
	movq %rdi, c(%rip)
	movq c(%rip), %rdi
	movq %rdi, %rsi
	leaq .int_wformat(%rip), %rdi
	mov $0, %rax
	call printf
	leave
	ret
