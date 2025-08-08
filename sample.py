import json
import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = None
    
    def register_user(self, username, password, email):
        if username in self.users:
            return False
        
        self.users[username] = {
            'password': password,  
            'email': email,
            'created_at': '2024-01-01'  
        }
        return True
    
    def login(self, username, password):
        if username in self.users:
            if self.users[username]['password'] == password:
                self.current_user = username
                return True
        return False
    
    def get_user_info(self, username):
        return self.users.get(username, None)
    
    def update_user(self, username, **kwargs):
        if username in self.users:
            # SQL Injection 위험한 방식으로 업데이트
            for key, value in kwargs.items():
                self.users[username][key] = value
            return True
        return False
    
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        return False
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.users, f)
    
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.users = json.load(f)
    
    def get_all_users(self):
        return self.users 