import re


class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def user_input(self):
        # firstname = input('enter firstname:')
        # lastname = input('enter lastname:')
        # age = int(input('enter age:'))
        user_data = {}
        user_data.update({'firstname': self.firstname, 'lastname': self.lastname, 'age': self.age})
        # user_data['firstname'] = firstname
        return user_data

    def input_validation(self, user_dic):
        try:
            input = r'[a-zA-Z]{5,10}'
            fname = re.search(input, user_dic['firstname'])
            lname = re.search(input, user_dic['lastname'])
            reg_num = r'[0-9]'
            age = re.search(reg_num, str(user_dic['age']))

            print(input)
            if fname and lname and age:
                print("ok")
            else:
                raise Exception("please pass alphabets. min length 5 and max length 10")
            return True
        except KeyError:
            return False
