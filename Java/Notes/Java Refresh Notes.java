Week 1 - Wednesday 11.09.2019 
=========================================================================================================================================

// public: Mean that main () can be call from anywhere

-----
// static: Mean that main () does not belong to a specific object
// static variables and methods belong to the class instead of specific instance

// eg. Without "static" and you want to use your method in other class, you will need to create an instance

// Class : animal

	animal animalObject = new animal();

	// to run the method:
		animalObject.methodName();

// With "static", we do not need to create an instance
	
	public static void methodName(){

	}

	// to run the method
		animal.methodName()

-----

// void: Mean that main () returns no value
// main: is the name of a function. Main is special because is it start of a program  
// String: mean the data type
// args: args is the argument passed to the function. "args" is not special and you can name it to anything else and the program would work the same

-----

CHAR

char test = 't' ----> ' ' correct
char book = "b" ----> " " wrong

-----
double is more precise than float

-----
//converting double to int

	double a = 10.59

	int aa = (int) a;

	System.out.println(aa)

-----

	int x = 2;

	x++;   -----> 3

++5 (pre increment)
5++ (post increment)

eg:
	x=42
	y=++x
	so , value of x will be 43 and y will be 43 as well.

	but
	
	x=42
	y=x++
	so,value of x will be 43 and y will be 42.

eg2.
	
	int test = 5 ;
	        
        	System.out.println(test++);
        	System.out.println(test);
        	System.out.println(++test);
    	}
	}
	
	// first output: 5 
	// second output: 6 
	// third output: 7

-----

	x+=y means x=x+y
	x-=y means x=x-y
	x*=y means x=x*y
	x/=y means x=x/y
	x%=y means x=x%y

	x=+y means x = y as + is the positive sign
	x=-y means x = -y as - is the positive sign

-----

SCANNER

Scanner s = new Scanner(System.in);

	System.out.println(s.next());

Read a byte - nextByte()
Read a short - nextShort()
Read an int - nextInt()
Read a long - nextLong()
Read a float - nextFloat()
Read a double - nextDouble()
Read a boolean - nextBoolean()
Read a complete line - nextLine()
Read a word - next()

-----

IF STATEMENT

	if (x > 10){
		sysout("x is more than 10");
	}

// NOT(!) logical operator 

	if (!(x > 10)){
		sysout("x is less than 10");
	}

-----

switch statement

