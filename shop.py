
import csv
import os

FILE_NAME = "medicines.csv"
medicines = []


# Load medicines from CSV
def load_data():
    global medicines
    medicines = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                medicines.append({
                    "ID": row["ID"],
                    "Name": row["Name"],
                    "Quantity": int(row["Quantity"]),
                    "Price": float(row["Price"])
                })


# Save medicines to CSV
def save_data():
    with open(FILE_NAME, "w", newline="") as file:
        fields = ["ID", "Name", "Quantity", "Price"]
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(medicines)


# Generate next medicine ID
def generate_id():
    numbers = []

    for medicine in medicines:
        numbers.append(int(medicine["ID"][1:]))

    next_number = max(numbers, default=0) + 1
    return "M" + str(next_number)


# Add medicine
def add_medicine():
    name = input("Name: ").strip()

    if not name:
        print("Invalid medicine name.")
        return

    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Enter valid numbers.")
        return

    medicine_id = generate_id()

    medicine = {
        "ID": medicine_id,
        "Name": name,
        "Quantity": quantity,
        "Price": price
    }

    medicines.append(medicine)
    save_data()

    print(
        f"Medicine added. ID: {medicine_id} | "
        f"{name} | Qty: {quantity} | Price: {price:.2f}"
    )


# View all medicines
def view_medicines():
    if not medicines:
        print("No medicines available.")
        return

    print("\n--- Medicine Stock ---")

    for medicine in medicines:
        print(
            f'{medicine["ID"]} | {medicine["Name"]} | '
            f'Qty: {medicine["Quantity"]} | '
            f'Price: {medicine["Price"]:.2f}'
        )


# Sell medicine
def sell_medicine():
    medicine_id = input("ID: ").strip().upper()

    medicine = next(
        (m for m in medicines if m["ID"] == medicine_id),
        None
    )

    if medicine is None:
        print("Medicine not found.")
        return

    try:
        quantity = int(input("Quantity: "))

        if quantity <= 0:
            print("Enter a valid positive quantity.")
            return

    except ValueError:
        print("Invalid quantity.")
        return

    if quantity > medicine["Quantity"]:
        print(f'Insufficient stock. Available: {medicine["Quantity"]}')
        return

    bill = quantity * medicine["Price"]

    medicine["Quantity"] -= quantity
    save_data()

    print(f"Sold {quantity} units. Bill: {bill:.2f}")

    if medicine["Quantity"] == 0:
        print("Stock left: 0 | Out of stock!")
    else:
        print(f'Stock left: {medicine["Quantity"]}')


# Delete medicine
def delete_medicine():
    medicine_id = input("ID: ").strip().upper()

    for medicine in medicines:
        if medicine["ID"] == medicine_id:
            medicines.remove(medicine)
            save_data()
            print(f"Medicine {medicine_id} deleted.")
            return

    print("Medicine not found.")


# Low stock report
def low_stock_report():
    print("\n--- Low Stock Report ---")

    found = False

    for medicine in medicines:
        if medicine["Quantity"] < 10:
            print(
                f'{medicine["ID"]} | {medicine["Name"]} | '
                f'Qty: {medicine["Quantity"]} (Low stock)'
            )
            found = True

    if not found:
        print("No low stock medicines.")


# Calculate inventory value
def inventory_value():
    total = 0

    for medicine in medicines:
        total += medicine["Quantity"] * medicine["Price"]

    print(f"Total inventory value: {total:.2f}")


# Main menu
def main():
    load_data()

    while True:
        print("\n===== PHARMACY INVENTORY SYSTEM =====")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Sell Medicine")
        print("4. Delete Medicine")
        print("5. Low Stock Report")
        print("6. Inventory Value")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_medicine()

        elif choice == "2":
            view_medicines()

        elif choice == "3":
            sell_medicine()

        elif choice == "4":
            delete_medicine()

        elif choice == "5":
            low_stock_report()

        elif choice == "6":
            inventory_value()

        elif choice == "7":
            print("Thank you for using Pharmacy Inventory System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
