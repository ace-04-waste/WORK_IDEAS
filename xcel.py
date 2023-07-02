from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()

# Select the active sheet
sheet = workbook.active

# Add data to the spreadsheet
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["A2"] = "John"
sheet["B2"] = 25
sheet["A3"] = "Alice"
sheet["B3"] = 30

# Save the workbook
workbook.save("my_spreadsheet.xlsx")
