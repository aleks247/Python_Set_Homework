invitations = set(input("Enter how many invitations you want to send: ") for _ in range(int(input())))
arrived_guests = set()

while True:
    command = input()
    if command.lower() == "end":
        break
    arrived_guests.add(command)

missing_guests = sorted(invitations.difference(arrived_guests))

teachers_missing = [guest for guest in missing_guests if guest[0].isdigit()]
students_missing = [guest for guest in missing_guests if not guest[0].isdigit()]

print(len(missing_guests))
print("\n".join(teachers_missing + students_missing))
