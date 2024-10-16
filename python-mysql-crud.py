import mysql.connector


def create(cursor):
    itemname = input("Enter item name: ")
    itemdescription = input("Enter item description: ")

    sql ="INSERT INTO items (itemname, itemdescription) VALUES (%s, %s)"
    cursor.execute(sql, (itemname, itemdescription))
    print("Item added successfully!")


def read(cursor):
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")


def update(cursor):
    item_id = int(input("Enter item ID to update: "))
    itemname = input("Enter new item name: ")
    itemdescription = input("Enter new item description: ")

    cursor.execute("UPDATE items SET itemname = %s, itemdescription = %s WHERE id = %s", (itemname, itemdescription, item_id))
    print("Item updated successfully!")


def delete(cursor):
    item_id = int(input("Enter item ID to delete: "))
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    print("Item deleted successfully!")


def main():

    db = mysql.connector.connect(host='localhost',user='root',password='',database='test')
    cursor = db.cursor()

    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create(cursor)
            db.commit()
        elif choice == '2':
            read(cursor)
        elif choice == '3':
            update(cursor)
            db.commit()
        elif choice == '4':
            delete(cursor)
            db.commit()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    db.close()

main()
