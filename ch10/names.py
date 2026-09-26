from name_func import get_formatted_name

print("enter 'q' at any time to quit.")
while True:
    first = input("\nplease input your first name:")
    if first == "q":
        break
    last = input("please give me a last name:")
    if last == "q":
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tneatly formatted name: {formatted_name}")
