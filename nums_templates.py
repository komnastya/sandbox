# Print / generate all numbers consisted of given parts of the number based on described template

# NUMBER TEMPLATE
# = <DIGITS>                                               # integer part
#   ( "." <DIGITS> )?                                      # optional fractional part
#   ( ( "e" or "E" ) ( ( "" or "-" or "+" ) <DIGITS> ) )?  # optional exp part

# The first variant with print statement


def print_nums(integers, fractionals, exps):
    def gen_nums_int():
        for integer in integers:
            print(integer)

    def gen_nums_frac():
        for integer in integers:
            for fractional in fractionals:
                print(str(integer) + "." + str(fractional))

    def gen_nums_exp():
        for integer in integers:
            for exp in ["e", "E"]:
                for sign in ["", "+", "-"]:
                    for exp_digit in exps:
                        print(str(integer) + exp + sign + str(exp_digit))

                        for fractional in fractionals:
                            print(
                                str(integer)
                                + "."
                                + str(fractional)
                                + exp
                                + sign
                                + str(exp_digit)
                            )

    gen_nums_int()
    gen_nums_frac()
    gen_nums_exp()


def gen_num(integer_part, fractional_part, exp_part):
    def gen_num_int():
        for int_digits in integer_part:
            yield str(int_digits)

    def gen_num_frac():
        for frac_digits in fractional_part:
            yield "." + str(frac_digits)

    def gen_num_exp():
        for exp in ["e", "E"]:
            for exp_sign in ["", "-", "+"]:
                for exp_digits in exp_part:
                    yield exp + exp_sign + str(exp_digits)

    for num_int in gen_num_int():
        yield num_int
        for num_frac in gen_num_frac():
            yield num_int + num_frac
        for num_exp in gen_num_exp():
            yield num_int + num_exp
        for num_frac in gen_num_frac():
            for num_exp in gen_num_exp():
                yield num_int + num_frac + num_exp


for num in gen_num([123], [1, 2], [5]):
    print(num)
