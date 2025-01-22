from faker import Faker

fake = Faker()

# Function to generate a registered user
def get_registered_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }

if __name__ == "__main__":
    print(get_registered_user())
