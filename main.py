def father(some):
    def use(things):
        print("father")
        print(things)
        # some()

    return use


@father
def son(x):
    print("son")
    print("son : ", x)


son("传入参数-1")
