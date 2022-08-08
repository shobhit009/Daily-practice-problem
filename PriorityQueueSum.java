import java.io.*;
import java.util.*;
class PriorityQueueSum {
    public static void main(String[] args){
        System.out.println(minOperations([7,3,7,1,8,10,1,5,6],9,7));
    }

   int static minOperations(int[] arr, int n, int k) {
       // code here
       int cnt=0;
       PriorityQueue<Integer> pq=new PriorityQueue<>();
       for(int i:arr){
           pq.add(i);
       }
       while(pq.peek()<k){
           int a=pq.poll();
           int b=pq.poll();
           cnt++;
           pq.add(a+b);
       }
       return cnt;
   }
}
 