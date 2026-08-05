#สร้างรายชื่อผู้ใช้และรหัสผ่าน
user_credentials = {
    'admin1': 'password1',
    'admin2': 'password2'
}
#สร้างฐานข้อมูลสำหรับเก็บข้อมูลสินค้า
storage = {
    '1001': {'name': 'Hummer', 'price': 5, 'stock': 3},
    '1002': {'name': 'Scissors', 'price': 2, 'stock': 5},
    '1003': {'name': 'Paper', 'price': 1, 'stock': 10}
}

#List รายการขาย 
sales_history = []
#Function การทำงานของการเข้าถึงตัวโปรแกรมโดยผ่านกาารยืนยันต้วตนด้วย username และ password.
def authenticate(username, password):
    if username in user_credentials and user_credentials[username] == password:
        return True
    return False
#Function การเพิ่มสินค้าเข้ามาใหม่โดยการใส่ค่าลงไปให้ตรงกับตัวแปร
def add_item():
  name = input("Enter the item name : ")
  price = float(input("Enter the item price : "))
  stock = int(input("Enter the initial stock level : "))

  # สร้างรายการใหม่พร้อมรายละเอียดที่ให้ไว้
  new_item = {
    "name": name,
    "price": price,
    "stock": stock
}
#Function แสดงสินค้าที่อยู่ในตัวแปร storage
def display_storage():
    print("Storage stock list :")
    for item_id, item_info in storage.items():#ใช้ for loop เพื่อแสดง item_id,item_info ที่ถูกเก็บไว้ในตัวแปร name,price,stock ออกมา
        print(f"{item_id}: {item_info['name']} - Price: {item_info['price']} $ - Inventory: {item_info['stock']} piece")

# หลักๆคือ ไว้คำนวนของที่เลือกมาแบบซื้อ paper ให้ใส่ ID ของ paper คือ 1003 แล้วให้ใส่จำนวนที่ต้องการเสร็จแล้วจะนำมาเก็บใว้ใน cart แล้วกลับมาทำงานใน while loop ต่อ
# ถ้าซื้อ hummer เพิ่มอีก 1 ก็เอานำมาเก็บไว้ใน cart แล้วกลับมาทำงานใน while loop ต่อ ถ้าต้องการสิ้นสุกการซื้อให้กด Y จะนำตัวแปรที่ถูกเก็บไว้ใน cart มาคำนวนออกมาเป็น total_price
def make_sale():
    display_storage()
    total_price = 0
    cart = {}   #ตะกร้า

    while True:
        item_id = input("Enter Item ID (Or type 'Y' to complete the sale) : ")
        if item_id == 'Y':
            break
        
        if item_id not in storage:
            print("Item ID is broken...")
            continue
        
        quantity = int(input(f"Enter quantity {storage[item_id]['name']}: "))
        
        if quantity > storage[item_id]['stock']:
            print("Out of stock")
            continue
        
        cart[item_id] = quantity
        total_price += storage[item_id]['price'] * quantity
        storage[item_id]['stock'] -= quantity #ตรงนี้คือการลบของที่อยู่ใน stock 
    
    if cart:
        sales_history.append(cart)
        print(f"Total : {total_price} $")
        print("The sale is complete.")

def view_sales_history():
    print("History of sale:")
    for index, sale in enumerate(sales_history, 1):
        print(f"Object {index}: {sale}")

#เพิ่ม stock 
def update_stock(storage):
    item_id = input("Enter the ID of the item you want to update: ")
    if item_id in storage:
        units = int(input("Enter the number of units you want to add or subtract : "))

        # ตรวจสอบว่าผู้ใช้ต้องการเพิ่มหรือลบ
        action = input("Do you want to add or delete (enter 'add' or 'delete') : ").lower()

        if action == 'add':
            storage[item_id]['stock'] += units
        elif action == 'delete':
            if storage[item_id]['stock'] >= units:
                storage[item_id]['stock'] -= units
            else:
                print("Out of stock")
        else:
            print("Plase enter 'add' or 'delate'")
        
        print("Item level updated! Current product levels are : ", storage[item_id]['stock'])
    else:
        print("ID is incorrect.")

    return storage

while True:
    print("="*35)
    print("|   Program Point of Sale : POS   |")
    print("="*35)
    username = input("Username : ")
    password = input("Password : ")
    print("="*35)
    if authenticate(username, password):
        print("Login Succeed.")

        while True:
          print("="*35)
          print("|   Program Point of Sale : POS   |")
          print("="*35)
          print("|1. Display Storage stock list    |")
          print("|2. Save list Product Sales       |")
          print("|3. Add an item to the menu       |")
          print("|4. View History of sale          |")
          print("|0. Exit                          |")
          print("="*35)
          choice = input("Enter your choice : ")
          
          if choice == '1':
              display_storage()
          elif choice == '2':
              make_sale()
          elif choice == '3':
              add_item()
          elif choice == '4':
              view_sales_history()
          elif choice == '5':
              update_stock(storage)
          elif choice == '0':
              print("Exit Program . . .")
              break    
          else:
              print("Please select the correct transaction.")
    else:
      print("Login failed : Invalid username or password.")    