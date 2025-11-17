#include <iostream>
#include <unistd.h>
#include <math.h>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;

float A, B, C;
float cubeWidth = 18;
int width = 160, height = 44;
float zBUffer[160 * 44];
char buffer[160 * 44];
int backgroundASCIICode = ' ';
int distanceFromCam = 100;
float incrementSpeed = 0.6;
float x, y, z, ooz, K1 = 40;
int xp, yp, idx;

float CalcX(int i, int j, int k){
	return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) + j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C);
}

float CalcY(int i, int j, int k){
	return j * cos(A) * cos(C) + k * sin(A) * cos(C) - j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) - i * cos(B) * sin(C);
}

float CalcZ(int i, int j, int k){
	return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B);
}

void CalcSurf(float cubeX, float cubeY, float cubeZ, int ch){
	x = CalcX(cubeX, cubeY, cubeZ);
	y = CalcY(cubeX, cubeY, cubeZ);
	z = CalcZ(cubeX, cubeY, cubeZ) + distanceFromCam;

	ooz = 1/z;
	xp = (int)(width/2 - 2 * cubeWidth + K1 * ooz * x * 2);
	yp = (int)(height/2 + K1 * ooz * y);
	idx = xp + yp * width;
	if(idx >= 0 && idx < width * height){
		if(ooz > zBUffer[idx]){
			zBUffer[idx] = ooz;
			buffer[idx] = ch;
		}
	}
}

int main(){
    cout << "\x1b[2J";
    while(1){
		memset(buffer, backgroundASCIICode, width * height);
		memset(zBUffer, 0, width * height * 4);
		for(float cubeX = -cubeWidth; cubeX < cubeWidth; cubeX += incrementSpeed){
			for(float cubeY = -cubeWidth; cubeY < cubeWidth; cubeY += incrementSpeed){
				CalcSurf(cubeX, cubeY, -cubeWidth, '.');
				CalcSurf(cubeWidth, cubeY, cubeX, '$');
				CalcSurf(-cubeWidth, cubeY, -cubeX, '~');
				CalcSurf(-cubeX, cubeY, cubeWidth, '#');
				CalcSurf(cubeX, -cubeWidth, -cubeY, ';');
				CalcSurf(cubeX, cubeWidth, cubeY, '+');
			}
		}
		cout << "\x1b[H";
		for(int k = 0; k < width * height; k++){
			putchar(k % width ? buffer[k] : 10);
		}
	    A += 0.005;
	    B += 0.005;
	    usleep(1000);
    } 
	return 0;
}
