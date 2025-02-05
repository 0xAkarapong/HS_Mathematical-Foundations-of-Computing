def g(x):
    return x**0.5

x_list = [2.1, 1.8, 0.5, -0.5]

def check_contractions(f, x_list):
    for x in x_list:
        print(f'f({x}) = {f(x)}')

print(check_contractions(g, x_list))