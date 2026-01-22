"""
Python Alchemy

Module:
chapters.chapter_06_reusable_code_magic.pizza_ordering_system

Mini Project: Pizza Ordering System with Return Values

Demonstrates:
    - Positional argument (size)
    - Default argument (crust)
    - *args (variable toppings)
    - **kwargs (extras like delivery, drinks, discounts)
    - return value (total bill)
"""


def order_pizza(size, crust="Regular", *toppings, **extras):
    """
    Simulates a pizza ordering system.

    Parameters:
    - size (str): Size of the pizza (Small, Medium, Large)
    - crust (str): Type of crust (Regular, Thin, Cheese Burst)
    - *toppings: Variable number of toppings
    - **extras: Additional options like delivery, drinks, discounts

    Returns:
    - float: Total bill amount
    """

    # Base price by size
    base_prices = {"Small": 6, "Medium": 8, "Large": 10}
    price = base_prices.get(size, 8)  # default Medium if invalid

    # Crust price (extra for fancy crusts)
    crust_prices = {"Regular": 0, "Thin": 1, "Cheese Burst": 2}
    price += crust_prices.get(crust, 0)

    # Add price for each topping
    topping_price = 1.5 * len(toppings)
    price += topping_price

    # Handle extras (**kwargs)
    if "drink" in extras:
        price += 2  # fixed price for drink
    if "delivery" in extras and extras["delivery"] == "Home Delivery":
        price += 3  # delivery charge

    # Apply discount if provided
    discount = 0
    if "discount" in extras:
        try:
            discount = int(extras["discount"].replace("%", ""))
            price = price - (price * discount / 100)
        except:
            pass  # ignore invalid discount format

    # Print order summary
    print(f"🍕 Order Summary:")
    print(f"- Size: {size}")
    print(f"- Crust: {crust}")
    print(f"- Toppings: {toppings if toppings else 'No extra toppings'}")
    print(f"- Extras: {extras if extras else 'None'}")
    print(f"💰 Total (after {discount}% discount): ${price:.2f}")
    print("✅ Order placed successfully!\n")

    return price  # returning the final bill


# --- Example Calls ---

# 1. Simple order
bill1 = order_pizza("Medium")
print("Returned Bill:", bill1, "\n")

# 2. Custom crust with toppings
bill2 = order_pizza("Large", "Thin", "Olives", "Mushrooms", "Peppers")
print("Returned Bill:", bill2, "\n")

# 3. With extras using **kwargs
bill3 = order_pizza("Large", "Cheese Burst", "Pepperoni", "Cheese",
                    delivery="Home Delivery", drink="Coke", discount="10%")
print("Returned Bill:", bill3, "\n")
