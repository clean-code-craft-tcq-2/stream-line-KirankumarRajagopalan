#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "SendBatteryParameters.h"

void print(float temperature, float SOC, float ChargeRate){
    printf(" Temperature : %.2f , State of Charge : %.2f , Charge Rate : %.2f \n",temperature,SOC,ChargeRate);
}

void ReadBMSParamsFromFile(float* Temperature, float* SOC, float* ChargeRate)
{
    float Temp_reading, SOC_reading,CR_reading;
    FILE* fp= fopen("./BatteryParameters.txt","r");  

    if (NULL == fp)
    {
        printf("file can't be opened \n");
    }
    else 
    {
        for(int i=0;fscanf(fp, "%f\t%f\t%f\n", &Temp_reading,&SOC_reading,&CR_reading)!=EOF ;i++)
        {
            *(Temperature+i) = Temp_reading;
            *(SOC+i)  = SOC_reading;
            *(ChargeRate+i)   = CR_reading;
        }
    }
    fclose(fp);  
}

void SendBMSParamsToConsole(float* Temperature, float* SOC, float* ChargeRate)
{
    float Temp_ToPrint, SOC_ToPrint, CR_ToPrint;
    for(int i = 0; i<NO_OF_READINGS;i++)
    {
        Temp_ToPrint = *(Temperature+i);
        SOC_ToPrint = *(SOC+i);
        CR_ToPrint = *(ChargeRate+i);
        print(Temp_ToPrint, SOC_ToPrint, CR_ToPrint);
    }
}

void BMS_ParametersSender()
{
  float Temperature[NO_OF_READINGS], SOC[NO_OF_READINGS], ChargeRate[NO_OF_READINGS] = {0};
  ReadBMSParamsFromFile( Temperature,SOC,ChargeRate);
  SendBMSParamsToConsole( Temperature,SOC,ChargeRate);
}
