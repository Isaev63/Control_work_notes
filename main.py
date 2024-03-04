from user_interface import UserInterface

if __name__ == '__main__':
    filename = input('\033[1;32mВведите имя файла: \033[0m')
    try:
        ui = UserInterface(filename)
        ui.run()
    except ValueError as ex:
        print(ex)
