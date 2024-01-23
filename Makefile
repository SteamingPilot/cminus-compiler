UNIT = test_add_float test_add test_and_float test_and test_arith2 test_arith test_array_float \
   test_array test_bubble_float test_bubble test_call test_constdim test_dcs test_decl1 \
   test_decl2 test_decl3 test_dimen test_dim test_div_float test_div test_dynamic \
   test_ecall test_ejohn1 test_ejohn2 test_eq test_expr_char test_expr_float test_expr \
   test_farray test_f_noparams test_func2 test_func_no test_funcproc test_func test_gcd \
   test_gt test_hello test_if1 test_if_float test_if test_inv test_io_float \
   test_io test_log test_lt test_muldecl test_mul_float test_mul test_newdyn \
   test_nodecl test_nomeaning test_not test_or_float test_or test_param test_p_noparams \
   test_proc2 test_procfunc test_proc_no test_qs test_recurs test_retn test_simple \
   test_skeleton test_sub_float test_sub test_swapper test_sym test_typ2 test_type1 \
   test_var_multiple2 test_var_multiple test_var_simple test_while2_float test_while2 test_while3 test_while_array_char \
   test_while_array test_while_float test_while

.SILENT:

all_tests: 
	for tst in $(UNIT); do \
		echo "Running" $$tst; \
		make $$tst; \
	done

test_%: 
	make -C test $@

install:
	pip install ply

run:
	gcc -g -o ./output/mytest ./output/mytest.s
	./output/mytest