int day = 6;

		switch(day){
			
			case 1:
			case 2:
			case 3:
			case 4:
			case 5:
				System.out.print("Work");
				break;

			case 6:
			case 7:
				System.out.print("Holiday");
				break;

eg 2.
	
	char c = 'A';

		switch(c){
			
			case 'A':
			case 'E':
			case 'I':
			case 'O':
			case 'U':
				System.out.print("Vowel");
				break;

			default:
				System.out.print("Not vowel");
			
			// no break is needed in the default section, as it is always the last statement in the switch.


=========================================================================================================================================

Week 1 - Thursday 12.09.2019 

WHILE LOOP

eg.
	
	int x = 5;

	while( x > 0 ){
		
		Sysout(x--);

	}

	/*	
	*	5
	*	4
	*	3
	*	2
	*	1
	*/

-----

FOR LOOP

for (initialization; condition; increment/decrement) {
	statement(s)
}

eg.
	for(int x = 1; x <= 5; x++){
		System.out.println(x);

	}


A for loop is best when the starting and ending numbers are known.

-----

DO...WHILE LOOP

//similar to a while loop, except that a do...while loop is guaranteed to execute at least one time.

eg.

	int x = 10;
		

		do{
		
			System.out.println(x);
			
		} while(x > 10);

	/*
	*	10
	*/

Do not need to create a class instance to repeat the main class

eg.

	int choice;

	do{
		
		[game/class/method]

		sysout("Type 1 to restart the game");

		choice = s.nextInt();

	}while(x == 1);

	Sysout("Session has ended");

// normally used in inserting pin

eg.

	int pin = 1234;
    
	int pn;

    do{ 
       Scanner input = new Scanner (System.in);
       System.out.println("Enter your pin");
       pn = input.nextInt();
    } while (pn != pin);

//unimited retries?


eg. Placing order before checking out.

	// when exit button is tap, goodsNumber == 0;
	
	int goodsNumber;

	do{
		goodsNumber = s.nextInt();

		

	}while(goodsNumber != 0);

-----

LENGTH OF A STRING

eg. 

	String sentence = "hello world";

	int len = sentence.length();

To get the letter one by one

eg.

	for(int i = 1; i <= sentence.length(); i++){
			char c = sentence.charAt(i);              <----- charactering each of the character of sentence.

		}

Other way to do this

eg.

	import java.text.*;
	
	final CharacterIterator it = new StringCharacterIterator(s);
	for(char c = it.first(); c != CharacterIterator.DONE; c = it.next()) {
		// process c...
	}

eg.

	for(char c : Lists.charactersOf(yourString)) {
    	// Do whatever you want     
	}

-----

CALCULATE HOW FAST A PROGRAM RUNS

eg.
	
	long t = System.currentTimeMillis();

    t = System.currentTimeMillis() - t;
    
    System.out.println("After " + t + "msec");


-----

LIST

Generic Lists
By default you can put any Object into a List, but from Java 5, Java Generics makes it possible to limit the types of object you can insert into a List. Here is an example:

List<MyObject> list = new ArrayList<MyObject>();

eg. 
	List<String> nameOfList = new ArrayList<String>();
	
	String s = "a string";
	nameOfList.add(s);
	
	String string2 = nameOfList.get(0);

	System.out.println("", string2);

Adding obejct to a list

eg.

	List<Integer> numlist = new ArrayList<Integer>();

	//OR

	List numlist = new ArrayList();

	numlist.add(5);
	numlist.add(10);
	numlist.add(3);

	// Now the list is
	System.out.println(numlist);

	// To get the num of a specified array
	numlist.get(1);  // <--- output is 10

	// To remove array #2
	numlist.remove(1);

	//After removing, the #3 array becomes #2 array
	numlist.get(1);  // <--- output is 3

-----

RANDOM

// Generate random integers in range 0 to 999 
        int randnum = rand.nextInt(1000); 

// Generate random integers in range 1 to 1000 
        int randnum = 1 + rand.nextInt(1000); 

// Generate Random doubles 
		double rand_dub1 = rand.nextDouble();



-----

NUMBER PRINTING FORMAT

%3.2lf 		//(print as a floating point at least 3 wide and a precision of 2)

%0.2lf      //(print as a floating point at least 0 wide and a precision of 2)

%.2lf       //(print as a floating point at least 0(default) wide and a precision of 2)

-----

TO RESTART MAIN OR METHOD

eg. 
	main(args);

eg. 
	dowork(variable);


-----

DIFFERENT BETWEEN 		int a[] = new int[sizeOfList]	&	 Lists<Integer> a = new ArrayList<Integer>();

LIST ASSIGNING VALUE:
for loop{int k...}
randNumList.add(k, 1 + r.nextInt(100));		<-- FOR List<Integer> randNumList = new ArrayList<Integer>();
randNumList[k] = 1 + r.nextInt(100);   		<--  FOR int randNumList[] = new int[n];

OUTPUT FOR SPECIFIC INDEX
System.out.println(randNumList.get(0)); 	<-- FOR List<Integer> randNumList = new ArrayList<Integer>();
System.out.println(randNumList[0]);     	<-- FOR int randNumList[] = new int[n];

OUTPUT FOR WHOLE LIST
System.out.println(randNumList);			<-- FOR List<Integer> randNumList = new ArrayList<Integer>();

for(int k = 0; k < n; k ++){				<-- FOR int randNumList[] = new int[n];
	
	System.out.println(a[k]);

}

LENGTH OR SIZE
li.size 									<-- FOR List<Integer> randNumList = new ArrayList<>();
li.length 									<-- FOR int randNumList[] = new int[n];

-----

HOW TO PRINT SPECIFIC LETTER FROM A STRING?

String s = "Hello";

char c[] = s.toCharArray();

System.out.println(c[0])	// <--- 'H'

CHECK IF AN ELEMENT IS IN AN ARRAY / ARRAYLIST

=========
For Array
=========
NEED APACHE
String[] fieldsToInclude = { "id", "name", "location" };

if (ArrayUtils.contains( fieldsToInclude, "id" ) ) {
    // Do some stuff.
}

ELSE [ONLY FOR STRING]
public static boolean useList(String[] arr, String targetValue) {
    return Arrays.asList(arr).contains(targetValue);
}

OR

if(Arrays.asList(arr).contains(targetValue)){
	//process
}

Checking if given a key
String[] values = {"AB","BC","CD","AE"};
boolean sInArray = Arrays.stream(values).anyMatch("s"::equals);

================================
AWESOME WORK BUT DONT UNDERSTAND, UNDERSTAND NOW, ITS GENERIC

public static <T> boolean contains(final T[] array, final T v) {
    for (final T e : array)
        if (e == v || v != null && v.equals(e))
            return true;

    return false;
}

Improvement:
The v != null condition is constant inside the method. It always evaluates to the same Boolean value during the method call. So if the input array is big, it is more efficient to evaluate this condition only once, and we can use a simplified/faster condition inside the for loop based on the result. The improved contains() method:

public static <T> boolean contains2(final T[] array, final T v) {
    if (v == null) {
        for (final T e : array)
            if (e == null)
                return true;
    } 
    else {
        for (final T e : array)
            if (e == v || v.equals(e))
                return true;
    }

    return false;
}

================================



=============
FOR ARRAYLIST
=============
public boolean contains(Object o) {
    return indexOf(o) >= 0;
}

OR

ArrayList<String> list = new ArrayList<>(2);
         
    list.add("A");
    list.add("B");
    list.add("C");
    list.add("D");
         
    System.out.println( list.contains("A") );       //true
     
    System.out.println( list.contains("Z") );       //false

-----

HOW TO GET THE MS OF RUNTIME

==JAVASCRIPT==
var start = new Date().getTime();

//PROCESS, CODES

console.log(new Date().getTime() - start);


==JAVA==
long start = System.currentTimeMillis();
// code
System.out.println(System.currentTimeMillis() - start);

OR

public class TestTimeTaken {
    public static void main(String args[]) throws InterruptedException{
        long startTimeNanoSecond = System.nanoTime();
        long startTimeMilliSecond = System.currentTimeMillis();

        //code
        Thread.sleep(1000);
        //code

        long endTimeNanoSecond = System.nanoTime();
        long endTimeMilliSecond = System.currentTimeMillis();

        System.out.println("Time Taken in "+(endTimeNanoSecond - startTimeNanoSecond) + " ns");
        System.out.println("Time Taken in "+(endTimeMilliSecond - startTimeMilliSecond) + " ms");


    }
}


-----

CAPITALIZE FIRST LETTER OF A SENTENCE

String a = "hello";
StringUtils.capitalize(a);


-----

Print 01 instead of 1

String a = String.format("%02d", 1);

-----

GENERATE RANDOM CHARACTER BETWEEN A - Z

char c = (char) (r.nextInt(26) + 'A');

Between 'a' to 'z'
char c = (char) (r.nextInt(26) + 'a');

-----

PRINT WITHOUT SEMICOLON

public class Print_Without_Semicolon 
{
     public static void main(String[] args) 
     {
        int i = 0;
        if(System.out.printf("Sanfoundary!! ") == null) {}
        for(i = 1; i < 2; System.out.println("Hello World."))
        {
            i++;
     	}
     }
}

-----

GET SUM OF ALL INTEGER IN A NUMBER

int num = 1234;
int sum = 0;

while(num > 0){
	
	sum += (num % 10);
	num /= 10;

}

sysout(sum);

-----

GET REVERSED OF A NUMBER

int num = 1234;
int reversed = 0;
int digit;

while(num > 0){
	
	digit = num % 10;
	reversed = (reversed * 10) + digit;
	num /= 10;

	if(reversed == 0) sysout("0");
}

sysout(reversed);

-----

CHECK IF STRING CONSIST

if(a.contains(?=.*[a-z])){
	
}

^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$

descriptions are as follow
(?=.*[a-z])  -- check lower case letter
(?=.*[A-Z]) -- check upper case letter
(?=.*\d) -- check one digit exists

String s = "some text";
boolean hasNonAlpha = s.matches("^.*[^a-zA-Z0-9 ].*$");
one other is to use an external library, such as Apache commons:

String s = "some text";
boolean hasNonAlpha = !StringUtils.isAlphanumeric(s);


string.matches("^\\W*$"); should do what you want, but it does not include whitespace. 
string.matches("^(?:\\W|\\s)*$"); does match whitespace as well.

======

FILE INPUT AND OUTPUT

Difference between FileWriter and PrintWriter
PrintWriter has more features, you can use it to printf, println & print
While FileWriter just write some words and strings using any special features.

---
eg 1. Using File

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;

// IN MAIN
	try {
            File f = new File("fileName.txt");

            if (!f.exists()) {
                f.createNewFile();
            }

            PrintWriter pw = new PrintWriter(f);
            pw.println("ABC");

        } catch (IOException e) {
            
            e.printStackTrace();
            // OR
            System.err.println("Problem with output file");

        }

eg 2. Using File Writer

Writer fileWriter = new FileWriter("data\\filewriter.txt");

fileWriter.write("data 1");

fileWriter.close();


eg 3. Using BufferedWritter
BufferedWritter the simplest way to write the content to a file. It writes text to a character-output stream, buffering characters so as to provide for the efficient writing of single characters, arrays, and strings.

Unless prompt output is required, it is advisable to wrap a BufferedWriter around any Writer whose write() operations may be costly, such as FileWriter and OutputStreamWriter.

As it buffers before writing, so it result in less IO operations, so it improve the performance.

BufferedWritter Example
public static void usingBufferedWritter() throws IOException 
{
    String fileContent = "Hello Learner !! Welcome to howtodoinjava.com.";
     
    BufferedWriter writer = new BufferedWriter(new FileWriter("c:/temp/samplefile1.txt"));
    writer.write(fileContent);
    writer.close();
}


eg 4. Write File using FileWriter/PrintWriter
FileWriter the most clean way to write files. Syntax is self explanatory and easy to read and understand. FileWriter writes directly into file (less performance) and should be used only when number of writes are less.

FileWriter Example
public static void usingFileWriter() throws IOException 
{
    String fileContent = "Hello Learner !! Welcome to howtodoinjava.com.";
     
    FileWriter fileWriter = new FileWriter("c:/temp/samplefile2.txt");
    fileWriter.write(fileContent);
    fileWriter.close();
}


Use PrintWriter to write formatted text to a file. This class implements all of the print methods found in PrintStream, so you can use all formats which you use with System.out.println() statements.

PrintWriter Example
public static void usingPrintWriter() throws IOException 
{
    String fileContent = "Hello Learner !! Welcome to howtodoinjava.com.";
     
    FileWriter fileWriter = new FileWriter("c:/temp/samplefile3.txt");
    PrintWriter printWriter = new PrintWriter(fileWriter);
    printWriter.print(fileContent);
    printWriter.printf("Blog name is %s", "howtodoinjava.com");
    printWriter.close();
}


eg 5. Write File using FileOutputStream
Use FileOutputStream to write binary data to a file. FileOutputStream is meant for writing streams of raw bytes such as image data. For writing streams of characters, consider using FileWriter.

FileOutputStream Example
public static void usingFileOutputStream() throws IOException 
{
    String fileContent = "Hello Learner !! Welcome to howtodoinjava.com.";
     
    FileOutputStream outputStream = new FileOutputStream("c:/temp/samplefile4.txt");
    byte[] strToBytes = fileContent.getBytes();
    outputStream.write(strToBytes);
  
    outputStream.close();
}

eg 6. Write File using DataOutputStream
DataOutputStream lets an application write primitive Java data types to an output stream in a portable way. An application can then use a data input stream to read the data back in.

DataOutputStream Example
public static void usingDataOutputStream() throws IOException 
{
    String fileContent = "Hello Learner !! Welcome to howtodoinjava.com.";
     
    FileOutputStream outputStream = new FileOutputStream("c:/temp/samplefile5.txt");
    DataOutputStream dataOutStream = new DataOutputStream(new BufferedOutputStream(outputStream));
    dataOutStream.writeUTF(fileContent);
  
    dataOutStream.close();
}

eg 7. Write File using FileChannel
FileChannel can be used for reading, writing, mapping, and manipulating a file. If you are dealing with large files, FileChannel can be faster than standard IO.

File channels are safe for use by multiple concurrent threads.

FileChannel Example
public static void usingFileChannel() throws IOException 
{
    String fileContent = "Hello Learner !! Welcome to howtodoinjava.com.";
     
    RandomAccessFile stream = new RandomAccessFile("c:/temp/samplefile6.txt", "rw");
    FileChannel channel = stream.getChannel();
    byte[] strBytes = fileContent.getBytes();
    ByteBuffer buffer = ByteBuffer.allocate(strBytes.length);
    buffer.put(strBytes);
    buffer.flip();
    channel.write(buffer);
    stream.close();
    channel.close();
}

eg 8. Write File using Java 7 Path
Java 7 introduced Files utility class and we can write a file using it’s write function, internally it’s using OutputStream to write byte array into file.

Path Example
public static void usingPath() throws IOException 
{
    String fileContent = "Hello Learner !! Welcome to howtodoinjava.com.";
     
    Path path = Paths.get("c:/temp/samplefile7.txt");
  
    Files.write(path, fileContent.getBytes());
}

---
Summary
1. If we try to write to a file that doesn’t exist, the file will be created first and no exception will be thrown (except using Path method).
2. Always close the output stream after writing the file content to release all resources. It will also help in not corrupting the file.
3. Use PrintWriter is used to write formatted text.
4. Use FileOutputStream to write binary data.
5. Use DataOutputStream to write primitive data types.
6. Use FileChannel to write larger files.

=====
APPENDING FILE
eg 1. Appending vs Overwriting

Writer fileWriter = new FileWriter("c:\\data\\output.txt", true);  //appends to file

Writer fileWriter = new FileWriter("c:\\data\\output.txt", false); //overwrites file


eg 2. Flushing

The Java FileWriters flush() method flushes all data written to the FileWriter to the underlying file. The data might be buffered in OS memory somewhere, even if your Java code has written it to the FileWriter. By calling flush() you can assure that any buffered data will be flushed (written) to disk. Here is an example of flushing data written to a Java FileWriter by calling its flush() method:

fileWriter.flush();

example:
String s = "Hello World";

      // create a new writer
      Writer writer = new PrintWriter(System.out);

      try {
         // append a string
         writer.append(s);

         // flush the writer
         writer.flush();

         // append a new string in a new line
         writer.append("\nThis is an example");

         // flush the stream again
         writer.close();

      } catch (IOException ex) {
         ex.printStackTrace();
      }
   }
}


