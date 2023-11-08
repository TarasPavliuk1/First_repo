def main():
    user = {}

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except KeyError:
                return 'No user with this name'
            except ValueError:
                return 'Give me name and phone please'
            except IndexError:
                return 'Enter user name'
        return inner

    def hello_handler(command):
        if command in ["hello"]:
            return 'Hello, how can I help you?'

    @input_error
    def add(*args):
        name, phone = args
        user[name] = phone
        return f'User "{name}" added with phone number {phone}'

    @input_error
    def change(*args):
        name, phone = args
        user[name] = phone
        return f'Phone number for user "{name}" updated to {phone}'

    @input_error
    def phone(*args):
        name = args[0]
        return user.get(name, 'User not found')

    def show_all():
        if user:
            for name, phone in user.items():
                print(f"Ім'я: {name}, Номер телефону: {phone}")
        else:
            return 'No users in the list'

    def exit_handler(command):
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            exit()

    while True:
        command = input("Enter your command: ").lower()

        if command in ["hello"]:
            response = hello_handler(command)
            print(response)
        elif command.startswith("add "):
            name_phone = command[4:].split(',')
            response = add(*name_phone)
            print(response)
        elif command.startswith("change "):
            name_phone = command[7:].split(',')
            response = change(*name_phone)
            print(response)
        elif command.startswith("phone "):
            name = command[6:]
            response = phone(name)
            print(response)
        elif command in ["show all"]:
            response = show_all()
            if response:
                print(response)
        elif command in ["good bye", "close", "exit"]:
            exit_handler(command)
        else:
            print("Command not recognized. Please try again.")

if __name__ == "__main__":
    main()
