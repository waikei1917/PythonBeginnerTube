

while True:
    try:
        number = int(input("what is the number? \n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure you input the number.")
    except ZeroDivisionError:
        print("No Zero")
    except:
        break
    finally:
        print("loop completed")