#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int calc_add(int *parr){
    int i, add = 0;
    for(i = 0; i < 6; i++){
        add = add + parr[i];
    }
    return add;
}

int main(){
    int arr[6]={};
    int i = 0;
    int answer = 0;
    printf("sum of six numbers \n");

    for(i = 0; i <6; i++){
        printf("enter a num%d \n",i+1);
        scanf("%d", &arr[i]);
    }
    answer = calc_add(arr);
    printf("%d", answer);
}