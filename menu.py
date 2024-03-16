import sys
from diarybook import Diary, DiaryBook
from util import read_from_json_into_application, insert_into_json_file, save_users_to_json, read_from_users_file,read_from_data_json,read_from_user_json
from user import User
import os

class Menu:
    def __init__(self):
        self.diarybook = DiaryBook()
        self.users_file = 'users.json'
        self.current_user = None
        self.users = read_from_users_file(self.users_file)
        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            "5": self.quit
        }

    def display_login_menu(self):
        print("""
                    Welcome to DiaryBook  
                    1. Login
                    2. Register
                    """)

    def login_or_register(self):
        while True:
            self.display_login_menu()
            choice = input("Enter an option: ")
            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if self.authenticate_user(username, password):
                    print("Login successful!")
                    self.current_user = username
                    break
                else:
                    print("Invalid username or password. Please try again.")
            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.register_user(username, password)
                print("Registration successful! Please login.")
            else:
                print("Invalid choice. Please try again.")

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.login(password, username):
                return True
        return False

    def register_user(self, username, password):
        new_user = User.register(username, password)
        self.users.append(new_user)
        save_users_to_json(self.users, self.users_file)

    def display_menu(self):
        print(""" 
                     Notebook Menu  
                    1. Show diaries
                    2. Add diary
                    3. Search diaries
                    4. Populate database
                    5. Quit program
                    """)

    def run(self):
        self.login_or_register()
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    def show_diaries(self, username=None):
        if username:
            user_diaries = read_from_user_json(username)
            print("User Diaries:")
            for diary in user_diaries:
                print(f"{diary['memo']}")
        else:
            print("User Diaries:")
            for user in self.users:
                user_diaries = read_from_user_json(user.username)
                for diary in user_diaries:
                    print(f"{user.username}: {diary['memo']}")
        
        print("\nGeneral Diaries:")
        general_diaries = read_from_data_json()
        for diary in general_diaries:
            print(f"{diary['memo']}")
        
    print("\nGeneral Diaries:")
    general_diaries = read_from_data_json()
    for diary in general_diaries:
        print(f"{diary['memo']}")

    def add_diary(self):
        if self.current_user:
            memo = input("Enter a memo:         ")
            tags = input("add tags:             ")
            user = self.current_user
            diary_data = {
                "memo": memo,
                "tags": tags,
                "username": user
            }
            user_diary_file = f"{self.current_user}_data.json"
            if not os.path.exists(user_diary_file):
                with open(user_diary_file, 'w') as file:
                    file.write("[]")
            insert_into_json_file(diary_data, user_diary_file)
            print("Your note has been added")
        else:
            print("Please log in first to add a diary entry.")

    def search_diaries(self):
        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text)
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def quit(self):
        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        diaries1 = read_from_json_into_application(self.current_user)
        for diary in diaries1:
            self.diarybook.diaries.append(diary)

if __name__ == "__main__":
    Menu().run()