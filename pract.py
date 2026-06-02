def guess(value):
    for cast in (int,float):
        try:
            return type(cast(value))
            break
        except ValueError:
            pass
    if value.lower() in ("true","false"):
        return bool
    return str

    

value=input(f"Enter the value:")

x=guess(value)
print(x)