eg 3. Appending using BuffleWriter
:: BufferedWritter buffers before writing, so it result in less IO operations, so it improve the performance.

public static void usingBufferedWritter() throws IOException 
{
    String textToAppend = "Happy Learning !!";
     
    BufferedWriter writer = new BufferedWriter(
                                new FileWriter("c:/temp/samplefile.txt", true)  //Set true for append mode
                            );  
    writer.newLine();   //Add new line
    writer.write(textToAppend);
    writer.close();
}


eg 4.  Append to File using PrintWriter
:: Use PrintWriter to write formatted text to a file.

public static void usingPrintWriter() throws IOException 
{
    String textToAppend = "Happy Learning !!";
     
    FileWriter fileWriter = new FileWriter("c:/temp/samplefile.txt", true); //Set true for append mode
    PrintWriter printWriter = new PrintWriter(fileWriter);
    printWriter.println(textToAppend);  //New line
    printWriter.close();
}


eg 5. Append to File using FileOutputStream
:: Use FileOutputStream to write binary data to a file. FileOutputStream is meant for writing streams of raw bytes such as image data. For writing streams of characters, consider using FileWriter.

public static void usingFileOutputStream() throws IOException 
{
    String textToAppend = "\r\n Happy Learning !!"; //new line in content
     
    FileOutputStream outputStream = new FileOutputStream("c:/temp/samplefile.txt", true);
    byte[] strToBytes = textToAppend.getBytes();
    outputStream.write(strToBytes);
  
    outputStream.close();
}


