import json
import time

products = []
cart = []

def welcome_screen():
    print(r"""
    ***************************************
    *      WELCOME TO ONLINE SHOP        *
    *         Python Shop v1.0           *
    ***************************************
    """)
    time.sleep(2)

def main_menu():
    print("""
    ======= MAIN MENU =======
    1. Add Product (Admin)
    2. View All Products
    3. Search Product
    4. Add to Cart
    5. View Cart
    6. Remove from Cart
    7. Checkout
    8. Apply Discount
    9. Save Products to File
    10. Load Products from File
    11. Help / Instructions
    0. Exit
    =========================
    """)

def add_product():
    try:
        product = {
            "id": input("Enter Product ID: "),
            "name": input("Enter Product Name: "),
            "price": float(input("Enter Price: ")),
            "stock": int(input("Enter Stock Quantity: "))
        }
        products.append(product)
        print(" Product added successfully!")
    except ValueError:
        print(" Error: Price must be a number and Stock must be an integer!")

def view_products():
    if not products:
        print(" No products available.")
    else:
        print("\n{:<10}{:<20}{:<10}{:<10}".format("ID", "Name", "Price", "Stock"))
        for p in products:
            print("{:<10}{:<20}{:<10.2f}{:<10}".format(p["id"], p["name"], p["price"], p["stock"]))

def search_product():
    keyword = input("Enter product ID or name to search: ").lower()
    found = [p for p in products if keyword in p["id"].lower() or keyword in p["name"].lower()]
    if found:
        for p in found:
            print(f" Found: {p['name']} (ID: {p['id']}), Price: ${p['price']:.2f}")
    else:
        print(" Product not found.")

def add_to_cart():
    pid = input("Enter Product ID to add to cart: ")
    for p in products:
        if p["id"] == pid:
            quantity = int(input(f"Enter quantity (Max {p['stock']}): "))
            if quantity <= p["stock"]:
                cart.append({"id": p["id"], "name": p["name"], "price": p["price"], "quantity": quantity})
                p["stock"] -= quantity  # Update stock
                print(f" {quantity}x {p['name']} added to cart!")
            else:
                print(" Not enough stock!")
            return
    print(" Product ID not found.")

def view_cart():
    if not cart:
        print(" Your cart is empty.")
    else:
        total = 0
        print("\n{:<10}{:<20}{:<10}{:<10}{:<10}".format("ID", "Name", "Price", "Qty", "Subtotal"))
        for item in cart:
            subtotal = item["price"] * item["quantity"]
            total += subtotal
            print("{:<10}{:<20}{:<10.2f}{:<10}{:<10.2f}".format(
                item["id"], item["name"], item["price"], item["quantity"], subtotal))
        print(f"\n Total: ${total:.2f}")

def checkout():
    if not cart:
        print(" Cart is empty. Add items first!")
        return
    view_cart()
    confirm = input("Confirm purchase? (yes/no): ").lower()
    if confirm == "yes":
        print(" Order placed successfully! Thank you for shopping.")
        cart.clear()
    else:
        print(" Checkout cancelled.")

def apply_discount():
    discount_code = input("Enter discount code (TRY 'PYTHON10' for 10% off): ")
    if discount_code == "PYTHON10":
        total = sum(item["price"] * item["quantity"] for item in cart)
        discounted = total * 0.9
        print(f" Discount applied! New total: ${discounted:.2f} (Saved: ${total - discounted:.2f})")
    else:
        print(" Invalid discount code.")

def save_products():
    with open("products.json", "w") as f:
        json.dump(products, f)
    print(" Products saved to 'products.json'.")

def load_products():
    global products
    try:
        with open("products.json", "r") as f:
            products = json.load(f)
        print(" Products loaded successfully.")
    except FileNotFoundError:
        print(" No saved products file found.")
    except json.JSONDecodeError:
        print(" File is corrupted.")

def help_menu():
    print("""
     Instructions:
    - Admin: Use 'Add Product' to add new items.
    - Customers: Search products, add to cart, and checkout.
    - Discount Code: 'PYTHON10' gives 10% off.
    - Always save changes before exiting.
    """)

def main():
    welcome_screen()
    while True:
        main_menu()
        choice = input("Choose an option: ")
        match choice:
            case "1": add_product()
            case "2": view_products()
            case "3": search_product()
            case "4": add_to_cart()
            case "5": view_cart()
            case "6": print("🚧 (Remove from cart function coming soon!)")
            case "7": checkout()
            case "8": apply_discount()
            case "9": save_products()
            case "10": load_products()
            case "11": help_menu()
            case "0":
                print(" Goodbye! Visit us again.")
                break
            case _: print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
