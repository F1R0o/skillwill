import json
from diarybook import Diary
from user import User
import os



def read_from_user_json(username):
    user_data_file = f"{username}_data.json"
    if os.path.exists(user_data_file):
        with open(user_data_file, 'r') as file:
            data = json.load(file)
        return data
    else:
        print(f"User data file '{user_data_file}' not found.")
        return []

def read_from_data_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def read_from_json_into_application(username):
    user_data = read_from_user_json(username)
    data = read_from_data_json()
    return user_data + data  




def insert_into_json_file(diary_data, path):
    with open(path, "r+") as file:
        data = json.load(file)
        data.append(diary_data)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    print("Data has been inserted into", path)




def save_users_to_json(users, path):
    with open(path, 'w') as file:
        json.dump([user.__dict__ for user in users], file, indent=4)
    print("Users have been saved to", path)



def read_from_users_file(path):
    try:
        with open(path, "r") as file:
            users_data = json.load(file)
            users = [User(user['username'], user['password']) for user in users_data]
            return users
    except FileNotFoundError:
        return []