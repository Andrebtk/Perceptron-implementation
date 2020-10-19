print("\n")
print("---------------------------")
print("   perceptron algorithm    ")
print("---------------------------")
print("\n\n")

print("Should i go outside today ? \n")
print("Answer by yes or no\n")

#take the input for the x

print("Does the weather look nive right now ?")
x1 = input()
print("Does the forecast say it will be nive all day ?")
x2 = input()
print("Do i have a jacket")
x3 = input()
print("\n")

#transform the yes/no in 1/0

def a(x):
    if x == "yes":
        x = 1
    else:
        x = 0
    return x
x1 = a(x1)
x2 = a(x2)
x3 = a(x3)


#paramater for the perceptron

bias = 2
x1_weight = 2
x2_weight = 1
x3_weight = 2


#Calculate y by doing the sum of all the x by there weight less the bias

y = (x1 * x1_weight) + (x2 * x2_weight) + (x1 * x2_weight) - bias


# Use the function of heaviside to output the result of y

if y > 0:
    print("The perceptron say that you should go outside today")

elif y < 0:
    print("The perceptron say that you should not go outside today")