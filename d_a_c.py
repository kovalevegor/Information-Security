# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:35:50 2024

@author: gogak
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:37:46 2024

@author: gogak
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, password):
        return self.password == password

class Object:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def read(self):
        return self.data

    def write(self, new_data):
        self.data = new_data

    def append(self, additional_data):
        self.data += additional_data

    def delete(self):
        self.data = ""

class AccessControl:
    def __init__(self):
        self.users = {}
        self.objects = {}
        self.permissions = {}

    def add_user(self, user):
        self.users[user.username] = user

    def add_object(self, object):
        self.objects[object.name] = object

    def set_permission(self, user, object, action):
        self.permissions[user.username, object.name, action] = True
        
    def set_restriction(self, user, object, action):
        self.permissions[user.username, object.name, action] = False

    def has_permission(self, user, object, action):
        # return self.permissions.get((user.username, object.name), "") == permission
        return self.permissions.get(user.username, object.name, action)
    def print_permissions(self):
         if not self.permissions:
            print("Нет установленных разрешений.")
            return

         print("Список разрешений:")
         for (username, object_name, action), has_permission in self.permissions.items():
            permission = "Разрешено" if has_permission else "Запрещено"
            print(f"- Пользователь: {username}, объект: {object_name}, действие: {action}, разрешение: {permission}")

def main():
    # Инициализация системы
    access_control = AccessControl()
    
    # Добавление пользователей
    God = User("God", "god")
    Angel = User("Angel", "angel")
    King = User("King", "king"  )
    Prophet = User("Prophet", "prophet")
    Peasant = User("Peasant", "peasant")
    Pawn = User("Pawn", "pawn")
    
    access_control.add_user(God)
    access_control.add_user(Angel)
    access_control.add_user(King)
    access_control.add_user(Prophet)
    access_control.add_user(Peasant)
    access_control.add_user(Pawn)

 # Добавление объектов
    object1 = Object("Будущее", "Это слишком секретная информация")
    object2 = Object("Смысл жизни", "Не есть сладкого и ложиться спать до двеннадцати")
    object3 = Object("Жития святых", "Во дни княжения Владимира Святославича, просветившего Русь светом Христовой веры, жили два сына его, Борис и Глеб. Благочестивые и кроткие, они являлись образцом христианского жития.После кончины отца старший брат Святополк, одержимый жаждой власти, убил своих братьев, Бориса и Глеба. Невинные мученики, не противившиеся злу, приняли смерть с кротостью и смирением. Их души воспарили к престолу Господа, где они обрели нетленный венец славы. С тех пор Борис и Глеб стали небесными покровителями Русской земли, заступниками и помощниками всех верующих. Их мощи, источающие чудеса, являют собой источник духовной силы и утешения. Память святых князей Бориса и Глеба вечно жива в сердцах людей, чтущих их за веру, любовь к ближним и самоотверженность.")
    object4 = Object("Исторические хроники", "И пошёл Олег на Царьград, оставив Игоря в Киеве. Придя к Царьграду, он вытащил свои корабли на сушу и повелел воинам сделать колеса. И поставили корабли на колеса, и поднялся ветер, и поплыли корабли по полю. Греки же, увидев это, испугались и сказали: \"Это не люди, а святые идут на нас!\". И послали к Олегу, прося мира и давая дань. Олег же, немного постояв у Царьграда, заключил мир с греками и взял с них дань, и вернулся в Киев.")
    object5 = Object("Светская литература", "Кого интересует эта скукотища?")
    object6 = Object("Проповеди", "Слушайте, люди, и внимайте моим словам, ибо я несу вам весть о сверхчеловеке! Бог мертв! Мы сами должны стать творцами своих ценностей, обрести волю к власти и провозгласить новую эру. Сверхчеловек – это тот, кто стоит над добром и злом, кто создает свои собственные законы. Станьте сверхчеловеками, братья и сестры! Преодолейте себя, обретите свободу и силу! Вечное возвращение – вот истина бытия. Все события будут повторяться бесконечное число раз, поэтому каждый момент жизни драгоценен. Не цепляйтесь за старое, переоцените ценности! Amor fati – любите свою судьбу, даже если она трагична. В каждом из вас живет дионисийское и аполлоническое начала: стремление к хаосу и экстазу, а также к порядку и гармонии. Творчество – это основа жизни. Превратите свою жизнь в произведение искусства, живите без оглядки на прошлое. Будьте верны земле, не ищите утешения в потустороннем мире. Мир станет лучше, если каждый из нас станет творцом своего счастья. Такова проповедь Заратустры. Прислушайтесь к ней, и она озарит ваш путь!")
    object7 = Object("Сказки и легенды", "В те давние времена жил герой по имени Беовульф. Из геатских земель пришел он в Данию, где чудовище Грендель сеяло страх. Сразился Беовульф с монстром, одолел его и спас короля Хродгара. Но не ведал он покоя. Мать Гренделя явилась, мстя за сына. Отправился Беовульф в ее логово, тьмой окутанное, и там с ней сразился. Одолел и ее, вернув мир в королевство. Вернулся Беовульф на родину, королем стал. Но не везло ему - дракон свирепый напал на его земли. Сразился Беовульф с драконом, но рану смертельную получил. Скончался герой, но слава о нем жива. Помните, воины, о Беовульфе, о его доблести и чести!")
    access_control.add_object(object1)
    access_control.add_object(object2)
    access_control.add_object(object3)
    access_control.add_object(object4)
    access_control.add_object(object5)
    access_control.add_object(object6)
    access_control.add_object(object7)

    # Настройка прав доступа
    access_control.set_permission(God, object1, "read")
    access_control.set_permission(God, object1, "write")
    access_control.set_permission(God, object1, "delete")
    access_control.set_permission(God, object1, "append")
    
    access_control.set_permission(Prophet, object3, "read")
    access_control.set_restriction(Prophet, object3, "write")
    access_control.set_restriction(Prophet, object3, "delete")
    access_control.set_restriction(Prophet, object3, "append")
    # Вход в систему
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    user = access_control.users.get(username)
    access_control.print_permissions()
    # Аутентификация
    if user and user.authenticate(password):
        print(f"Добро пожаловать, {username}!")

        # Работа с объектами
        while True:
            object_name = input("Введите имя объекта: ")
            object = access_control.objects.get(object_name)

            if object:
                action = input("Введите действие для объекта (read, write, delete, append): ")
                permission = access_control.has_permission(username, object_name, action)
                # if action == 'show':
                #     access_control.print_permissions()
                if permission:
                    if action == "read":
                        print(f"Данные объекта {object_name}: {object.read()}")
                    if action == "write":
                        new_data = input("Введите новые данные: ")
                        object.write(new_data)
                        print(f"Данные объекта {object_name} обновлены.")
                elif permission == "write":
                    new_data = input("Введите новые данные: ")
                    object.write(new_data)
                    print(f"Данные объекта {object_name} обновлены.")
                elif permission == "append":
                    new_data = input("Введите данные для добавления: ")
                    object.append(new_data)
                    print(f"Данные добавлены к объекту {object_name}.")
                else:
                    print(f"У вас нет доступа к объекту {object_name}.")
            else:
                print(f"Объект {object_name} не найден.")

            choice = input("Продолжить? (y/n): ")
            if choice.lower() == "n":
                break
    else:
        print("Неверный логин или пароль.")

if __name__ == "__main__":
    main()
