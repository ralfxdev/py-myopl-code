import basic

while True:
    text = input('test > ')
    resulst, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(resulst)
