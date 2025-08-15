def is_valid_for_vote(age):
    """Return True if age is 18 or older, else False."""
    return age >= 18

# Example usage:
user_age = int(input("Enter your age: "))
if is_valid_for_vote(user_age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

for n in range(1,10):
    print("Hello world",n*5)

