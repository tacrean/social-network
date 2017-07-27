class User:
    def __init__(self, userName, userId):
        self.userName = userName
        self.friendList = []
        self.page = Page(self.userName, self)


class Page:
    def __init__(self, userName, User):
        self.interface = ''
        self.postList = {}
        self.userName = userName

    def viewInterface(self):
        print(self.userName + "'s Page")
        User.friendList.append(User('test'))
        print(User.friendList.userName)

        for key in self.postList:
            print(key)
        Actions = input('Actions: Make a new post (a) Add new firends (b)')
        if Actions == 'a':
            title = input('What is the title of your new post? ')
            body = input('What do you want your post to say? ')
            User.postList[title]=body
        if Actions == 'b':
            newFriend = input('who would you like to add?')#check agains users
            #checking key
            key = userName
            v = newFriend
            for key in Network.connections:
                if v == value:
                    print('You are already friends')
                    self.interface()
            key = Network.users.index(newFriend)
            v = Network.users.index(userName)
            for key in Network.connections:
                if v == value:
                    print('You are already friends')
                    self.interface()
            #adding friend
            #userName
            #newFriend
            #add the friend connection to the dictionary
            User.friendList.append(User(newFriend))
            newFriend.friendList.append(User(userName))




class Network:
    def __init__(self):
        self.users = []
        self.connections = {}
        self.users.append(User('taima', len(self.users)))
    def addNewUser(self):
        userName = input('What do you want your username to be?')
        for users in self.users:
            if users.userName == userName:
                access = input('That name is already taken, if this is your account type login to access it. ')
                return access ##add function of logging in versus adding a new user then link it here
        print('Welcome to the network!')
        self.users.append(User(userName, len(self.users)))
        for i in self.users:
            print(i.userName)
        return
            #add link to the persons profile here

    def logInUser(self):
        userName = input('What is your username? ')

        for users in self.users:
            if users.userName == userName:
                print("hey girl")#link to the user profile here
                self.users[userId].page.viewInterface()
                return
        access = input('You are not in the system, do you want to create a new account? ')
        return access

    def friend(self):
        newFriend = input('Who do you want to add as a friend?')
        for user in self.friendList:
            if user == newFriend:
                print('You are already friends!')
        #for user in self.users:

def main():


    print('Welcome to The Network!')
    myNetwork= Network()
    running = 1
    while(running):
        access = input('Do you want to login or create a new account? ')
        if access == 'login':
            access = myNetwork.logInUser()
        if access == 'create a new account' or access == 'new account' or access == 'new':
            access = myNetwork.addNewUser()
         #if access != 'create a new account' or access != 'new account' or access != 'new' or access != 'login':
        #     print(access)
        #     print('Thank you for using The Network, goodbye.')
        #     exit()
        if access == 'quit':
            print('Thank you for using The Network, goodbye.')
            exit()
        if access == 'page':
            print(myNetwork.users[0].page.viewInterface())

main()
