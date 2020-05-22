class PropertiesManagerSingleton:
    _instance = None
    
    def __new__(self):
        if self._instance is None:
            self._instance = object.__new__(self)
        self._prop = {}
        return self._instance
    
    @property
    def prop(self):
        return self._prop

if __name__ == "__main__":

    s1 = PropertiesManagerSingleton()
    s2 = PropertiesManagerSingleton()
    s1.prop["user"] = "user-test"

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    print(f'value key user is: {s2.prop["user"]}')