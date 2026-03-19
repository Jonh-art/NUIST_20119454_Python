studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
print("Original Student List:")
for name in studentNames:
    print(f"{name} Evans")
print("\n------------------------")
new_name = input("\nEnter a new first name to add to the list: ")
studentNames.append(new_name)
