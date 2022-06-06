#define CATCH_CONFIG_MAIN // This tells Catch to provide a main() - only do this in one cpp file

#include "test/catch.hpp"
#include "SendBatteryParameters.h"

TEST_CASE("Tests to check if data is correctly read from file") {
  float Temperature[NO_OF_READINGS] = {0};
  float StateOfCharge[NO_OF_READINGS] = {0};
  float ChargeRate[NO_OF_READINGS] = {0};
  ReadBMSParamsFromFile( Temperature,StateOfCharge,ChargeRate);
  
  float expectedoutput[3][3] = {{20,23,0.5}, {25,34,0.7},{45,67,0.05}};
  for(int i=0;i<3;i++)
  {
    REQUIRE(Temperature[i] == expectedoutput[i][0]);
    REQUIRE(StateOfCharge[i] == expectedoutput[i][1]);
    REQUIRE(ChargeRate[i] == expectedoutput[i][2]);
  }
}
