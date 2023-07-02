# Function to save the quotes to a file
def save_quotes(quotes):
    with open("quotes.txt", "w") as file:
        for tag, quote_info in quotes.items():
            file.write(f"Tag: {tag}\n")
            file.write(f"Quote: {quote_info['quote']}\n")
            file.write(f"Author: {quote_info['author']}\n")
            file.write(f"Date: {quote_info['date']}\n")
            file.write("\n")

# Function to load the quotes from the file
def load_quotes():
    quotes = {}
    with open("quotes.txt", "r") as file:
        lines = file.readlines()
        num_lines = len(lines)
        i = 0
        while i < num_lines:
            tag = lines[i].split(":")[1].strip()
            quote = lines[i+1].split(":")[1].strip()
            author = lines[i+2].split(":")[1].strip()
            date = lines[i+3].split(":")[1].strip()
            quotes[tag] = {
                "quote": quote,
                "author": author,
                "date": date
            }
            i += 5  # Move to the next set of lines
    return quotes

# Check if quotes file exists, if not, create an empty file
try:
    with open("quotes.txt", "x") as file:
        pass
except FileExistsError:
    pass

# Load existing quotes from the file
quotes = load_quotes()

while True:
    # Ask the user for input
    print("Enter a command: 'add', 'list', or 'done'")
    command = input("Command: ")

    # Check if the user wants to add a quote
    if command.lower() == "add":
        print("Enter a book quote (or 'done' to finish):")
        quote = input("Quote: ")

        # Check if the user wants to exit
        if quote.lower() == "done":
            break

        author = input("Author: ")
        date = input("Date: ")
        tag = input("Tag: ")

        # Store the quote information in the dictionary
        quotes[tag] = {
            "quote": quote,
            "author": author,
            "date": date
        }

        # Save the quotes to the file
        save_quotes(quotes)
        print("Quote added successfully.")

    # Check if the user wants to list all the tags
    elif command.lower() == "list":
        print("Tags:")
        for tag in quotes:
            print(tag)

    # Check if the user wants to exit
    elif command.lower() == "done":
        break

    # Invalid command
    else:
        print("Invalid command. Please try again.")

# Ask the user for a tag to retrieve a quote
while True:
    print("\nEnter a tag to retrieve a quote (or 'done' to exit):")
    tag = input("Tag: ")

    # Check if the user wants to exit
    if tag.lower() == "done":
        break

    # Retrieve the quote information from the dictionary
    if tag in quotes:
        quote_info = quotes[tag]
        print("Quote: ", quote_info["quote"])
        print("Author: ", quote_info["author"])
        print("Date: ", quote_info["date"])
    else:
        print("Tag not found. Please try again.")
