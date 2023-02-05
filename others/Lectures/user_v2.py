# Create a user class
class User:
    # Initialize the user's basic info
    def __init__(self, first_name: str, last_name: str, email: str, age: int, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    # Display the user infomation
    def display_info(self):
        if self.is_rewards_member:
            rewards_member = "He/She is a rewards member"
        else:
            rewards_member = "He/She is not a rewards member"
        
        info = f"Name: {self.first_name} {self.last_name} \nEmail: {self.email} \nAge: {self.age} \n{rewards_member} \nGold Card Points: {self.gold_card_points}"
        print(info)
        return self

    # Enroll the user
    def enroll(self):
        if self.is_rewards_member:
            print("{} {} is already a member".format(self.first_name, self.last_name))
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    # Spend the gold points in the user's card
    def spend_points(self, amount: int):
        if self.gold_card_points <= amount:
            print("You don't have enough gold points in your card")
        else:
            self.gold_card_points = self.gold_card_points - amount
            print("{} {} now has {} gold points in the card".format(self.first_name, self.last_name, self.gold_card_points))
        return self

# Create new users
user1 = User("Tony", "Stark", "tony.stark@gmail.com", 30)
user2 = User("Spider", "Man", "spider.man@gmail.com", 18)
user3 = User("Captain", "America", "captain.usa@gmail.com", 32)

#  Chaining Methods
user1.display_info().enroll().spend_points(50).display_info()

print("----------------------------------------------")
user2.enroll().spend_points(80).display_info()

print("----------------------------------------------")
user3.display_info().spend_points(40)