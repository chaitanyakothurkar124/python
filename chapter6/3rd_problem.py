names = ["Alice", "Bob", "Charlie", "David", "Eve" , "Frank", "Grace", "Heidi", "Ivan", "Judy"]
verification = input("Enter a name: ")
if verification in names:
    print("Name is present in the list.")
elif verification.lower() in [name.lower() for name in names]:
    print("Name is present in the list.")
else:
    print("Name is not present in the list.")