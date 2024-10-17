from time import sleep

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class UrTube():
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
       for user in self.users:
            if user.get('nickname') == nickname:
                if user.get('password') == hash(password):
                    self.current_user = nickname
                else:
                    print('Введен несуществующий логин или неверный пароль', 3)

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        bool_ = True
        if len(self.users) != 0:
            for user_ in self.users:
                if user.nickname == user_.get('nickname'):
                    bool_ = False
                    print(f'Пользователь {user.nickname} уже существует')
                    break
        if bool_:
            self.users.append({
                'nickname': user.nickname,
                'password': user.password,
                'age': user.age,
            })
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for item in args:
            bool_ = True
            for video in self.videos:
                if item.title.lower() == video.get('title').lower():
                    bool_ = False
                    break
            if bool_:
                self.videos.append({
                    'title': item.title,
                    'duration': item.duration,
                    'time_now': item.time_now,
                    'adult_mode': item.adult_mode
                })
            else:
                continue

    def get_videos(self, str_):
        list_ = []
        if len(self.videos) > 0:
            for video in self.videos:
                if video.get('title').lower().find(str_.lower()) != -1:
                    list_.append(video)
                else:
                    continue
        return list_

    def watch_video(self, str_):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            if len(self.videos) > 0:
                dict_ = {}
                for video in self.videos:
                    if video['title'] == str_:
                        dict_ = video
                        break
                if len(dict_):
                    user_ = {}
                    if dict_.get('adult_mode'):
                        for user in self.users:
                            if user.get('nickname') == self.current_user:
                                user_ = user
                                break
                        if user_.get('age') < 18:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        else:
                            while dict_['time_now'] in range(0, dict_['duration'] + 1):
                                sleep(1)
                                print(dict_['time_now'])
                                dict_['time_now'] += 1
                            print('Конец видео')
                            dict_['time_now'] = 0
                    else:
                        while dict_['time_now'] in range(0, dict_['duration'] + 1):
                            sleep(1)
                            print(dict_['time_now'])
                            dict_['time_now'] += 1
                        print('Конец видео')
                        dict_['time_now'] = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
