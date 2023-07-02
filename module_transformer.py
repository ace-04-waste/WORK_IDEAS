def transform_serial_number(serial_number):
    # Remove the first and last characters (letters)
    middle_part = serial_number[1:-1]

    # Split the middle part at position 4
    first_chunk = middle_part[:4]
    second_chunk = middle_part[4:]

    # Combine the transformed chunks
    transformed_serial_number = 'E6S0' + second_chunk + first_chunk

    return transformed_serial_number

# Example usage
serial_number = input("enter your serial number")
transformed_number = transform_serial_number(serial_number)
print(transformed_number)
