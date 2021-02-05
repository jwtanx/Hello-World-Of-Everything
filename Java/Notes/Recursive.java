PERMUTATION PERMUTATION PERMUTATION PERMUTATION PERMUTATION PERMUTATION PERMUTATION PERMUTATION

class Permutations
{
	// Utility function to swap two characters in a character array
	private static void swap(char[] ch, int i, int j)
	{
		char temp = ch[i];
		ch[i] = ch[j];
		ch[j] = temp;
	}

	// Recursive function to generate all permutations of a String
	private static void permutations(char[] ch, int currentIndex)
	{
		if (currentIndex == ch.length - 1) {
			System.out.println(String.valueOf(ch));
		}

		for (int i = currentIndex; i < ch.length; i++)
		{
			swap(ch, currentIndex, i);
			permutations(ch, currentIndex + 1);
			swap(ch, currentIndex, i);
		}
	}

	// generate all permutations of a String in Java
	public static void main(String[] args)
	{
		String s = "ABC";
		permutations(s.toCharArray(), 0);
	}
}


Here’s another Java implementation that doesn’t convert the String to charater array.

class Permutations
{
	// Recursive function to generate all permutations of a String
	private static void permutations(String candidate, String remaining)
	{
		if (remaining.length() == 0) {
			System.out.println(candidate);
		}

		for (int i = 0; i < remaining.length(); i++)
		{
			String newCandidate = candidate + remaining.charAt(i);

			String newRemaining = remaining.substring(0, i) +
								  remaining.substring(i + 1);

			permutations(newCandidate, newRemaining);
		}
	}

	// Find Permutations of a String in Java
	public static void main(String[] args)
	{
		String s = "ABC";
		permutations("", s);
	}
}

JAVAPOINT
public class PermuteString {  
    //Function for swapping the characters at position I with character at position j  
    public static String swapString(String a, int i, int j) {  
        char[] b =a.toCharArray();  
        char ch;  
        ch = b[i];  
        b[i] = b[j];  
        b[j] = ch;  
        return String.valueOf(b);  
    }  
      
    public static void main(String[] args)  
    {  
        String str = "ABC";  
        int len = str.length();  
        System.out.println("All the permutations of the string are: ");  
        generatePermutation(str, 0, len);  
    }  
      
    //Function for generating different permutations of the string  
    public static void generatePermutation(String str, int start, int end)  
    {  
        //Prints the permutations  
        if (start == end-1)  
            System.out.println(str);  
        else  
        {  
            for (int i = start; i < end; i++)  
            {  
                //Swapping the string by fixing a character  
                str = swapString(str,start,i);  
                //Recursively calling function generatePermutation() for rest of the characters   
                generatePermutation(str,start+1,end);  
                //Backtracking and swapping the characters again.  
                str = swapString(str,start,i);  
            }  
        }  
    }  
}  

TOWER OF HANOI TOWER OF HANOI TOWER OF HANOI TOWER OF HANOI TOWER OF HANOI TOWER OF HANOI