eg 6. Append to File using Files class
:: With Files class, we can write a file using it’s write function, internally it’s using OutputStream to write byte array into file.

To append content to an existing file, Use StandardOpenOption.APPEND while writing the content.

public static void usingPath() throws IOException 
{
    String textToAppend = "\r\n Happy Learning !!"; //new line in content
     
    Path path = Paths.get("c:/temp/samplefile.txt");
  
    Files.write(path, textToAppend.getBytes(), StandardOpenOption.APPEND);  //Append mode
}

=====
Create Read Only File Example

To make a file read only in java, you can use one of below methods. 3rd method using Runtime.getRuntime().exec() is platform specific because of command you pass to it as parameter. Rest two methods will work fine in most cases.

If you want to change Linux/unix specific file properties e.g. using “chmod 775” then java does not provide any way to do it. You should use third method using “Runtime.getRuntime().exec()”.

1) Use java.io.File.setReadOnly() method
private static void readOnlyFileUsingNativeCommand() throws IOException 
{
    File readOnlyFile = new File("c:/temp/testReadOnly.txt");
     
    //Mark it read only
    readOnlyFile.setReadOnly();
     
    if (readOnlyFile.exists()) 
    {
        readOnlyFile.delete();
    }
    readOnlyFile.createNewFile();
}

