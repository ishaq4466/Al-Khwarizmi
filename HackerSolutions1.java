import java.util.*;
import java.io.*;
import java.lang.*;




class DataStruct1
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
			System.out.println(hourglassSum1(arr2));*/
			

			}
}