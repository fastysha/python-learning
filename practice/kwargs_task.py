def foo(**kwargs) -> dict:
    print(dict(**kwargs))



foo(user='Radik', sex='Male', age=21, is_itshnik=True)# {user:Radik, age:21, sex:Male, is_itshnik:True}