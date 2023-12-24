import psycopg2

def fetch_data(action):
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="postgres",
            password="mysecretpassword"
        )

        cursor = connection.cursor()

        if action == 1:
            table_name = "urunler"
        elif action == 2:
            table_name = "kategoriler"
        elif action == 3:
            table_name = "ureticiler"
        elif action == 4:
            table_name = "stok_hareketleri"
        else:
            print("Invalid action. Please choose a number between 1 and 4.")
            return

        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)

        rows = cursor.fetchall()

        # Display fetched data
        for row in rows:
            print(row)

        # Ask the user if they want to update the data
        update_choice = input("Do you want to update this data? (yes/no): ")
        if update_choice.lower() == 'yes':
            # Ask user for new data column by column
            new_data = {}
            for column in range(len(rows[0])):  # Assuming all rows have the same number of columns
                column_name = input(f"Enter value for column '{cursor.description[column][0]}': ")
                new_data[cursor.description[column][0]] = column_name
            
            # Insert new data into the table
            columns = ', '.join(new_data.keys())
            values = ', '.join(["'" + str(value) + "'" for value in new_data.values()])
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            cursor.execute(insert_query)
            connection.commit()
            print("New data added successfully!")
        else:
            print("No updates performed.")

        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)

# Ask the user for action input
user_input = input("Enter the number for the action you want to perform:\n1) Fetch products\n2) Fetch categories\n3) Fetch producers\n4) Fetch stock movements\n")

try:
    action = int(user_input)
    fetch_data(action)
except ValueError:
    print("Please enter a valid number.")
