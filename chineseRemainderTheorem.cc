#include<iostream>
using namespace std;

int gcd(int a, int b){
    int gcd, i;
    for(i = 1; i <= a; i++)
        if(a%i == 0 && b%i == 0)
            gcd = i;
    return gcd;
}

int getInv(int a, int n){
    int i;
    if(gcd(a,n) != 1) {
        cout<<"Inverse doesn't exist!"<<endl;
        exit;
    }
    for (i = 0; i < n; i++)
        if ((a * i) % n == 1)
            return i;
    return 0;
}

int crt(int a[], int m[], int len){
    int prod = 1, x, i, capM[len], mInv[len], finVal = 0;
    for(i = 0; i < len; i++)
        prod *= m[i];
    for(i = 0; i < len; i++){
        capM[i] = prod / m[i];
        mInv[i] = getInv(capM[i], m[i]);
        finVal += a[i] * capM[i] * mInv[i];
    }
    x = finVal % prod;
    return x;
}

int main(){
    jump:
    int len = 2, i = 0, j;
    cout<<"##--CHINESE REMAINDER THEOREM--##"<<endl;
    cout<<"Enter number of equations: ";
    cin>>len;
    int a[len], m[len];
    cout<<"Enter values of respective aₖ and mₖ in equations x = aₖ mod mₖ ."<<endl;
    while(i<len){
        cout<<"Enter value of a"<<i+1<<": ";
        cin>>a[i];
        cout<<"Enter value of m"<<i+1<<": ";
        cin>>m[i];
        i++;
    }
    for(i = 0; i < len; i++){
        for(j = 0; j < len; j++){
            if(i != j && gcd(m[i], m[j]) != 1){
                cout<<m[i]<<" and "<<m[j]<<" are not co-prime values.";
                cout<<endl<<"RESTART!"<<endl;
                goto jump;
            }
        }
    }
    cout<<endl<<"Entered equations: "<<endl;
    for(i = 0; i < len; i++)
        cout<<i+1<<"-> x = "<<a[i]<<" mod "<<m[i]<<endl;
    cout<<endl<<"On solving, x = "<<crt(a, m, len)<<endl;
}
