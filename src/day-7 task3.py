filename = input("Enter the filename to open: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("\nFile contents:\n")
        print(content)

except FileNotFoundError:
<<<<<<< HEAD
    print("Oops! That file doesn't exist yet 😅")
=======
    print("Oops! That file doesn't exist yet 😅")
>>>>>>> 5078fcc88d7aebc08da7b8392d5674892e302cea
