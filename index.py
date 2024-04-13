


#Python is a high level, object oriented, and easy to understand programming language, which was developed by Guido Van Rossum
print("Hello world") #first program

#variable declaration
name=5
print(name)

#concatetion string
name="Akarsh"
profession="Web developer"
print(name+profession)

#operators in python -> Arithmetic(+,-,*,/,%), Logical ops(and,or,not), Assignment ops(=,+=,-=,*=,/=), bitwise ops(&,||,!), relational ops(<,>,>=,<=,==),Membership ops(in,not in).
a=15
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b) # when we need the quotient / jb hume bhaagfal chahiye ho tb
print(a%b) # when we need the remainder/ jb hume shesh ki zaroorat ho

#logical ops
# -----For "AND"----
# 0 0 = 0; 1 0 = 0; 0 1 = 0; 1 1 = 1
marks=35
if marks>10 and marks < 20:
    print("Less tahn 20 and greater than 10")

else:
    print("No the above condition")

#if hp >= 1:
    #makeAlive(health)

# ---OR--- or loves true
# 0 0 = 0; 1 0 = 1; 0 1 = 1; 1 1 = 1
newString="Hello"
if newString=="Hello" or newString==" ":
    print("Variable is declared")
elif newString=="huii" or newString=="Bye":

    print("Hiii or Bye")
else:
    print("none matched!!")

# ---NOT--- kisi v given condition ko ulta kr dete h
    # true - false ; false - true

# --Project: Create a program to add the marks of a student and find his result.

#loops
# 1-- For loop
    # for(initialization, limit/condition, increment): body of loop
for i in range(1,10,2):
    print(i)

while i!=10:
    print(i)
