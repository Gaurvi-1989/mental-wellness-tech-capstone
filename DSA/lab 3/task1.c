// task 1: Implement push pop on a stack of integers. program must print appropriate messages
//  for stack overflow, underflow and stack empty

// task 2: Implement the various searching techniques over the list of integers

#include <stdio.h>

// Linear Search
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i; // found
    }
    return -1;
}

// Binary Search (requires sorted array)
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}


int main() {
    int arr[50], n, choice, key, pos;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nSearching Methods:\n");
    printf("1. Linear Search\n");
    printf("2. Binary Search\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    printf("Enter key to search: ");
    scanf("%d", &key);

    switch (choice) {
        case 1:
            pos = linearSearch(arr, n, key);
            break;
        case 2:
            pos = binarySearch(arr, n, key);
            break;
        default:
            printf("enter validchoice!\n");
            return 0;
    }

    if (pos != -1)
        printf("Element found at index %d\n", pos);
    else
        printf("Element not found.\n");

    return 0;
}