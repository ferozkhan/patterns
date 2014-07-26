

class Publisher:

    def __init__(self):
        pass

    def register_user(self):
        pass

    def unregister_user(self):
        pass

    def notify_all(self):
        pass


class Subscriber:

    def __init__(self):
        pass

    def notify(self):
        pass


class NewsChannel(Publisher):

    def __init__(self):
        self.__registered_users = []
        self.news = ''

    def register_user(self, user):
        if user and user not in self.__registered_users:
            self.__registered_users.append(user)

    def unregister_user(self, user):
        if user and user in self.__registered_users:
            self.__registered_users.remove(user)

    def notify_all(self):
        for user in self.__registered_users:
            user.notify(self.news)

    def publish_news(self, news):
        if news:
            self.news = news
            self.notify_all()


class User(Subscriber):

    def __init__(self):
        pass

    def notify(self, news):
        print 'user1: ' +  news


class User2(Subscriber):

    def __init__(self):
        pass

    def notify(self, news):
        print 'user2: ' + news


if __name__ == '__main__':
    user = User()
    user2 = User2()
    news_channel = NewsChannel()
    news_channel.register_user(user)
    news_channel.register_user(user2)
    news_channel.publish_news('News Headline!')
    news_channel.publish_news('Another News Headline!')
