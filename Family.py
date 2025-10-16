# Classes: Father, Mother, Child, Family
from pprint import pprint as pretty
class Father:
    """
   Class: Father
    Attributes:
        - father_name (str): The name of the father.
        - father_age (int or float): The age of the father.

    Methods:
        - set_father_name(name): Sets the father's name.
        - set_father_age(age): Sets the father's age.
        - get_father_name(): Returns the father's name.
        - get_father_age(): Returns the father's age.
    """

    def __init__(self):
        self.father_name = ""
        self.father_age = None

    def set_father_name(self, name):
        self.father_name=name

    def set_father_age(self, age):
        self.father_age=age

    def get_father_name(self):
        return self.father_name

    def get_father_age(self):
        return self.father_age


class Mother:
    """
        Class: Mother
    Attributes:
        - mother_name (str): The name of the mother.
        - mother_age (int or float): The age of the mother.

    Methods:
        - set_mother_name(name): Sets the mother's name.
        - set_mother_age(age): Sets the mother's age.
        - get_mother_name(): Returns the mother's name.
        - get_mother_age(): Returns the mother's age.
    """
    def __init__(self):
        self.mother_name = ""
        self.mother_age = None

    def set_mother_name(self, name):
        self.mother_name = name

    def set_mother_age(self, age):
        self.mother_age = age

    def get_mother_name(self):
        return self.mother_name

    def get_mother_age(self):
        return self.mother_age


class Child(Father, Mother):
    """
     Class: Child (inherits from Father and Mother)
    Attributes:
        - child_name (str): The child's name.
        - child_age (int or float): The child's age.

    Methods:
        - set_child_name(name): Sets the child's name.
        - set_child_age(age): Sets the child's age.
        - get_child_name(): Returns the child's name.
        - get_child_age(): Returns the child's age.
        - set_father(name, age): Sets the father's name and age.
        - set_mother(name, age): Sets the mother's name and age.
        - set_parents(father_details, mother_details):
          Accepts two dictionaries (for father and mother),
          each with keys "name" and "age", and sets their values.
    """
    def __init__(self):
        super(Child, self).__init__()
        self.child_name=""
        self.child_age=None

    def set_child_name(self, name):
        self.child_name=name

    def set_child_age(self, age):
        self.child_age = age

    def get_child_name(self):
        return self.child_name

    def get_child_age(self):
        return self.child_age

    def set_father(self, father_name, father_age):
        self.set_father_name(father_name)
        self.set_father_age(father_age)

    def set_mother(self, mother_name, mother_age):
        self.set_mother_name(mother_name)
        self.set_mother_age(mother_age)

    def set_parents(self, father_details, mother_details):
        try:
            if "name" not in father_details or "age" not in father_details or "name" not in mother_details or "age" not in mother_details:
                raise ValueError
            self.set_father(father_details["name"],father_details["age"])
            self.set_mother(mother_details["name"],mother_details["age"])
        except ValueError:
            return "Keys \"name\" & \"age\" must be included in father & mother details"
        except Exception as e:
            return f"Error {e}"

#Family class:
class Family(Child):
    """
    Class: Family (inherits from Child)
    Attributes:
        - parents (dict): Contains two dictionaries for 'father' and 'mother'.
        - children (dict): Dictionary mapping child names to ages.
        - last_name (str): The family's last name.

    Methods:
        - add_child(name, age): Adds a child to the children dictionary.
          Validates that age is between 0 and 120.
        - get_children(): Returns a list of all children's names.
        - get_child(i): Returns the i-th child's name (1-based index).
        - get_parents_name(): Returns a formatted string with parents' names
    """
    def __init__(self, parents, children, last_name=''):
        super(Family, self).__init__()
        self.parents = parents
        self.children = children
        self.last_name = last_name
        self.set_parents(parents["father"],parents["mother"])

    def add_child(self, child_name, child_age):
        try:
            if type(child_name) != str or not isinstance(child_age,(int,float)):
                raise TypeError
            if child_age > 120 or child_age < 0:
                raise ValueError
            self.children[child_name]=child_age
        except TypeError:
            return "Check the name or age"
        except ValueError:
            return "Age is not in range 0-120"
        except Exception as e:
            return f"Error: {e}"

    def get_children(self):
        try:
            return list(self.children.keys())
        except Exception as e:
            return f"Error {e}"

    def get_child(self, i):
        try:
            children_list=self.get_children()
            if len(children_list) >= i:
                return children_list[i - 1]
            else:
                raise IndexError
        except IndexError:
            return "Child index out of range"
        except Exception as e:
            return f"Error {e}"

    def get_parents_name(self):
        try:
            return f"Father name: {self.father_name}, Mother name: {self.mother_name}"
        except Exception as e:
            return f"Error {e}"

# Main function to interact with the user and create a family object
def main():
    father_name = input("Enter father name ")
    father_age = input("Enter father age ")
    father_age = float(father_age)
    mother_name = input("Enter mother name ")
    mother_age = input("Enter mother age ")
    mother_age = float(mother_age)
    num_of_children = input("Enter number of children ")
    num_of_children = int(num_of_children)
    children = {}
    for i in range(num_of_children):
        child_name = input("Child name: ")
        child_age = input("Child age: ")
        child_age = float(child_age)
        children[child_name] = child_age
    last_name = input("Enter last name ")

    father_details = {"name":father_name, "age":father_age}
    mother_details = {"name":mother_name, "age":mother_age}
    parents = {"father":father_details, "mother": mother_details}

    # Create Family object and display details
    f = Family(parents,children,last_name)
    print(f"Family: {f.last_name}")
    print(f"Father: {f.father_name}, Age: {f.father_age}")
    print(f"Mother: {f.mother_name}, Age: {f.mother_age}")
    print("Children:")
    for name, age in f.children.items():
        print(f" - {name}: {age}")


if __name__ == "__main__":
    main()


# numpy.arange()

       # self.parents= {"Father name" : self.father_name,"Father Age": self.father_age, "Mother name":self.mother_name,"Mother Age": self.mother_age}






