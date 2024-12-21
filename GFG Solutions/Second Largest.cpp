class Solution {
  public:
    // Function returns the second
    // largest elements
int getSecondLargest(vector<int> &arr) {
        // Code Here
        int secondLargest=-1;
        int n=arr.size();
        int largest=arr[0];
        for(int i=1;i<n;i++)
        {
            if(arr[i]>largest)
            {
                secondLargest=largest;
                largest = arr[i];
            }
            else if(arr[i]<largest && arr[i]>secondLargest)
            {
                secondLargest=arr[i];
            }
        }
        return secondLargest;
    }
};
