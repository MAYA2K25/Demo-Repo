def oper(a,b):
   if not isinstance(a, (int,float)):
      raise TypeError(f"The value entered for a is not an integer,we got {type(a).__name__}")
   if not isinstance(b, (int,float)):
      raise TypeError(f"The value entered for b is not an integer,we got {type(b).__name__}")
   if b==0:
      raise ValueError("As b is zero value operation cannot be performed")
   
   return a+b,a/b,a*b


try:
   a= float(input("Enter value for a:"))
   b=float(input("Enter value for b:"))

   result=oper(a,b)
   print(f"Addition value for oper is {result[0]}")
   print(f"Division value for oper is {result[1]}")
   print(f"Multiplication value for oper is {result[2]}")


except TypeError as e:
    print(f"Type error: {e}")

except ValueError as e:
    print(f"Value error: {e}")

except Exception as e:
    print(f"Something went wrong: {e}")