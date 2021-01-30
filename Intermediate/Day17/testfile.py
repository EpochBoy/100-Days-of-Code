class User:

    # Python Constructor
    # init is called every time we create a new object
    # Convention is naming param same as attribute
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # You can also assign values using variables as below without passing params
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# PascalCaseIsCapitalizingAllWords
# camelCaseIsLowerCasingFirstWord
# snake_case_is_all_words_lower_cased_and_seperated_by_an_underscore

# Python Class' name should be pascal-case

user_1 = User("001", "FredTheNinja")
user_2 = User("002", "Memer")
print(user_1.id, user_1.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
