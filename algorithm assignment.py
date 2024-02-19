import time

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id, self.name, self.price, self.category = product_id, name, float(price), category

class ProductList:
    def __init__(self):
        self.products = []

    def insert(self, product_data):
        self.products.append(Product(*product_data))

    def display(self):
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    def search_by_id(self, product_id):
        return next((product for product in self.products if product.product_id == product_id), None)

    def update(self, product_id, new_price):
        product = self.search_by_id(product_id)
        if product:
            product.price = float(new_price)
            print(f"Product with ID {product_id} updated.")
        else:
            print(f"Product with ID {product_id} not found.")

    def delete(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]
        print(f"Product with ID {product_id} deleted.")

    def bubble_sort(self):
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]

def time_sorting_alg(sorting_func, product_list):
    start_time = time.time()
    sorting_func()
    end_time = time.time()
    return end_time - start_time

def main():
    product_list = ProductList()

    with open("product_data.txt", "r") as file:
        for line in file:
            product_data = line.strip().split(",")
            product_list.insert(product_data)

    print("Original Product List:")
    product_list.display()
    print("\n")

    product_list.insert(["101", "New Product", "25.99", "Electronics"])
    print("After Insertion:")
    product_list.display()
    print("\n")

    product_list.update("101", "29.99")
    print("After Update:")
    product_list.display()
    print("\n")

    product_list.delete("101")
    print("After Deletion:")
    product_list.display()
    print("\n")
  
    sorted_time = time_sorting_alg(product_list.bubble_sort, product_list)
    print(f"Bubble Sort Time: {sorted_time:.6f} seconds")

if __name__ == "__main__":
    main()
