Python Abstract

This code is written to demonstrate how to write an abstract class in python.

Abstract class (as the word abstract might suggest) is supposed to be class that cannot be instantiated to an object. Now, what may be the use of such a class you might ask. Many a times we want to group a bunch of insances as inheriting from the same hierarchy, however, we have no interest in creating an instance of the said parent.

For example, let's say have a class for different languages: English, Hindi, Sanskrit, Spanish etc. Now we want to find some way to group these classes together since we know they are all languages. So we create a base abstract class 'Language' and we derive the above classes from this base class. This helps us in two ways:
a. Provide a common interface for various languages to derive from. For example, we can have variables 'script', 'origin', 'usage_population' and functions like 'get_region', 'translate_into', 'translate_from' declared in the base abstract class. These are declared as abstract methods. More explanation on abstract methods below.
b. Avoid code repitition by defining some functions in the base class. For example, define function 'percent_used'

percent_used()
{
	usage_population/total_world_population;
}

Note that we may never have to create an instance of the 'Language' class itself. This is where the term 'abstract' comes to play. Now, that we have a notional concept of what an abstract class is, we will see how to implement that in python.

Abstraction is an important Object Oriented programming concept and various languages have their own ways of implementing them. As mentioned above the primary reason behind creating abstract class is to be able to define abstract methods. An abstract method is a method defined in a base class which is expected to be overriden in the derived class. So the base class might just have a declaration or only partial implementation defined in the abstract method.

In Java, the keyword 'abstract' is used to define an abstract class.Java:
public asbtract class Language{

...

} 

In C++, there is no keyword abstract to explcitly define a class abstract. However, it is possible to acheieve abstraction using pure virtual function. The way to do this is there must be atleast one pure virtual function defined inside a class in C++. This ensures that one cannot create an instance of such a class. What is a virtual function and pure virtual function is another topic for another time (The internet is replete with these examples). For our purpose, let's just see what a pure virtual function looks like.

class Language
{
   ...
	virtual get_region() = 0;
}

That's right, a pure virtual function is declared by assiging the function definition to 0. The presence of atleast one such function inside a class renders it abstract in C++. Any class that derives from the above class is abstract too unless all the pure virtual functions in the base class are given proper definitions in the derived class.

It is important to see the nature and usage of abstract classes in these traditional Object Oriented Programming languages before we come to python. The pythonic concepts have tended more towards reliance on developer responsibility rather than rigid enforcement of rules. This can be seen with the absence of private and public concepts in Classes. However, the developer can always indicate methods and members as private by using the underscore before the name in the declaration.

In the same spirit, to use abstract class one must import the 'abc' library as there is no keyword or implied abstraction in python by default. 'abc' stands for abstract base class. In order for a class to be abstract it must be derived from the ABC module in the 'abc' library. The abstract method is declared using the '@abstractmethod' decorator in the 'abc' library. 

Code:
from abc import ABC, abstractmethod

class Language(ABC):
    ...

    @abstractmethod
    def get_region():
        ...
