import sys
from statistics import mean

def ReadDataFromSender():
    values_from_sender =[]
    incoming_values = sys.stdin.readlines()
    for value in incoming_values:
        print(value)
        value = value.strip('\n')[0]
        if (value == '===============================================================================') :
            continue
        SplittedValues = value.split(',')
        values_from_sender.append(FormatDataFromSender(SplittedValues))
    return values_from_sender

def FormatDataFromSender(oneReading):
    print(oneReading)
    temp = float((oneReading[0].split(":")[-1]).strip())
    SoC = float((oneReading[1].split(":")[-1]).strip())
    ChargeRate = float((oneReading[2].split(":")[-1]).strip())
    return [{'temp':temp, 'SoC':SoC, 'ChargeRate':ChargeRate}]

def FindRangeValues(temp, SoC, ChargeRate):
    min_temp = min(temp)
    max_temp = max(temp)
    min_SoC = min(SoC)
    max_SoC = max(SoC)
    min_ChargeRate = min(ChargeRate)
    max_ChargeRate = max(ChargeRate)
    return (min_temp, max_temp,  min_SoC, max_SoC, min_ChargeRate, max_ChargeRate)

def CalculateMovingAverages(values_from_sender):
    avg_temp = mean([one_reading['temp'] for one_reading in values_from_sender][-5:])
    avg_SoC = mean([one_reading['SoC'] for one_reading in values_from_sender][-5:])
    avg_ChargeRate = mean([one_reading['ChargeRate'] for one_reading in values_from_sender][-5:])
    return (avg_temp, avg_SoC, avg_ChargeRate)

def PrintMovingAveragesintoConsole(values_from_sender):
    (avg_temp, avg_SoC, avg_ChargeRate) = CalculateMovingAverages(values_from_sender)
    PrintStatisticsTOConsole("Average", "Temperature", avg_temp)
    PrintStatisticsTOConsole("Average", "State Of Charge", avg_SoC)
    PrintStatisticsTOConsole("Average", "Charge rate", avg_ChargeRate)
    return (avg_temp, avg_SoC, avg_ChargeRate)

def PrintRangesOfParamsIntoConsole(values_from_sender):
    temp = [one_reading['temp'] for one_reading in values_from_sender]
    SoC = [one_reading['SoC'] for one_reading in values_from_sender]
    ChargeRate = [one_reading['ChargeRate'] for one_reading in values_from_sender]
    (min_temp, max_temp,  min_SoC, max_SoC, min_ChargeRate, max_ChargeRate) = FindRangeValues(temp, SoC, ChargeRate)
    PrintStatisticsTOConsole("Minimum", "Temperature", min_temp)
    PrintStatisticsTOConsole("Maximum", "Temperature", max_temp)
    PrintStatisticsTOConsole("Minimum", "State Of Charge", min_SoC)
    PrintStatisticsTOConsole("Maximum", "State Of Charge", max_SoC)
    PrintStatisticsTOConsole("Minimum", "Charge rate", min_ChargeRate)
    PrintStatisticsTOConsole("Maximum", "Charge rate", max_ChargeRate)
    return (min_temp, max_temp, min_SoC, max_SoC, min_ChargeRate, max_ChargeRate)

def PrintStatisticsTOConsole(statistic, parameter, value):
    print(f"{statistic} value of {parameter} is {value}")
    return(f"{statistic} value of {parameter} is {value}")

def CalculateStaticticsOfSenderData():
    values_from_sender = ReadDataFromSender()
    (min_temp, max_temp, min_SoC, max_SoC, min_ChargeRate, max_ChargeRate) = PrintRangesOfParamsIntoConsole(values_from_sender)
    (avg_temp, avg_SoC, avg_ChargeRate) = PrintMovingAveragesintoConsole(values_from_sender)
    return [(min_temp, max_temp, min_SoC, max_SoC, min_ChargeRate, max_ChargeRate),(avg_temp, avg_SoC, avg_ChargeRate)]

if __name__ == "__main__":
    CalculateStaticticsOfSenderData()
