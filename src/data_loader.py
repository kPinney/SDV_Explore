import pandas as pd

def load_single_table_data(file_path='your_data.csv'):
    """
    Loads single table data from a CSV file.
    If the file is not found, it generates dummy data.
    """
    try:
        real_data = pd.read_csv(file_path)
        print(f"Single table data loaded successfully from {file_path}.")
        return real_data
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        print("Generating dummy single table data for demonstration.")
        data = {
            'id': range(100),
            'name': [f'User{i}' for i in range(100)],
            'age': [20 + (i % 50) for i in range(100)],
            'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'] * 20,
            'salary': [30000 + (i * 500) % 70000 for i in range(100)],
            'start_date': pd.to_datetime(pd.date_range(start='2023-01-01', periods=100, freq='D')),
            'end_date': pd.to_datetime(pd.date_range(start='2023-01-02', periods=100, freq='D'))
        }
        return pd.DataFrame(data)

def load_multi_table_data(table_paths=None):
    """
    Loads multi-table data from a dictionary of CSV file paths.
    If file paths are not provided or files are not found, it generates dummy data.
    """
    if table_paths:
        try:
            real_data_multi_table = {
                table_name: pd.read_csv(path) for table_name, path in table_paths.items()
            }
            print("Multi-table data loaded successfully.")
            return real_data_multi_table
        except FileNotFoundError as e:
            print(f"Error loading multi-table data: {e}")

    print("Generating dummy multi-table data for demonstration.")
    customers_data = {
        'customer_id': [1, 2, 3, 4],
        'customer_name': ['Alice', 'Bob', 'Charlie', 'David'],
        'city': ['New York', 'Los Angeles', 'Chicago', 'New York']
    }
    orders_data = {
        'order_id': [101, 102, 103, 104, 105],
        'customer_id': [1, 2, 1, 3, 2],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
        'price': [1200, 25, 75, 300, 50]
    }
    return {
        'customers': pd.DataFrame(customers_data),
        'orders': pd.DataFrame(orders_data)
    }
