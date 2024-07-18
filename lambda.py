def maths_operation(a,b):
    '''
    the function takes two numbers as inputs and returns
    their sum and product.

     parameters:
    a(float): The first number.
    b(float): the second number
    Returns:
    tuple:A tuple containing the sum and product of the two numbers.
    '''
    sum_result = (lambda x, y: x + y)(a,b)
    product_result = (lambda x, y: x * y)(a,b)
    return sum_result,product_result

def main():
    #get user inputs
    a = float(input("please enter the firstnumber"))
    b = float(input("please enter the second number"))

    sum_result,product_result = maths_operation(a,b)

    #calling the maths_operation
    print(f"the sum of {a} and {b} is:{sum_result}")
    print(f"the product of {a} and {b} is:{product_result}")

    main()
    

    
   
    
   
