
def fetch_shopify_orders():
    print("calling the shopify api to get orders placed via shopify")

def fetch_order_tags(order_id):
    print(f"fetching order tags for order_id {order_id}...")
    return ['whatsapp', 'new-customer', 'spender']

if __name__ == "__main__":
    fetch_shopify_orders()
