class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.preferences = {}

class Item:
    def __init__(self, id, name, features):
        self.id = id
        self.name = name
        self.features = features

class ContentBasedFilter:
    def __init__(self):
        self.users = []
        self.items = []

    def add_user(self, user):
        self.users.append(user)

    def add_item(self, item):
        self.items.append(item)

    def calculate_similarity(self, user, item):
        similarity = 0
        for feature in user.preferences:
            if feature in item.features:
                similarity += user.preferences[feature] * item.features[feature]
        return similarity

    def recommend(self, user_id):
        user = next((u for u in self.users if u.id == user_id), None)
        if user is None:
            return []

        recommended_items = []
        for item in self.items:
            similarity = self.calculate_similarity(user, item)
            if similarity > 0:
                recommended_items.append((item, similarity))

        recommended_items.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in recommended_items]

# Misol
filter = ContentBasedFilter()

user1 = User(1, "John")
user1.preferences = {"genre": 1, "year": 2000, "director": 1}

user2 = User(2, "Alice")
user2.preferences = {"genre": 1, "year": 2010, "director": 0}

item1 = Item(1, "Movie1", {"genre": 1, "year": 2000, "director": 1})
item2 = Item(2, "Movie2", {"genre": 1, "year": 2010, "director": 0})
item3 = Item(3, "Movie3", {"genre": 0, "year": 2000, "director": 1})

filter.add_user(user1)
filter.add_user(user2)
filter.add_item(item1)
filter.add_item(item2)
filter.add_item(item3)

print(filter.recommend(1))  # [Movie1, Movie3]
print(filter.recommend(2))  # [Movie2]
