""" 
This is about the operators in Python. 
These operators are used to perform operations on variables and values.
The types of operators in Python are:
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
"""

# ----- Arithmetic Operators -----

"""
Operator	        Description  	Example
+	                Addition	    5 + 3 → 8
-	                Subtraction	    5 - 3 → 2
*	                Multiplication  5 * 3 → 15
/	                Division	    5 / 2 → 2.5
//	                Floor Division	5 // 2 → 2
%	                Modulus         5 % 2 → 1 
**	                Exponentiation	2 ** 3 → 8 
"""
print("----------------------Arithmetic Operators------------------------------")
# Code for Arithmetic Operators
num1 = 12
num2 = 4
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)


# ----- Assignment Operators -----

"""
Operator  	Description	            Example
=	          Assign	            x = 5
+=	          Add & Assign        	x += 3 (same as x = x + 3)
-=	          Subtract & Assign	    x -= 2
*=	          Multiply & Assign	    x *= 2
/=	          Divide & Assign	    x /= 2
%=	          Modulus & Assign   	x %= 2
**=           Exponentiate & Assign	x **= 2
//=	          Floor Divide & Assign	x //= 2
"""
print("----------------------Assignment Operators------------------------------")
# Code for Assignment Operators
val = 15
val += 3  # val = val + 3
print("After +=:", val)
val *= 2  # val = val * 2
print("After *=:", val)
val //= 4  # val = val // 4
print("After //=:", val)


# ----- Comparison Operators -----

""" 
Operator	Description     	Example
==	        Equal to	        5 == 3 → False
!=	        Not equal to     	5 != 3 → True
>	        Greater than	    5 > 3 → True
<	        Less than        	5 < 3 → False
>=	        Greater or equal	5 >= 5 → True
<=	        Less or equal   	3 <= 5 → True  
"""
print("----------------------Comparison Operators------------------------------")
# Code for Comparison Operators
age1 = 25
age2 = 18
print("Equal:", age1 == age2)
print("Not Equal:", age1 != age2)
print("Greater Than:", age1 > age2)
print("Less Than:", age1 < age2)
print("Greater or Equal:", age1 >= age2)
print("Less or Equal:", age1 <= age2)


# ----- Logical Operators -----

"""
Operator	 Description	                                      Example
and	         Returns True if both conditions are true	         (5 > 3) and (8 > 5) → True
or	         Returns True if at least one condition is true	     (5 > 3) or (8 < 5) → True
not          Reverses the result	                             not(5 > 3) → False 
"""
print("----------------------Logical Operators------------------------------")
# Code for Logical Operators
status1 = True
status2 = False
print("Logical AND:", status1 and status2)
print("Logical OR:", status1 or status2)
print("Logical NOT:", not status1)


# ----- Identity Operators -----

"""
Operator	Description                                                	Example
is	        Returns True if both variables refer to the same object  	x is y
is not	    Returns True if variables refer to different objects	    x is not y 
"""
print("----------------------Identity Operators------------------------------") 
# Code for Identity Operators
list1 = ["apple", "banana", "cherry"]
list2 = list1  
list3 = ["apple", "banana", "cherry"]  
print("list1 is list2:", list1 is list2)  
print("list1 is list3:", list1 is list3)  
print("list1 is not list3:", list1 is not list3) 


# ----- Membership Operators -----

"""
Operator	Description	                                 Example
in	        Returns True if value exists in sequence	'a' in 'apple'
not in	    Returns True if value does not exist	    'z' not in 'apple' 
"""
print("----------------------Membership Operators------------------------------")
# Code for Membership Operators
fruits = ["apple", "orange", "grape", "mango"]
print("Mango in list:", "mango" in fruits)  
print("Pineapple not in list:", "pineapple" not in fruits)  


# ----- Bitwise Operators -----

"""
Operator	Description	      Example (a=5, b=3)
&	        AND	              5 & 3 → 1
|		    OR	              5 | 3 → 7
^	        XOR	              5 ^ 3 → 6
~	        NOT	              ~5 → -6
<<        	Left Shift	      5 << 1 → 10
>>	        Right Shift	      5 >> 1 → 2
"""
print("----------------------Bitwise Operators------------------------------")
# Code for Bitwise Operators
numA = 6  
numB = 2  
print("Bitwise AND:", numA & numB)
print("Bitwise OR:", numA | numB)
print("Bitwise XOR:", numA ^ numB)
print("Bitwise NOT:", ~numA)
print("Left Shift:", numA << 1)
print("Right Shift:", numA >> 1)

print("-----------------------------------------------------------------------")
