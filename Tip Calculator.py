# Tip Calculator

# Step 1: Get inputs
bill_amount = float(input("Enter the bill amount: $"))
tip_percent = float(input("Enter tip percentage (e.g., 15 for 15%): "))

# Step 2: Calculate tip
tip = (tip_percent / 100) * bill_amount

# Step 3: Calculate total
total = bill_amount + tip

# Step 4: Show results
print("\n--- Bill Summary ---")
print(f"Bill Amount: ${bill_amount:.2f}")
print(f"Tip ({tip_percent}%): ${tip:.2f}")
print(f"Total Amount: ${total:.2f}")