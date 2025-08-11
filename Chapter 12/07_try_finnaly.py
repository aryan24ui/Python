def main():
    try:
        a = int(input("Hey, Enter the number : "))
        print(a)
        return a
    
    except Exception as e:
        print(e)
        return
    
    finally:    # chalega hi chalega
        print("I am inside finally")

main()