2) Use java.io.File.setWritable(false) method
private static void readOnlyFileUsingSetWritable() throws IOException 
{
    File readOnlyFile = new File("c:/temp/testReadOnly.txt");
    if (readOnlyFile.exists()) 
    {
        readOnlyFile.delete();
    }
    readOnlyFile.createNewFile();
     
    //Mark it read only
    readOnlyFile.setWritable(false);
}

3) Execute a native command (platform dependent)
private static void readOnlyFileUsingSetReadOnly() throws IOException 
{
    File readOnlyFile = new File("c:/temp/testReadOnly.txt");
    //Mark it read only in windows
    Runtime.getRuntime().exec("attrib " + "" + readOnlyFile.getAbsolutePath() + "" + " +R");
}

===
LECTURER NOTES	LECTURER NOTES	LECTURER NOTES	LECTURER NOTES	LECTURER NOTES	LECTURER NOTES	LECTURER NOTES	LECTURER NOTES

1. WRITING TO TEXT FILE
---	
import java.io.PrintWriter;
import java.io.FileOutputStream;
import java.io.IOException;

try {
   PrintWriter outputStream = new PrintWriter(new FileOutputStream("data.txt"));
   …

   outputStream.printf("blablabla");
   outputStream.println("blablabla");
   outputStream.print("blablabla");

   …
   outputStream.close();
} catch (IOException e) {
   System.out.println("Problem with file output"); 
}

WRITING TO A SPECIFIED DIRECTORY
---
PrintWriter outputStream = new PrintWriter(new FileOutputStream("d:/sample/data.txt"))

APPENDING TO A TEXT FILE
---
PrintWriter outputStream = new PrintWriter(new FileOutputStream("d:/sample/data.txt", true));


2. READING FROM TEXT FILE
---
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

try {
   Scanner inputStream = new Scanner(new FileInputStream("data.txt"));
   …

	String input = inputStream.nextLine();
	int num1 = inputStream.nextInt();
	double num2 = inputStream.nextDouble();

   …
   inputStream.close();			// <--- ALWAYS REMEMBER TO CLOSE
} catch (FileNotFoundException e) {
   System.out.println("File was not found"); 
}

---
TO CHECK FOR THE END OF A TEXT FILE
while(inputStream.hasNextLine()){
	
}

---
TO OPEN FILE FROM A SPECIFIED DIRECTORY
Scanner inputStream = new Scanner(new FileInputStream("d:/sample/data.txt"));

---
USING BUFFEREDREADER TO READ TEXT FILE

BufferedReader inputStream = new BufferedReader(new FileReader("sample.txt"));

EG USING BUFFEREDREADER
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

try {
   BufferedReader inputStream = new BufferedReader (new FileReader("data.txt"));
   …
   inputStream.close();
} catch (FileNotFoundException e) {
   System.out.println("File was not found");  
} catch (IOException e) {
   System.out.println("Error reading from file");
}

---
To check for the end of a text file
while ( (input=inputStream.readLine()) != null ){
	
}

---
To open file from a specified directory
BufferedReader inputStream = new BufferedReader( new FileReader("d:/sample/data.txt") );

=====
FILE CLASS

File class contains methods that used to check the properties of the file.
The file class is loaded using import java.io.File;

File fileObject = new File("data.txt");
if (fileObject.exists()) {
   System.out.println("The file is already exists");
   fileObject.renameTo("data1.txt");
}
if (fileObject.canRead())
   System.out.println("The file is readable");
if (fileObject.canWrite())
   System.out.println("The file is writable");

---
WRITING TO A BINARY FILE

ObjectOutputStream is the stream class that used to write data to a binary file.

ObjectOutputStream streamObject = new ObjectOutputStream (new FileOutputStream(FileName));

The writeInt, writeDouble, writeChar, writeBoolean can be used to write then value of different variable type to the output stream. Use writeUTF to write String object to the output stream.

eg. 
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.FileOutputStream;
try {
   ObjectOutputStream outputStream = new ObjectOutputStream (new FileOutputStream("data.dat"));
   …
   outputStream.close();
} catch (IOException e) {
   System.out.println("Problem with file output.");
}

