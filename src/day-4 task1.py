# Step 1: Create a dictionary with at least three contacts
contacts = {
    "Jyothi": "8746001575",
    "Hitha": "9591607129",
    "Charlie": "9001122334"
}

contacts["Diana"] = "9988776655"

contacts["Hitha"] = "9591607129"

existing_contact = contacts.get("jyothi", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")

print("Safe Lookup Results:")
print("Jyothi:", existing_contact)
print("Eve:", missing_contact)

print("\nContact List:")

for name, phone in contacts.items():
<<<<<<< HEAD
    print(f"Contact: {name} | Phone: {phone}")
=======
    print(f"Contact: {name} | Phone: {phone}")
>>>>>>> 5078fcc88d7aebc08da7b8392d5674892e302cea
