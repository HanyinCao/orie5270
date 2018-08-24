import scipy.optimize as so

def rosenbrock(X):
    term_1 = 100*(X[1] - X[0]**2)**2 + (1 - X[0])**2
    term_2 = 100*(X[2] - X[1]**2)**2 + (1 - X[1])**2
    return term_1 + term_2

if __name__ == '__main__':
    min_value = None
    for i in range(-5,6,1):
        for j in range(-5,6,1):
            for k in range(-5,6,1):
                initial_guess = [i, j, k]
                result = so.minimize(rosenbrock, initial_guess, method = "BFGS")

                if min_value is None:
                    min_value = result.fun
                    result_X = result.x
                else:
                    if min_value > result.fun:
                        min_value = result.fun
                        result_X = result.x

    print ("The optimized result is ", min_value)
    print ("The resulting X is ", result_X)