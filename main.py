
products = {
    '7675864382017': {'name': 'Hoodies/Sweaters', 'price': 6.00, 'quantity_sold': 0, 'total_earnings': 0.0},
    '1053234896276': {'name': 'T-Shirts', 'price': 2.00, 'quantity_sold': 0, 'total_earnings': 0.0},
    '897624524602': {'name': 'Flannels', 'price': 4.00, 'quantity_sold': 0, 'total_earnings': 0.0}, 
    '7999500063161': {'name': 'Shorts', 'price': 4.00, 'quantity_sold': 0, 'total_earnings': 0.0},
    '3059287682147': {'name': 'Pants', 'price': 6.00, 'quantity_sold': 0, 'total_earnings': 0.0},
    '6354858249024': {'name': 'Kids Pants', 'price': 2.00, 'quantity_sold': 0, 'total_earnings': 0.0},
    '4499626976541': {'name': 'Kids Shirts', 'price': 2.00, 'quantity_sold': 0, 'total_earnings': 0.0},
    '8757653415942': {'name': 'Coats or Jackets', 'price': 4.00, 'quantity_sold': 0, 'total_earnings': 0.0}
    }

def update_product_sales(barcode):
    if barcode in products:
        product = products[barcode]
        product['quantity_sold'] += 1
        product['total_earnings'] += product['price']
        print(f"Sold 1 of {product['name']}. Total earnings: ${product['total_earnings']:.2f}")
    else:
        print("Product not found.")

def main():
    while True:
        barcode = input("Scan barcode (type 'stop' to end): ")
        if barcode.lower() == 'stop':
            break

        update_product_sales(barcode)

    # Print summary of sales
    print("\nSummary of Sales:")
    total_quantity = total_earnings = 0
    for product in products.values():
        print(f"{product['name']}: Sold {product['quantity_sold']}, Earnings: ${product['total_earnings']:.2f}")
        total_quantity += product['quantity_sold']
        total_earnings += product['total_earnings']
    print(f"\nTotal Products Sold: {total_quantity}, Total Income: ${total_earnings:.2f}")

if __name__ == "__main__":
    main()
