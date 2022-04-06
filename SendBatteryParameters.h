#define NO_OF_READINGS 50

void print(float temperature, float SOC, float CR);
void ReadBMSParamsFromFile(float* Temperature, float* SOC, float* ChargeRate);
void SendBMSParamsToConsole(float* Temperature, float* SOC, float* ChargeRate);
void SendBatteryParameters();