---
READING FROM BINARY FILE
ObjectInputStream is the stream class that used to read a binary file written using ObjectOutputStream

ObjectInputStream streamObject = new ObjectInputStream (new FileInputStream(FileName));

The ObjectInputStream, FileInputStream and IOException, FileNotFoundException class need to be loaded using the import statement.

The readInt, readDouble, readChar, readBoolean can be used to read the value from the input stream. Use readUTF to read String object from the input stream.

eg. 
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.ObjectInputStream;
import java.io.FileOutputStream;
try {
   ObjectInputStream inputStream = new ObjectInputStream (new FileInputStream("data.dat"));
   …
   inputStream.close();
} catch (FileNotFoundException e) {
   System.out.println("File was not found"); 
} catch (IOException e) {
   System.out.println("Problem with file output.");
}

---
To check for the end of a text file
Use EOFException 
try {
   while(true) {
      number = inputStream.readInt();
   }
} catch (EOFException e) { }

-----

PrintWriter use IOExeption

Scanner use FileNotFoundException

// LINE BY LINE
	while(s.hasNextLine()){
        System.out.println("The string is \"" + s.nextLine() + "\"");
    }

// WORD BY WORD
	while(s.hasNext()){
        System.out.println("The string is \"" + s.next() + "\"");
    }

// ADDING ALL NUMBER IN A FILE

	try{
        
        Scanner s = new Scanner(new FileInputStream("number.txt"));
        int sum = 0;
        int num;
        
        // String input = s.nextLine();
        while(s.hasNextInt()){
            num = s.nextInt();
            sum += num;
        }
        System.out.println(sum);
        s.close();
        
    } catch(FileNotFoundException e){
        System.err.println("File not found");
    }


// Binary FILE
try {
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("testdat.dat"));
        
        out.writeUTF("Welcome Back");   // <----  String use UTF
        // out.writeBytes("Welcome Back");
        out.writeInt(20);
        out.writeDouble(3123.123);
        
        out.close();
        
    } catch (IOException e) {
        System.err.println("Error with file");
    }


// Reading a Binary File 
try {
        ObjectInputStream in = new ObjectInputStream(new FileInputStream("testdat.dat"));
        
        System.out.println(in.readUTF());   // <----  String use UTF
        System.out.println(in.readInt());
        System.out.println(in.readDouble());
        
        in.close();
        
    } catch(FileNotFoundException e){
    	System.err.println("File not found!");

    } catch (IOException e) {
        System.err.println("Error with file");
    }

// ObjectInputStream doesnt have has.nextInt() like s.readInt() from txt file
// so we need to use EOFException - End of File Exception. When there is no more data = no data is read, the program will go to this exception.

ObjectInputStream in = new ObjectInputStream (new FileInputStream("number.dat"));
int sum = 0;
try{
	
	while(true){
		int num = in.readInt();
		sum += num;
	}
} catch(EOFException e){
	//sout("End of data");
}

sysout(sum);
in.close();

// PrintWriter and Scanner together in a try block
try {
   		PrintWriter p = new PrintWriter(new FileOutputStream("reverse1.txt")); 
    	Scanner s = new Scanner(new FileInputStream("exam.txt"));
       	int line=0;
       	while(s.hasNextLine()) {
           s.nextLine();
           line++;
        }
        s.close();
        String[] str1 = new String[line];           
        s = new Scanner(new FileInputStream("exam.txt"));
        for(int i =0; i<line; i++ ) {
            str1[i] =  s.nextLine();
        }
        for(int i=line-1; i>=0; i--) {              
           	for(int j=str1[i].length()-1; j>=0; j--) {
               	p.print(str1[i].charAt(j));
           	}  
           	p.println();
        }           
        s.close();
        p.close();
     
    } catch (FileNotFoundException e) {
        System.out.println("File was not found"); 
    }

BINARY READ FILE
    try {
            ObjectInputStream in = new ObjectInputStream (new FileInputStream("data.dat"));
            System.out.println(in.readUTF());      
            System.out.println(in.readInt());
            System.out.println(in.readDouble());
            in.close();
            
            ObjectInputStream in1 = new ObjectInputStream (new FileInputStream("number.dat"));
            int sum=0;
            try {            
                while (true) {            
                   int num = in1.readInt();
                    sum+=num;
                    System.out.print(num + " "); 
                }                
            } catch (EOFException e) {
            
            }
            System.out.println("\nTotal is " + sum);
            in1.close();
            
            
        } catch (FileNotFoundException e) {
            System.out.println("File was not found"); 
        } catch (IOException e) {
            System.out.println("Problem with file");
        }

CONVERTING DEC TO H B O
int no=44;

 	String bNo=Integer.toString(no,2);//binary output 101100
 	String oNo=Integer.toString(no,8);//Oct output 54
 	String hNo=Integer.toString(no,16);//Hex output 2C

  	String bNo1= Integer.toBinaryString(no);//binary output 101100
  	String oNo1=Integer.toOctalString(no);//Oct output 54
  	String hNo1=Integer.toHexString(no);//Hex output 2C

  	String sBNo="101100";
  	no=Integer.parseInt(sBNo,2);//binary to int output 44

  	String sONo="54";
  	no=Integer.parseInt(sONo,8);//oct to int  output 44

  	String sHNo="2C";
  	no=Integer.parseInt(sHNo,16);//hex to int output 44

