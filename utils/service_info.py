from faker import Faker

class ServiceInfo:

    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        return "test_" + name




if __name__ == '__main__':
    title = ServiceInfo().get_name()
    print(title)