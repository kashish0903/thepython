# Names
# store names of friends in a list
names = ['Alice', 'Bob', 'Charlie', 'Diana']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# greetings
names = ['Alice', 'Bob', 'Charlie', 'Diana']
print(f"hello,{names[0]}! how are you today?")
print(f"hello,{names[1]}! how are you today?")
print(f"hello,{names[2]}! how are you today?")
print(f"hello,{names[3]}! how are you today?")

# your ownlist
# list of favorite transportation
cars = ['Tesla', 'BMW', 'Audi', 'Toyota']
print(f"I love this {cars[0]}! car for automation")
print(f"I love this {cars[1]}! car for engine&style")
print(f"I love this {cars[2]}! car for looks")
print(f"I love this {cars[3]}! car for strong body part")

# changing guest list
guests = ['Albert Einstein', 'Marie Curie', 'Lenardo da vinci']
# print who cannot make it
print(f"\n {guests[1]} can't make the dinner.")
# replace the guest
guests[1] = 'Isaac Newton'
# print new invitation
print(f"\n Dear {guests[0]},you are invited for dinner!")
print(f"\n Dear {guests[1]},you are invited for dinner!")
print(f"\n Dear {guests[2]},you are invited for dinner!")
# add guest
guests.insert(0, 'Nikola Tesla')
guests.insert(2, 'ada lovelace')
guests.append("Stephen Hawking")
for guest in guests:
    print(f"\n Dear {guest},you are invited to dinner!")
    # shrinking guest list
    guests = ['Nikola Tesla', 'Albert Einstein', 'Marie Curie',
              'Lenardo da vinci', 'Isaac Newton', 'Stephen Hawking']
# remove guests until only two remaining guests
while len(guests) > 2:
    removed_guests = guests.pop(2)
    print(f"Sorry {removed_guests},I can't invite you to dinner.")
    # remaining guests
    print(f"\n Dear {guests[0]},you are still invited for dinner!")
    print(f"Dear {guests[1]},you are still invited for dinner!")
# final list of guest who are invited
print(f"Final guest list: {guests}")
