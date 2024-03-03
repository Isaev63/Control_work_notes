from notes import Notes


class UserInterface:
    """
    Class for handling user interface interactions.
    """

    def __init__(self, filename):
        """
        Initializes the UserInterface object.
        Parameters:
            filename (str): The name of the file to store notes (without extension).
        """
        self.notes = Notes(filename)

    def run(self):
        """
        Runs the main loop of the user interface.
        The loop displays a menu of options to the user and executes the chosen action.
        """
        while True:
            print('\n\033[1;32m[1] Создать заметку\n'
                  '[2] Редактировать заметку\n'
                  '[3] Показать заметку по ID\n'
                  '[4] Показать список всех заметок\n'
                  '[5] Удалить заметку\n'
                  '[6] Выход\033[0m\n')

            option = input('\033[32m[*] -- Выберете нужное действие: \033[0m')

            try:
                if option == '1':
                    self.notes.create_note()
                elif option == '2':
                    id_note = int(input('\033[32m[*] -- Введите ID записи: \033[0m'))
                    self.notes.edit_note(id_note)
                elif option == '3':
                    id_note = int(input('\033[32m[*] -- Введите ID записи: \033[0m'))
                    self.notes.read_note(id_note)
                elif option == '4':
                    self.notes.read_all_notes()
                elif option == '5':
                    id_note = int(input('\033[32m[*] -- Введите ID записи: \033[0m'))
                    self.notes.delete_note(id_note)
                elif option == '6':
                    break
                else:
                    print('\033[1;31m[*] -- Неверная опция! '
                          'Выберете числа из предложенного списка [1, 2, 3, 4, 5].\033[0m')
            except ValueError as ex:
                print(f'\033[1;31m{ex}\033[0m')
