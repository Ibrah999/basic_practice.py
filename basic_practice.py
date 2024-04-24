def sound(animal):
    return "moew"

print(sound("cat"))

def attribute(animal):
    return "I'm a " + animal + "! My sound is '" + sound(animal) + "'."

print(attribute("cat"))