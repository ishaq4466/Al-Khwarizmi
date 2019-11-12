import java.util.*;
import java.io.*;
import java.lang.*;




class HackerSolutions1
{
		// Reversing the array
	  static int[] reverseArray(int[] a) {
    		
    		int reverseArr[]=new int[a.length]; //4
    		int lastInd=a.length-1; 	// 
    		for(int i=0;i<a.length;i++,lastInd--)
    		{
    				reverseArr[lastInd]=a[i];
    		}
	  	
	  	return reverseArr;

    }

    static int hourglassSum1(int[][] arr) {

    	System.out.println("Size of arr: "+arr.length);
    	for(int row=0;row<6;row++)
    	{	
    		for(int col=0;col<6;col++)
    			System.out.print(arr[row][col]+" ");
    		
    		System.out.println();
    	}
    	int noOfIterations=arr.length-3+1;
    	System.out.println("noOfIterations: "+noOfIterations);
    	int max=Integer.MIN_VALUE;
    	for(int a=0;a<noOfIterations;a++)
    	{
	    	
	    	int tempArr[][]=new int[3][3];
	    	
    		
    		for(int b=0;b<noOfIterations;b++)
    		{
	    		int sum=0;
	    		System.out.println("=====================");
		    	for(int i=a,m=0; i<(3+a);i++,m++)
		    	{
		    		for(int j=b,n=0;j<(3+b);j++,n++)
		    		{
		    			
		    			tempArr[m][n]=arr[i][j];
		    			System.out.print(arr[i][j]+" ");
		    			// tempArr[i-a][j-b]=arr[i][j];
		    		}
		    		System.out.println();
		    	}
			    // System.out.println("*********************");
			    for(int x=0;x<3;x++)
			    {for(int y=0;y<3;y++)
			    	{
			    		// System.out.print(tempArr[x][y]);
			    		if(x==1 && (y==0||y==2))
			    			continue;	
			    		sum+=tempArr[x][y];
			    	}
				    System.out.println();
			    }	
			    System.out.println("Sum is: "+sum);
			    if(max<sum)
			    {
			    	max=sum;
			    }

			    System.out.println("Maximum is: "+max);
			    System.out.println("*********************");
		    }


		  }

    	return 0;
	   }

	  static int[] matchingStrings(String[] strings, String[] queries) {
	  	int returnArray[]=new int[queries.length];
	  	Map<String,Integer> stringsMap=new HashMap<String,Integer>();
	  

		  	for(int i=0;i<strings.length;i++)
		  	{
		  		Integer n=stringsMap.get(strings[i]);
		  		if(n==null)
		  			stringsMap.put(strings[i],1);
		  		else
		  		{
		  			++n;
		  			stringsMap.put(strings[i],n);
		  		}
		  	}

		  for(int i=0;i<queries.length;i++)
		  {	
		  	if(stringsMap.containsKey(queries[i])==false)
		  		returnArray[i]=0;
		  	else
		  		returnArray[i]=stringsMap.get(queries[i]);
		  }
		  return returnArray;
	   }


// [1,2,3,4,5]--> [2,3,4,5,1]	
	static int[] rotateLeftArr(int arr[],int d)
	{

		for(int i=0; i<d;i++)
		{
			int temp=arr[0];
			for(int j=0;j<arr.length-1;j++)
			{
				arr[j]=arr[j+1];
				System.out.print(arr[j]+" ");	
			}
			arr[arr.length-1]=temp;
			System.out.print(arr[arr.length-1]+" ");	
			System.out.println();
		}

		return arr;
	}
		/*		int n=5; int queries[][]={
																		{1,2,100},
																		{2,5,100},
																		{3,4,100},
																		{1,3,200};   }
		*/
		

		static long arrayManipulation(int n, int[][] queries) {
					System.out.println(n+" "+queries.length);

                int returnArray[]=new int[n];
               System.out.println(Arrays.toString(returnArray));
                for(int i=0;i<queries.length;i++)
                {		
                	System.out.println(Arrays.toString(queries[i]));
                    for(int start=queries[i][0]-1;start<queries[i][1];start++)
                    {
                        returnArray[start]+=queries[i][2];
                    }
                   System.out.println(Arrays.toString(returnArray));
                }
                long maxElement=0;
                for(int i=0;i<returnArray.length;i++)
                    if(maxElement<returnArray[i])
                        maxElement=returnArray[i];
                return maxElement;

                }

	public static void main(String args[])
	{
			/*
			// Solution for the reverse array
			int arr1[]={1,23,45,66,88,0};
			for(int i=0; i<arr1.length; i++)
			System.out.print(arr1[i]+" ");
			System.out.println();
			System.out.println("Revrse Array: "+Arrays.toString(reverseArray(arr1)));*/

			/*
			// 2D hour glass sum
			//int arr2[][]={{1,1,1,0,0,0},{0,1,0,0,0,0},{1,1,1,0,0,0},{0,0,2,4,4,0},{0,0,0,2,0,0},{0,0,1,2,4,0}};
			int arr2[][]={
			{-9,-9 ,-9 , 1, 1, 1},
			{ 0 ,-9 , 0,  4 ,3 ,2},
			{-9 ,-9 ,-9 , 1 ,2 ,3},
			{ 0 , 0 , 8  ,6 ,6 ,0},
			{ 0 , 0,  0 ,-2 ,0 ,0},
			{0  ,0,  1  ,2, 4, 0}};
			System.out.println(hourglassSum1(arr2));
			*/
			// Left Array rotation solution
			/*
				int a[]={1,2,3,4,5};	
			  int d=2; int array[];
				for(int i=0; i<a.length;i++) {
            array[(i+n-d)%n] = a[i];
        	}
			a=rotateLeftArr(a,4);
			for(int i=0;i<a.length;i++)
				System.out.print(a[i] +" ");
			System.out.println();
			// System.out.println(Arrays.toString(rotateLeftArr(a,4)));
			*/

			/* 
				// Sparse Arrays
				//String strings[]={"def","de","fgh"}, queries[]={"de","lmn","fgh"};
				String strings[]={"aba","baba","aba","xzxb"}, queries[]={"aba","xzxb","ab"};
				System.out.println("Strings: "+Arrays.toString(strings));
	  		System.out.println("Queries: "+Arrays.toString(queries));
				System.out.println(Arrays.toString(matchingStrings(strings,queries)));*/

				// Array manipulation
				// n--> size of the array to be initialized to be zero.
				// queries=[ 1 2 100] ==> add 100 between index 1 and 2
 
				// int n=5; int queries[][]={{1,2,100},{2,5,100},{1,2,100},{1,3,100},{2,5,100}};
				int n=10; int queries[][]={ {1	,5,3}, {4,8,7}, {6,9,1} };
				
				long result = arrayManipulation(n, queries); 
				System.out.println(result);

			}
	}


/*

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int d = scan.nextInt();
        int[] array = new int[n];
        for(int i=0; i<n;i++) {
            array[(i+n-d)%n] = scan.nextInt();
        }
        for(int i=0; i<n;i++) {
            System.out.print(array[i] + " ");
        }      
    }
*/