ANOTHER WAY
Solution 1 :

public static void main(String[] args) {

    String str = "CC%";
    String result = "";
    char[] messChar = str.toCharArray();

    for (int i = 0; i < messChar.length; i++) {
        result += Integer.toBinaryString(messChar[i]) + " ";
    }

    System.out.println(result);
}
prints :

1000011 1000011 100101

Solution 2 :

Possibility to choose the number of displayed bits per char.

public static String toBinary(String str, int bits) {
    String result = "";
    String tmpStr;
    int tmpInt;
    char[] messChar = str.toCharArray();

    for (int i = 0; i < messChar.length; i++) {
        tmpStr = Integer.toBinaryString(messChar[i]);
        tmpInt = tmpStr.length();
        if(tmpInt != bits) {
            tmpInt = bits - tmpInt;
            if (tmpInt == bits) {
                result += tmpStr;
            } else if (tmpInt > 0) {
                for (int j = 0; j < tmpInt; j++) {
                    result += "0";
                }
                result += tmpStr;
            } else {
                System.err.println("argument 'bits' is too small");
            }
        } else {
            result += tmpStr;
        }
        result += " "; // separator
    }

    return result;
}
public static void main(String args[]) {
    System.out.println(toBinary("CC%", 8));
}
prints :

01000011 01000011 00100101

=====
HOW TO EXPAND AN ARRAY

Anytime i have to perform a task like this, I always use ArrayLists, add new items to the ArrayList, then cast the ArrayList to an array prior to using it in a ListView etc.

However, in the case that I wouldnt have the ability to use an ArrayList first, you could always take the initial array and cast it into a second array of the original array size + 1.

String[] arr1 = new String[1];
String[] arr2;

arr2 = new String[arr1.length() + 1];
Then copy arr1 into arr2. This can be done manually, of course, but using a for loop would be most efficient.

for (int i = 0; i < arr1.length(); i++) {
    arr2[i] = arr1[i];
}
Finally, you can add the final item into arr2 at the final index.

arr2[arr1.length() + 1] = "New Employee Information";
Similarly, you could delete an item in the reverse fashion. It gets a little more complex because you need to filter for the item that you're removing, or you'd need to know the array index of the item to remove it. But, by rebuilding the array, youll always have an array of the exact size of the items youre holding.


=====
Date Format

Date dNow = new Date( );
SimpleDateFormat ft = 
new SimpleDateFormat ("E yyyy.MM.dd 'at' hh:mm:ss a zzz");

System.out.println("Current Date: " + ft.format(dNow));

// Output
Current Date: Sun 2004.07.18 at 04:14:09 PM PDT

G	Era designator	AD
y	Year in four digits	2001
M	Month in year	July or 07
d	Day in month	10
h	Hour in A.M./P.M. (1~12)	12
H	Hour in day (0~23)	22
m	Minute in hour	30
s	Second in minute	55
S	Millisecond	234
E	Day in week	Tuesday
D	Day in year	360
F	Day of week in month	2 (second Wed. in July)
w	Week in year	40
W	Week in month	1
a	A.M./P.M. marker	PM
k	Hour in day (1~24)	24
K	Hour in A.M./P.M. (0~11)	10
z	Time zone	Eastern Standard Time
'	Escape for text	Delimiter'
"	Single quote	`			"

String time = "15:30:18";

DateFormat sdf = new SimpleDateFormat("hh:mm:ss");
Date date = sdf.parse(time);

System.out.println("Time: " + sdf.format(date));


=====
Calculating two dates

public static long getDifferenceDays(Date d1, Date d2) {
    long diff = d2.getTime() - d1.getTime();
    return TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS);
}


import java.text.DateFormat; 
import java.text.SimpleDateFormat; 
import java.util.Date; 
  
public class SectoDate { 
    public static void main(String args[]) 
    { 
  
        // milliseconds 
        long miliSec = 3010; 
  
        // Creating date format 
        DateFormat simple = new SimpleDateFormat("dd MMM yyyy HH:mm:ss:SSS Z"); 
  
        // Creating date from milliseconds 
        // using Date() constructor 
        Date result = new Date(miliSec); <------- IMPORTANT
  
        // Formatting Date according to the 
        // given format 
        System.out.println(simple.format(result)); 
    } 
} 

=====
TERNARY

sout(x + y == 2 ? "Yes" : "No");


=====
Check if prime

public static boolean isPrime(int n) {

        for (int i = 2; i < n/2; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }

=====
Check if leap year

if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0){
    System.out.println("It is a leap year.");
} else {
    System.out.println("It is not a leap year.");
}

=====
Standard deviation

There is a simple formula that can be used to quickly calculate standard deviation every time a number is added. Here is some code that implements that formula, assuming total[] has been declared and populated already:

double powerSum1 = 0;
double powerSum2 = 0;
double stdev = 0;

