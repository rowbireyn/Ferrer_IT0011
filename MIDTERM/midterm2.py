months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
m, d, y = input("Enter the date (mm/dd/yyyy): ").split("/")
print(f"Date Output: {months[int(m)-1]} {int(d)}, {y}")