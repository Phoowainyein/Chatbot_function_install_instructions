#! /usr/bin/python3

"""def function_with_return(input_to_function1,input_to_function2):
    variable_that_we_return_from_function=input_to_function1+input_to_function2
    return variable_that_we_return_from_function
#call to function
answer_to_print1=function_with_return(1,4)
print(answer_to_print1)"""

#easy1:modify function so it takes 3 inputs
#instead of 2
#modify also function call,to call function with
#numbers 1,4,5

def easy1(input1,input2,input3):
    easy_to_return=input1+input2+input3
    return easy_to_return
easy1_answer=easy1(1,4,5)
print(easy1_answer)

#easy2:make another function call with numbers 1,2,3
#save that to variable answer_to_print2 and print that also
answer_to_print2=easy1(1,2,3)
print(answer_to_print2)
