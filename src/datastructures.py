
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 4
        # example list of members
        self._members = [
            {"first_name": "Jhon",
             "last_name": "Jackson",
             "age": 33,
             "id": 1,
             "lucky_numbers": [7,13,22]},
             {"first_name": "Jane ",
             "last_name": "Jackson",
             "age": 35,
             "id": 2,
             "lucky_numbers": [10, 14, 3]},
             {"first_name": "Jimmy  ",
             "last_name": "Jackson",
             "age": 5,
             "id": 3,
             "lucky_numbers": [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        print(member)
        # fill this method and update the return
        
        if int(member["age"]) <= 0:
            print("Edad inválidad")
            return False
        
        if not "id" in member:
            member["id"] = self._generateId()
    
        member["last_name"] = self.last_name
        self._members.append(member)
        return True

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return False
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
