// Last updated: Fri, February 05, 2021 - 17:52

OOP, Polymorphism Basic

###########################################################################
# CHECK IF PRIME NUMBER & IS PALINDROME
###########################################################################

public boolean isPrime(int n) {
    for (int i = 2; i < n/2; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

public static boolean isPalindrome(int n) {

    int num = n;
    int rev = 0;

    while (num > 0) {
        rev = (rev * 10) + (num % 10);
        num /= 10;
    }

    if (rev == n) return isPrime(rev);
    else return false;

}


###########################################################################
# FOP CHAP 6 : METHODS
###########################################################################
1. To end a void method, the return statement without any expression can be used "return;"

			public static void returnNothing(){
		        for(int i = 0; i < 10; i++){
		            if(i == 5) return;
		        }
		        System.out.println("This line wont be printed out unless the return; is changed to break;");
		    }

2. Object and array are known as reference type. Java *does not manipulate objects and arrays directly*. Instead, it *manipulates references to objects and arrays*.

3. Static method is the method that do not require an calling object. Math.pow(x, y); [SEE CHAP 8.8]

4. A variable of class type stores the reference of where the object is located in the memory.


###########################################################################
# FOP CHAP 8 : Class     # DS CHAP 1 : OOP
###########################################################################
1. Java is an Object-oriented programming language (OOP).

2. A copy constructor is a constructor with one parameter of the same type as the class. It creates an object that is separate, independent object with the instance variables are *exact copy of an argument object.*

3. public means that there are no restrictions on where the instance variable can be used.

4. private means that the instance variable is accessible only by methods of the same class.

5. protected means that the instance variable is accessible by methods of the same class, subclass or class in the same package.

6. A package is a namespace for organizing classes and interfaces in a logical manner. It makes large software projects easier to manage.   

7. The "this" parameter refer to the reference to the current object

8. A static variable is a variable that belongs to the class. There is only one copies of the static variable for all the objects. [SEE CHAP 8.9]

9. A static variable can be used by objects to communicate between the objects. [SEE CHAP 8.10]

10. A static method can access the static variables but can’t access the instance variables.

			public class Parent {
			    
			    private int age;
			    
			    public static int getAge(){
			        return age; // <-- ERROR: non-static variable age cannot be referenced from a static context
			    }
			    
			}

11. Encapsulation means that the data and actions are combined into a single item which is a Class.

12. Method overloading allows one class to have more than one definitions of a single method name. 

			public void setValue(String n) {
			   name = n;
			}
			public void setValue(String n, int a) {
			   name = n;
			   age = a;
			}
			public void setValue(String n, int a, char g) {
			   name = n;
			   age = a;
			   gender = g
			}


###########################################################################
# FOP CHAP 9 : INHERITANCE     # DS CHAP 1 : OOP
###########################################################################
1. Advantage of inheritance is code reuse.

2. Inheritance is the process by which a new class known as a derived class is created from another class called the base class.

3. The base class sometimes refer to superclass and the more specialized class that inherits from the superclass is called the subclass.

4. A subclass automatically has all the instance variables, static variables and the public methods of superclass.

5. Yet, a subclass has no access to the private fields of its superclass.

6. 	Base Class 		= Super Class 	= Parent Class 	= Ancestor Class
	Derived Class 	= Sub Class 	= Child Class 	= Descendent Class

7. super() invoke the no-argument constructor of superclass. Calling the constructor of base class.

8. super can also be used to call the method of a superclass. super() can only be called in the first line of derived constructor. While super.baseClassMethod() can be used anywhere in derived class.

			public class HourlyEmployee extends Employee {
			    public HourlyEmployee() {
			       super();
			       super.superClassMethod();
			    }
			}

9. A derived class inherits method that belong to base class. If the base class requires different definition for an inherit method, the method can be redefined or override.

10. Yet, the method can not be overridden if the base class method consists of final modifier.

11. IMPORTANT RULE: an override method cannot change the return type of the method definition BUT if the returned type is a class type, the returned type can be changed to the descendant class type.

			public class BaseClass {
			   ...
			   public Employee getValue() {

			   }
			}

			public class DerivedClass extends BaseClass {
			   ...
			   public HourlyEmployee getValue() {

			   }
			}

12. Override method can change private method to public method in derived class but cannot change public method to private method.

			public class BaseClass {
			   ...
			   private void setValue(int a) {

			   }
			}

			public class DerivedClass extends BaseClass {
			   ...
			   public void setValue(int a) {

			   }
			}

13. A derived class can’t access directly to the private instance variables of the base class. 

14. A derived class can access all the public methods and protected variables or methods from the base class. 

15. "protected" modifier can be used to allow the access for its own class and the derived class. However, the object of own class can’t access directly the protected variables.

			public class A {
			   protected int num;
			}

			public class B extends A {
			}

			A obj = new A()
			obj.num = 10; //Error <-- Tried no error ah then what o?

			B obj1 = new B()
			obj1.num = 10; //num is inherited from A

16. Every class inherit the getClass method from the class Object. The getClass method can be used to check the class of an object. The getClass method can’t be overridden.

			if (obj1.getClass() == obj2.getClass()) {
			   System.out.println("The objects are belongs to same class");
			}

17. The *instanceof* operator checks whether an object is belongs to a class or any descendent class.

			if (obj1 instanceof ClassName) {
			   System.out.println("The object is one of the type of any descendent class of ClassName"); 
			}


###########################################################################
# FOP CHAP 10 : POLYMORPHISM     # DS CHAP 1 : OOP
###########################################################################
1. A super class that can take in different type of subclasses

			Dog extends Animal
			Cat extends Animal
			Cow extends Animal

			Animal[] animal = new Animal[1000];
			Animal Tom = new Cat();
			animal[0] = new Dog();
			animal[1] = new Cat();
			animal[2] = new Cow();

			// Different animal different sound and acts
			for(Animal a : animal){
				a.speak();
				a.eat();
				a.acts();
			}

2. Assigning an object of a derived class to a variable of base class is often called upcasting. 

			BaseClass a = new BaseClass;
			DerivedClass b = new DerivedClass;
			a = b; 

3. Downcasting assigning an object of a base class to a derived class. To test whether the downcasting is legitimate.

			DerivedClass obj = new DerivedClass();
			if (obj1 instanceof DerivedClass) {
			   obj = (DerivedClass) obj1
			}

4. Every object inherits a method named clone from the class Object.

5. The clone method return a copy of the calling object.
- .clone() is you copy every parameter and construct a new object where the *address is not equal*
- And an obvious difference between shallow and deep copy is that when you change value of shallow copy, it will change the original also but for deep copy, it won't

			public ClassName clone() {
			   return new ClassName(this);
			}

			// BELOW DOESNT WORK
			public Sale doCopy(Sale a) {
			   Sale b;
			   b = a.clone();
			   return b;
			}

			// THIS WORKS
		    public Parent doCopy(Parent a) throws CloneNotSupportedException{
		        Parent b = (Parent) a.clone();
		        return b;
		    }

6. An abstract class is a class that has some methods without complete definitions. 

			public abstract class className{

			}

7. A class with no abstract methods is called a concrete class.

8. Object can’t be created using abstract class constructor.

10. An abstract method serves as a placeholder for a method that will be fully defined in a descendent class. It has no method body. 

11. An abstract method can’t be private.

12. A Java interface specifies a set of methods that any class that implements the interface must have.

			public interface interfaceName{

			}

13. An interface has no instance variable and no method definitions. 
	An interface provides full abstraction. 
	An interface can have only public static final variable.
	An interface cannot implement another interface but can extends multiple interface.***
	The "abstract" keyword is not required when define the abstract methods in interface because all methods are by default abstract.

14. An interface can contain defined constants as well as method headings. When a method implements the interface, it automatically gets the defined constant.

			public interface interfaceName {
			   public static final int MAX = 100;
			   public returnType methodName(parameterType parameterName, ...);
			}

15. A class can implement any number of interfaces.

			public class classA implements interfaceName, interfaceName2{

			}

16. classA must implement all the method headings listed in the definitions of the interfaces. It must make all the methods in the interface public.

17. A derived class can have only one base class. However, a class can implement any number of interfaces.

18. Comparable interface has one method

			public int compareTo(Object other);

			/*
			The method return negative if calling object comes before the parameter object
			The method return positive if calling object comes after the parameter object
			The method return zero if calling object equals to the parameter object
			*/

19. Inner class are classes defined within other classes. Inner and outer classes have access to each other’s private members.

			public class ClassName {

			   private class ClassName {

			   }

			}

20. A static Inner class can have nonstatic instance variables and methods but an object of static inner class has no connection to an object of the outer class.

			public class ClassName {

			   private static class ClassName {

			   }

			}


###########################################################################
# FOP CHAP 11 : EXCEPTION HANDLING     DS CHAP 3 : EXCEPTION HANDLING 
###########################################################################
1. An exception represents an error condition that can occur during the normal course of program execution.

2. By using exception handling, the exception is caught and processed.

			try {
			   throw new Exception("Exception Description");
			} catch (Exception e) {
			   System.out.println(e.getMessage());
			} 

3. Multiple catch blocks

			try {
			   // try block
			} catch (ExceptionOne e) {
			   // catch block
			} catch (ExceptionTwo e) {
			   // catch block
			}

4. Nested catch blocks

			try {
			   // try block
			   
			   try {
			      // try block
			   } catch (ExceptionOne e) {
			      // catch block
			   } 

			} catch (ExceptionOne e) {
			   // catch block
			} 

5. Predefined Exceptions

			IOException
			NoSuchMethodException
			FileNotFoundException
			NumberFormatException
			DivisionByZeroException
			ArrayIndexOutOfBoundsException
			InputMismatchException
			ArithmeticException
			EOFException

6. The new exception class can be defined. An exception class can be a derived class of any exception class.

			public class exceptionClassName extends Exception {
			   public exceptionClassName() {
			      super("Error Message");
			   }
			   public exceptionClassName(String s) {
			      super(S);
			   }
			}

7. An exception can be thrown in a method without catching it in the same method. The method will stop if the exception is thrown.

			public returnType methodName(parameterType parameterName, ..) throws ExceptionName, ExceptionName2 ... {
				
			}

8. The finally block contains code to be executed whether or not an exception is thrown in a try block. The finally always execute when the try block exits. This block is usually used for clean up.

			try {
			   // try block
			} catch (ExceptionOne e) {
			   // catch block
			} finally {
			   // Code to be executed whether or not an exception is thrown
			}

9. Sometimes we can delay handling of an exception. Instead of having the exception to be thrown inside a method, we catch the exception during the method invocation.

10. In the method header, the identify exception is caught using the throws statement.

###########################################################################
# DS CHAP 2 : Introduction to Data Structure
###########################################################################
1. Data structure is an organization of information, usually in computer memory, for better algorithm efficiency.

2. It defines different methods of organizing data. It provides a means to manage large amounts of data efficiently. 

3. Usually have 3 core operations
			a way to add things
			a way to remove things
			a way to access things

4. Type of Operations
			Traversing - Accessing each data element exactly once so that certain items in the data may be processed
			Searching - Finding the location of the data element (key) in the structure
			Insertion - Adding a new data element to the structure
			Deletion - Removing a data element from the structure
			Sorting - Arrange the data elements in a logical order (ascending/descending)
			Merging - Combining data elements from two or more data structures into one

5. The most common data structures include:
			Array
			Linked List
			Stack
			Queue
			Tree
			Graph
			Hash Table

6. Array
	- A container object that holds a fixed number of values of a single type.
   	- Once an array is created, its size cannot be altered.

7. Linked List
	- a linear collection of data elements, with each element linked to the next element. It is a collection of data stored sequentially. It supports insertion and deletion anywhere in the list.

7.1 ArrayList
	- Implemented as a resizable array. 
	- elements can be accessed directly by using the get and set methods just like linked list
	- BUT LinkedList is worse in get and set if compared to ArrayList.

8. Stack
	- a collection of elements that organize in Last In First Out (LIFO). 
	- insertions and deletions take place only at the top of a stack. 

9. Queue
	- a collection of elements that organize in First In First Out (FIFO). 
	- insertions take place at the tail and deletions take place at the head.

10. Tree
	- a non-linear structure that organises the elements in a hierarchical structure.

11. Graph
	- a non-linear structure that made up of a set of elements named vertices and a set of edges that connect the vertices.

12. Hash Map/Table
	- represents a data structure in which collections of unique key and collections of values are stored where each key is associated with one value.

13. Generic allow us to define a set of operations that manipulate objects of a particular class, without specifying the class of the objects. 

14. Generic is a way to re-use the same code with different types of input.

15. T is usually used as a placeholder for the name of a type. A type variable can be any non-primitive type you specify.

16. The commonly used type parameter names are:
			E - Element
			K - Key
			N - Number
			T - Type
			S,U,V etc. - 2nd, 3rd, 4th types

17. The <T extends Comparable<T>> can be in method instead of at the class header.

			public static <T extends Comparable<T>> int countGreaterThan(T[] arr, T t){
				int count = 0;
				for(T e : arr){
					if(e.compareTo(t) > 0) count++;
				}
				return count;
			}

18. Multiple bound
			Class A {...}
			Interface B {...}
			Interface C {...}

			Class D <T extends A & B & C> {...}

19. The Java wildcard operator, ?, can be used for generic polymorphism.

20. LinkedList<? extends ParentClass> allows any LinkedList objects that are instance of ParentClass or sub classes of ParentClass.

21. LinkedList<? super ChildClass> allows any LinkedList objects that are instance of ChildClass or super class of ChildClass.

22. IMPORTANT RULE OF GENERIC
	- Cannot create an instance of a generic type
		T object = new T(); //Error

	- Generic array creation require casting
		T[] a = (T[]) new Object[size];
		T[][] b = (T[][]) new Object[row][column];

	- Exception classes cannot be generic
		public class MyException<T> extends Exception{ } //Error

23. Abstract data type (ADT) is a data type whose properties are specified independently of any particular implementation.

24. The interface can be used in Java to specify ADT.


###########################################################################
# DS CHAP 3 : RECURSION & EXCEPTION HANDLING 
###########################################################################
1. A method definition that includes a call to itself is recursive.

2. Base case is the case without the recursive call. It is used to stop the recursive call.

3. Reverse a String

			public void reverse(String s, int size) {
			   if (size==1)
			      System.out.print(s.charAt(size-1));
			   else {
			      System.out.print(s.charAt(size-1))
			      reverse(s, --size);
			   }
			}

			// base case is size equal to 1

4. Factorial
			public int factorial(int n) {
			   if (n==0) 
			      return 1;
			   else
			      return n*factorial(n-1);
			}

			// base case is n equal to 0

5. Power
			public int power(int x, int n) {
			   if (n==0) 
			      return 1;
			   else
			      return x*power(x, n-1);
			}

			// base case is n equal to 0

6. Binary Search

			int binarySearch(int[] a, int first, int last, int key) {
			   int index;
			   if (first > last)
			      return -1; 
			   else  { 
			      int mid = (first + last)/2;
			      if (key == a [mid])
			         index = mid; 
			      else if (key < a [mid])
			         index = binarySearch(a, first, mid-1, key);     
			      else
			         index = binarySearch(a, mid+1, last, key);
			      return index;
			   }
			}

7. Tower of Hanoi, Blob are the examples