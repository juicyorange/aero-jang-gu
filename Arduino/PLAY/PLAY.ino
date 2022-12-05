#include <Wire.h>

// I2C address of the MPU-6050
const int MPU=0x68;
// Variables that will store sensor data
float AcX, AcY, AcZ;
float GyX, GyY, GyZ;

float maxVal = 32768;
float minVal = -32768;

void setup(){

  Serial.begin(115200);
  Wire.begin();                      // Initialize comunication
  Wire.beginTransmission(MPU);       // Start communication with MPU6050 // MPU=0x68
  Wire.write(0x6B);                  // Talk to the register 6B
  Wire.write(0x00);                  // Make reset - place a 0 into the 6B register
  Wire.endTransmission(true);        //end the transmission
}
void loop(){
  // Start the transmission with the MPU-6050 sensor
  Wire.beginTransmission(MPU);
  Wire.write(0x3B); // Start with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 6, true); // Read 6 registers total, each axis value is stored in 2 registers

  AcX=(Wire.read()<<8|Wire.read());  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=(Wire.read()<<8|Wire.read());  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=(Wire.read()<<8|Wire.read());  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  
  Wire.beginTransmission(MPU);
  Wire.write(0x43); // Gyro data first register address 0x43
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 6, true); // Read 4 registers total, each axis value is stored in 2 registers

  GyX=(Wire.read()<<8|Wire.read());  // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  GyY=(Wire.read()<<8|Wire.read());  // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  GyZ=(Wire.read()<<8|Wire.read());  // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

  Serial.println(String(constrain(AcX, minVal, maxVal)) + " " + String(constrain(AcY, minVal, maxVal)) + " " + String(constrain(AcZ, minVal, maxVal)) + " " + String(constrain(GyX, minVal, maxVal)) + " " + String(constrain(GyY, minVal, maxVal)) + " " + String(constrain(GyZ, minVal, maxVal)));
}
