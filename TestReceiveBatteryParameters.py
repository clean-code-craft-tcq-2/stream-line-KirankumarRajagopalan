import unittest
import ReceivebatteryParameters as StreamLine_receiver

Formatted_sample_Value_from_sender = [
            {"temp": 20, "SoC": 23, "ChargeRate": 0.5},
            {"temp": 25, "SoC": 34, "ChargeRate": 0.7},
            {"temp": 45, "SoC": 67, "ChargeRate": 0.05},
            {"temp": 34, "SoC": 12, "ChargeRate": 0.1},
            {"temp": 15, "SoC": 10, "ChargeRate": 0.2},
            {"temp": 27, "SoC": 25, "ChargeRate": 0.33}
        ]
class TypewiseTest(unittest.TestCase):
    
    def test_PrintStatisticsTOConsole(self):
        self.assertTrue(StreamLine_receiver.PrintStatisticsTOConsole("Minimum", "Temperature", 15) == "Minimum value of Temperature is 15")
        self.assertTrue(StreamLine_receiver.PrintStatisticsTOConsole("Maximum", "State Of Charge", 67) == "Maximum value of State Of Charge is 67")
        self.assertTrue(StreamLine_receiver.PrintStatisticsTOConsole("Average", "Charge rate", 0.276) == "Average value of Charge rate is 0.276")
    
    def test_PrintMovingAveragesintoConsole(self):
        self.assertTrue(StreamLine_receiver.PrintMovingAveragesintoConsole(Formatted_sample_Value_from_sender)==(29.2, 29.6, 0.276))

    def test_PrintRangesOfParamsIntoConsole(self):
        self.assertTrue(StreamLine_receiver.PrintRangesOfParamsIntoConsole(Formatted_sample_Value_from_sender)==(15,45,10,67,0.05,0.7))

    def test_FormatDataFromSender(self):
        self.assertTrue(StreamLine_receiver.FormatDataFromSender([" Temperature : 20 ", "State of Charge : 23" , "Charge Rate :0.5\n"])==[{'temp': 20.0, 'SoC': 23.0, 'ChargeRate': 0.5}])

    def test_CalculateMovingAverages(self):
        self.assertTrue(StreamLine_receiver.CalculateMovingAverages(Formatted_sample_Value_from_sender)==(29.2, 29.6, 0.276))
    
    def test_FindRangeValues(self):
        self.assertTrue(StreamLine_receiver.FindRangeValues([one_reading['temp'] for one_reading in Formatted_sample_Value_from_sender], [one_reading['SoC'] for one_reading in Formatted_sample_Value_from_sender], [one_reading['ChargeRate'] for one_reading in Formatted_sample_Value_from_sender])==(15,45,10,67,0.05,0.7))

unittest.main(),
