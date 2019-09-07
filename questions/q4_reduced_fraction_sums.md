# Reduced Fraction Sums

Consider two fractions in the form `a/b` and `c/d` where `a`, `b`, `c`, and `d` are integers.

Give a string describing an arithmetic expression that sums these two fractions in the form: `a/b + c/d`, compute the sum and fully reduce the resultant fraction to its simplest form. 

For example, 
* The expression `1/2  + 1/6` evaluates to `4/6`, which we reduce to the string `2/3`.

* The expression `7/10 + 13/10` evaluates to `20/10`, which reduce to the string `2/1`.

## Function description

Complete the function `reducedFractionSums` in the editor below. The function must return an array of strings representing the fully reduced fractions.

`reducedFractionSums` has the following parameter(s):
    *expression[expressions[0], ..., expressions[n-1]]* : an array of strings in the form `a/b+c/d`.
    
## Constraints 

* 1 <= n <= 500 
* 1 <= a, b, c, d <= 2000

