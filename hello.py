print('hello') 
def higher_order_func(x):
    def helper(x):
        return (lambda x: x * x)(x)
    return helper
print(higher_order_func(9))
