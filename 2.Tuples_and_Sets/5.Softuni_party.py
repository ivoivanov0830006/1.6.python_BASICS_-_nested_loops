number_guests = int(input())

vip = set()
regular = set()

for _ in range(number_guests):
    guest = input()
    guest_type = guest[0]
    if guest_type.isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

while True:
    command = input()
    if command == "END":
        break
    guest_type = command[0]
    if guest_type.isdigit():
        vip.discard(command)
    else:
        regular.discard(command)

print(len(vip.union(regular)))
print("\n".join(sorted(vip)))
print("\n".join(sorted(regular)))


# ------------------------------------- Problem to resolve ------------------------------
#
# There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP.
# When a guest comes, check if they exist in any of the two reservation lists.
# On the first line, you will receive the number of guests – N. On the following N lines, you will be
# receiving their reservation codes. All reservation codes are 8 characters long, and all VIP numbers
# will start with a digit. Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of guests who did not come to the party and their reservation numbers:
# The VIP guests must be first.
# Both the VIP and the Regular guests must be sorted in ascending order.
# -------------------------------------- Example inputs ----------------------------------
# Input	                    Output
# 5                         2
# 7IK9Yo0h                  7IK9Yo0h
# 9NoBUajQ                  tSzE5t0p
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END
# ---------------------------------------------
# 6                         3
# m8rfQBvl                  7ugX7bm0
# fc1oZCE0                  UgffRkOn
# UgffRkOn                  m8rfQBvl
# 7ugX7bm0
# 9CQBGUeJ
# 2FQZT3uC
# 2FQZT3uC
# 9CQBGUeJ
# fc1oZCE0
# END