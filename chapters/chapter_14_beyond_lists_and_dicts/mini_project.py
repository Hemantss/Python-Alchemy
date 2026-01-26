from collections import Counter
import itertools
import heapq
import random


# --- Step 1: Simulating a Product Clickstream Dataset ---
def generate_clickstream(products, users, n=100):
    """
    Simulate a stream of user-product interactions.
    Each record: (user_id, product_name)
    """
    for _ in range(n):
        yield (random.choice(users), random.choice(products))


# --- Step 2: Aggregating and Grouping Data ---
def group_by_user(clickstream):
    """
    Group product views by user using itertools.groupby.
    """
    # Sort by user to group correctly
    sorted_stream = sorted(clickstream, key=lambda x: x[0])
    grouped = itertools.groupby(sorted_stream, key=lambda x: x[0])
    user_data = {}
    for user, items in grouped:
        products = [item[1] for item in items]
        user_data[user] = Counter(products)
    return user_data


# --- Step 3: Analyzing Global Trends ---
def get_global_trends(user_data, top_n=5):
    """
    Combine all user-level data and find top trending products globally.
    """
    global_counter = Counter()
    for counter in user_data.values():
        global_counter.update(counter)
    
    # Use heapq to efficiently extract top N products
    top_trending = heapq.nlargest(top_n, global_counter.items(), key=lambda x: x[1])
    return top_trending


# --- Step 4: Running the Pipeline ---
if __name__ == "__main__":
    products = ['Laptop', 'Headphones', 'Camera', 'Smartwatch', 'Keyboard', 'Mouse']
    users = ['U1', 'U2', 'U3', 'U4']

    # Generate simulated clickstream data
    clickstream = list(generate_clickstream(products, users, n=50))

    # Step 2: Group and count per user
    user_data = group_by_user(clickstream)

    # Step 3: Compute top trending items globally
    top_items = get_global_trends(user_data)

    print("=== User-Level Product Views ===")
    for user, counter in user_data.items():
        print(f"{user}: {dict(counter)}")

    print("\n=== Global Top Trending Products ===")
    for product, count in top_items:
        print(f"{product}: {count} views")