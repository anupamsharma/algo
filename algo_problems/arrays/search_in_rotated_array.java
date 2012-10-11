/*
Problem : Searching in rotated array.
   A sorted int array is rotated r(n can be anything and can change) times. Search for a number in it.
   What rotation means:
   Input array : 3, 5, 6, 10, 11, 12
   2 Rotated Array : 11, 12, 3, 5, 6, 10

@Author : Anupam Sharma

This problem is very simple but writing a running code which is taking care of all the cases is somewhat tricky 
(or it is tricky atleast for me...)....


*/
import java.util.*;

public class rotation {
	public static int search(int[] a, int key) {
	
		int left = 0;
		int right = a.length - 1;
		int middle=0;
		int x1=0;
		int x2=0;
		int x3=0;

		while(left <= right) {
			middle = (left + right) / 2;
			x1 = a[left];
			x2 = a[middle];
			x3 = a[right];
			if (key == x2) {return middle;}
			if (x1<=x2) {
				if((key > x2) || (key < x1)) {
					left = middle + 1;
				}
				else {
					right = middle - 1;	 
				}
			}
			else {
					
				if((key > x2) && (key <= x3)) {
					left = middle + 1;
				}
				else {
					right = middle - 1;
				}
				
			}	
		}
		return -1;
	}

	public static int[] rotate(int a[], int r) {
		int i = 0;
	
		while(i < r) {
			int j = 0;
			int last = a[a.length-1];
			int temp1 = a[0];
			int temp2 = 0;
			while (j < (a.length-1)) {
				temp2 = a[j+1];
				a[j+1] = temp1;
				temp1 = temp2;
				j = j + 1;
			}
			a[0] = last;
			i = i + 1;	
		}	
		return a;
	}

	public static void main(String args[]) {
			int a[] = {20,5,8,6,0,10,4,5,22,40,55};
			Arrays.sort(a);

			int count = 0;
			for(int b: a) {
				
				System.out.println(count + " : "+ b);
				count = count + 1;
			}
			a = rotate(a, 5);
			count = 0;
			for(int b: a) {
				
				System.out.println(count + " : "+ b);
				count = count + 1;
			}

			int res = 0;

			res = search(a, 3);
			System.out.println(3+ ":" + res);

			res = search(a, 5);			
			System.out.println(5+ ":" + res);

			res = search(a, 0);			
			System.out.println(0+ ":" + res);


			res = search(a, 55);			
			System.out.println(55+ ":" + res);


			res = search(a, 8);			
			System.out.println(8+ ":" + res);

			res = search(a, 10);			
			System.out.println(10+ ":" + res);
							
	}
}
