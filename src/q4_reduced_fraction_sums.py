import fractions

def reducedFractionSums(expressions):
    """
    Fairly self-explanatory, just use the built-in fractions package to perform
    the fraction addition -- they'll be automatically reduced in the end.
    """
    sum_array = []
    for expr in expressions:
        first_frac_string, second_frac_string = expr.split('+')
        first_frac = fractions.Fraction(first_frac_string)
        second_frac = fractions.Fraction(second_frac_string)
        sum_frac = first_frac + second_frac
        sum_array.append(str(sum_frac.numerator) + '/' + str(sum_frac.denominator))

    return sum_array
