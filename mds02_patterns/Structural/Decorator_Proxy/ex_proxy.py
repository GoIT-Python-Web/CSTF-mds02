class Resource:

    def __init__(self, content):
        self.content = content

    def view(self):
        print('Viewing resource')
        return self.content

    def download(self):
        print('Downloading resource')
        return self.content


class Proxy:
    def __init__(self, resource: Resource, user_role: str):
        self.resource = resource
        self.user_role = user_role

    def view(self):
        if self.user_role in ['admin', 'moderator', 'user']:
            return self.resource.view()
        else:
            print('Access denied')

    def download(self):
        if self.user_role in ['admin', 'moderator']:
            return self.resource.download()
        else:
            print('Access denied')


if __name__ == "__main__":
    resource = Resource('some content')
    proxy = Proxy(resource, 'admin')
    print(proxy.view())
    print(proxy.download())

    proxy_user = Proxy(resource, 'user')
    print(proxy_user.view())
    print(proxy_user.download())
