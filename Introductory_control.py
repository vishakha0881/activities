'''Problem Statement- I
Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.

Steps to Follow: 
Understand how net run rate getting calculated (Cite the reference in submission comment)
Follow the computational thinking process.
Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
Design Controls -  Compound Statements and Suites
Provide Feedback to the User (Console level Feedback)
Test (Paper Calculation)
Validate (Paper Calculation = Code  Result)'''

Nint = 28
Div = 1
divisor_sum = 0

while Div < Nint:
    if Nint % Div == 0:
        divisor_sum += Div
    Div += 1

if divisor_sum > Nint:
    print(Nint, "is an abundant number.")
elif divisor_sum < Nint:
    print(Nint, "is a deficient number.")
else:
    print(Nint, "is a perfect number.")