for i = 0 to total.length {
    powerSum1 += total[i];
    powerSum2 += Math.pow(total[i], 2);
    stdev = Math.sqrt(i*powerSum2 - Math.pow(powerSum1, 2))/i;
    System.out.println(total[i]); // You specified that you needed to print 
                                  // each value of the array
}
System.out.println(stdev); // This could also be placed inside the loop 
                           // for updates with each array value.
The beauty of this formula is that you don't have to reprocess the entire array each time you add a new value and you don't have to store any of the old values of the array, just the three variables declared in the code above.

=====
Bubble sort

In increasing order
// control number of passes
 	for ( int pass = 1; pass < b.length; pass++ ) 
         	// control number of comparison
		for ( int i = 0; i < b.length - 1; i++ ) 
			if ( b[ i ] > b[ i + 1 ] )  {
				int hold = b[i];        
				b[i] = b[i+1];  
				b[i+1] = hold;
			}

=====
Array List to Array

List<Integer> list = new ArrayList<>();
a.add(1);
a.add(2);
a.add(3);

int[] array = list.stream().mapToInt(i -> i).toArray();
OR
int[] array = list.stream().mapToInt(Integer::intValue).toArray();

======
Replace all symbol

public class App{

public static void main(String args[]) {

String text = "This - text ! has \\ /allot # of % special % characters";
text = text.replaceAll("[^a-zA-Z0-9]", "");
System.out.println(text);

String html = "This is bold";
html = html.replaceAll("[^a-zA-Z0-9\\s+]", "");
System.out.println(html);
}

}

Output
Thistexthasallotofspecialcharacters
b This is bold b

=====
Get day of the week in integer and in string
LocalDate dt = LocalDate.of(yy, mm, dd);
System.out.print(dt.getDayOfWeek());
>> FRIDAY

System.out.println(DayOfWeek.of(1));
>> MONDAY

int dayOfWeekNumber = dt.getDayOfWeek().getValue();
>> dayOfWeekNumber == 5

System.out.println(dt.format(DateTimeFormatter.ofPattern("dd/MM/YYYY")));
>> 27/05/2020


=====
GET WINDOWS DESKTOP PATH
File home = FileSystemView.getFileSystemView().getHomeDirectory(); 
and then if you need it as a string 
home.getAbsolutePath();


=====
CREATE A FOLDER
mkdirs() for many folders
File f = (new File("../potentially/long/pathname/without/all/dirs")).mkdirs();

mkdir() for one folder
File dir = new File("nameoffolder");
dir.mkdir();

=====
How to get the key set of a hashmap

import java.util.*;
public class Demo {
	public static void main(String args[]) {
		
		// Create hash map
		HashMap hm = new HashMap();
		hm.put("Wallet", new Integer(700));
		hm.put("Belt", new Integer(600));
		hm.put("Backpack", new Integer(1200));
		System.out.println("Map = "+hm);
		System.out.println("\nKeys...");
		Set keys = hm.keySet();
		Iterator i = keys.iterator();

		while (i.hasNext()) {
			System.out.println(i.next());
		}

		System.out.println("\nValues...");
		Collection getValues = hm.values();
		i = getValues.iterator();

		while (i.hasNext()) {
			System.out.println(i.next());
		}

	}
}

=====
Simple hashmap explanation

// First create a HashMap  that stores String as key, Queue as value (key = String, value = Queue) 
HashMap<String, Queue<String>> allQueues = new HashMap<>(); 

// Then to process your inputs:  
if (allQueues.containsKey(productCode)){ 
// this means you have already created a queue for this product code, simply enqueue it to the existing queue 
allQueues.get(productCode).enqueue(product); 
} 

else { 
// Queue for the productCode doesn’t exist. Create a new queue and put it in the hashmap 
Queue<String> q = new Queue<>(); 
q.enqueue(product); 
allQueues.put(productCode, q); 
} 

=====
Get the days difference [ONLY FOR JODATIME]
private static void dateDiff() {

    System.out.println("Calculate difference between two dates");
    System.out.println("=================================================================");

    DateTime startDate = new DateTime(2000, 1, 19, 0, 0, 0, 0);
    DateTime endDate = new DateTime();

    Days d = Days.daysBetween(startDate, endDate);
    int days = d.getDays();

    System.out.println("  Difference between " + endDate);
    System.out.println("  and " + startDate + " is " + days + " days.");

}

// my method
Date today = new Date();
long diff = today.getTime() - lastModified.getTime();

return TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS) > 5; // more than 5 days

=====
Minus days in Calendar
Date now = new Date();
Calendar cal = Calendar.getInstance();
cal.setTime(now);
System.out.println(cal.getTime());
cal.add(Calendar.DAY_OF_MONTH, -1);
System.out.println(cal.getTime());

=====
Convert one type to another, casting
float[] A = { 0.1f, 0.2f, 0.6f };
int[] B = Array.ConvertAll(A, x => (int)x);

float[] A = { 0.1f, 0.2f, 0.6f };
int[] B = A.Cast(Of int).ToArray();

Array.newInstance(Class<?> componentType, int length)
Arrays of Objects: Integer[] a = (Integer[])Array.newInstance(Integer.class, 5);
Arrays of primitives: int[] b = (int[])Array.newInstance(int.class, 5);
Arrays of Arrays: int[][] c = (int[][])Array.newInstance(b.getClass(), 5);
