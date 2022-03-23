#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

void bubble_sort(int arr[])    // 매개변수로 정렬할 배열과 요소의 개수를 받음
{
    int temp;

    for (int i = 0; i < 6; i++)    // 요소의 개수만큼 반복
    {
        for (int j = 0; j < 5; j++)   // 
        {
            if (arr[j] > arr[j + 1])          // 현재 요소의 값과 다음 요소의 값을 비교하여
            {                                 // 큰 값을
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;            // 다음 요소로 보냄
            }
        }
    }
    printf("[");
    for (int c = 0; c<6; c++){
        printf("%d, ",arr[c]);
    }
    printf("]");
}


int main(){
    int arr[6]={}; // 크기가 6인 배열 생성
    printf("enter 6 numbers \n");
    scanf("%d %d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4], &arr[5]); // 입력받은 숫자들을 배열의 각 자리에 입력

    bubble_sort(arr);
    
    return 0;
}
