class City:

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        # return False if self.name[-1] in 'aeiou' else True
        # return not self.name.endswith(("a", "e", "i", "o", "u"))

        return (self.name[-1] not in ['a','e','i','o','u'])


p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"

p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(bool(p2))  # печатает "True"

print(p2 == True)  # печатает "False"