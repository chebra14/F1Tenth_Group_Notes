### Object Orientated Programming (OOP)

- realpython.com/python3-object-orientated-programming/

#### What is OOP in Python?

- Provides a means of structuring programs so that properties and behaviours are bundled into individual objects
	- Object = Person
	- Property = name, age, and address
	- Behaviours = walking, talking, breathing, and running
#### How do you define a class in python?

`class Employee:`
	`def __init__(self, name, age)`
		`self.name = name`
		`self.age = age`

- Why not use a list to store info about the object?
	- Large files become difficult to manage
	- Errors occur of there are missing elements


##### Classes vs instances

- Classes
	- Create user-defined data structures
	- Defined functions are called methods
	- A blueprint for how to define something
- Instance
	- This is the object built from the class
- 


##### Class Definition

- Define the properties that the objects have using `__init__()`
	- Sets the initial state of the object by assigning the values of the object's properties
	- The first parameter must always be `self`
	- The attributes created are called instance attributes
- Class attributes have the same value for all class instances

`class Employee:`
	`species = "Canis familiaris"`
	
	def __init__(self, name, age)
		self.name = name
		self.age = age


#### How do you instantiate a class in python?

- Use open-close parenthesis:
`Dog()`
- Just instantiating it will just assign it its address value

##### Class and instance attributes

- If there are instance attributes required, you need to provide the parameters, otherwise there will be an error:

`miles = Dog("Miles", 4)`

- Attributes are accessed using dot notation:

`miles.name`
`>> Miles`

`miles.age`
`>> 4`

- Class attributes can be changed as well

- Access class attributes the same way:

`miles.species`
`>> Canis familiaris`


##### Instance methods

- These are functions that can be defined inside a class
- The first instance is always `self`

`def description(self):`
	`return f"{self.name} is {self.age} years old"`

`def speak(self, sound):`
	`return f"{self.name} says {sound}"`

- _*The f just formats as string

- This description isn't good practice
	- You can use `__str__` to make the description printable
	- Instead:
`def __str__(self):`
	`return f"{self.name} is {self.age} years olf"`

- Now you can just `print(miles)` 




_* These double underscore methods (dunder or magic methods) calls them in response to a specific function.



#### How do you inherit from another class in python?

- Inheritance is the process where one class takes on the attributes and methods of another. Formed classes become *child classes* derived from *parent classes*.
- You inherit but adding the name of the parent class in brackets after the child's declaration.

`class Parent:`
	`hair_colour = "brown"`

`class Child(Parent):`
	`pass`

- The child can override or extend the attributes of the parent 

##### Parent classes vs child classes

_* To see if an instance is a part of a specific object you can use `isinstance(instance, Obj)`



##### Parent class functionality extension

- To override a method defined in the parent, just assign a method with the same name.
- This won't affect the other children though
- Access the parent class using `super()`

`class JackRussellTerrier(Dog):`
	`def speak(self, sound= "Arf")`
		`return super().speak(sound)`