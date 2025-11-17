#include <iostream>
#include <math.h>
#include <cstring>

int k;
double sin(), cos();

using namespace std;

int main(){
 float A = 0, B = 0, i, j, z[1760];
 char b[1760];
 cout << "\n1b[2J";
 for(;;){
 	memset(b, 32, 1760);
 	memset(z, 0, 7040);
 	for(j = 0; j < 6.28; j += 0.004){
 		for(i = 0; i < 6.28; i += 0.03){
 			float c = sin(i), d = cos(j), e = sin(A), f = sin(j), g = cos(A),
 			      h = d + 2, D = 1 / (c * h * e + f * g + 5), l = cos(i),
 			      m = cos(B), n = sin(B), t = c * h * g - f * e;
 			int x = 40 + 30 * D * (l * h * m - t * n),
 			    y = 12 + 15 * D * (l * h * n + t * m), o = x + 80 * y,
 			    N = 8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n);
 	        if(y < 22 && y > 0 && x < 80 && x > 0 && D > z[o]) {
 	        	z[o] = D;
 	        	b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
 	        }
 		}
 	}
 	cout << "\1xb[H";
 	for(k = 0; k < 1761; k++)
 		putchar(k % 80 ? b[k] : 10);
    A += 0.04;
    B += 0.02;
 }
}
