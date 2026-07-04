import sqlite3
class Contact:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name.capitalize()
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"name: {self.name} email: {self.email} phone: {self.phone}"

class ContactBook:
    def __init__(self):
        self.conn = sqlite3.connect("contacts.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT
            )
            """)
        self.conn.commit()

    def add_contact(self, contact):
        self.cur.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (contact.name, contact.email, contact.phone))
        self.conn.commit()
        print("Contact added")

    def find_contact(self, name):
        self.cur.execute("SELECT id, * FROM contacts WHERE name LIKE ?", (f"%{name}%",))
        row = self.cur.fetchone()
        if row is not None:
            print(" | ".join([str(data) for data in row[1:]]))
        else:
            print("Contact not found")

    def show_all(self):
        print("ID | NAME | EMAIL | PHONE")
        self.cur.execute("SELECT * FROM contacts")
        items = self.cur.fetchall()
        for item in items:
            print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")

    def delete_contact(self, contact_id):
        self.cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        self.conn.commit()
        print("Contact deleted")

    def update_contact(self, contact_id, **kwargs):
        columns = ", ".join(f"{key}=?" for key in kwargs if kwargs[key])
        values = list(i for i in kwargs.values() if i)
        values.append(contact_id)
        self.cur.execute(f"UPDATE contacts SET {columns} WHERE id=?", values)
        self.conn.commit()
        print("Contact updated")


def main():
    conn_book = ContactBook()
    while True:
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Show all")
        print("4. Find contact")
        print("5. Update contact")
        print("6. Quit")
        choice = input("Enter choice (1-6): ")
        match choice:
            case "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                if not "@" in email:
                    print("email must contain a '@' character")
                    continue
                phone = input("Enter phone: ")
                if not phone.isdigit():
                    print("Phone number must contain digits only")
                    continue
                conn_book.add_contact(Contact(name, email, phone))
            case "2":
                row_id = input("Enter row ID: ")
                if not row_id.isdigit():
                    print("ID must be a digit")
                    continue
                conn_book.delete_contact(row_id)
            case "3":
                conn_book.show_all()
            case "4":
                name = input("Enter name: ")
                conn_book.find_contact(name)
            case "5":
                row_id = input("Enter row ID: ")
                print("Leave blank to keep existing value")
                new_name = input("Enter name: ").strip()
                new_email = input("Enter email: ").strip()
                if new_email:
                    if not "@" in new_email:
                        print("email must contain a '@' character")
                        continue
                new_phone = input("Enter phone: ").strip()
                if new_phone:
                    if not new_phone.isdigit():
                        print("Phone number must contain digits only")
                        continue
                conn_book.update_contact(row_id, name=new_name, email=new_email, phone=new_phone)
            case "6":
                conn_book.conn.close()
                break
if __name__ == "__main__":
    main()