#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int calc_add(int *parr){ // 배열에서 앞의 6자리 숫자의 합 구하는 함수
    int i, add = 0;
    for(i = 0; i < 6; i++){
        add = add + parr[i];
    }
    return add;
}

int main(){
    int arr[6]={}; // 크기가 6인 배열 생성
    int i = 0;
    int answer = 0;
    printf("enter 6 numbers \n");

    for(i = 0; i <6; i++){
        scanf("%d", &arr[i]); // 배열의 앞 공간부터 입력받은 숫자를 저장
    }
    answer = calc_add(arr);
    printf("%d", answer);
    
    return 0;
}
