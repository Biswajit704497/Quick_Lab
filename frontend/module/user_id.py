import uuid
def generate_user_id():
    return str(uuid.uuid4())

if __name__ == '__main__':
    id = generate_user_id()
    print(id)