def display_items(stock):
  print("Items:")
  for (item, quantity) in stock.items():
    if quantity > 0:
      print(f"- {item} ({quantity})")
    else:
      print(f"- {item} (Out of stock)")

def get_user_choice(stock):
  user_choice = {}
  while True:
    item = input("Enter item name (or 'exit' to finish): ").lower()
    if item == "exit":
      break
    if item not in stock:
      print(f"Item '{item}' not available.")
      continue
    quantity = int(input(f"Enter quantity for {item} (max: {stock[item]}): "))
    if quantity <= 0 or quantity > stock[item]:
      print("Invalid quantity. Please enter a positive value less than or equal to the available stock.")
      continue
    user_choice[item] = quantity
    stock[item] -= quantity
  return user_choice

def calculate_bill(user_choice, price):
  total_bill = 0
  for item, quantity in user_choice.items():
    total_bill += quantity * price[item]
  return total_bill

def display_remaining_stock(stock):
  print("\nRemaining stock:")
  for item, quantity in stock.items():
    if quantity > 0:
      print(f"- {item} ({quantity})")


if __name__ == "__main__":
    stock = {"shirt": 5, "pants": 3, "hat": 2, "book": 0}
    price = {"shirt": 20, "pants": 30, "hat": 15, "book": 10}
    
    display_items(stock.copy())

    user_choice = get_user_choice(stock.copy()) 

    if user_choice:
        bill_amount = calculate_bill(user_choice, price)
        print("\nBill:")
        for item, quantity in user_choice.items():
            print(f"- {item} x {quantity} ({price[item]} each): {quantity * price[item]} INR.")
        print(f"Total: {bill_amount} INR")
        display_remaining_stock(stock)
    else:
        print("No items purchased.")
