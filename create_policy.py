import json
import uuid

VALUES = {
  0: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/VFD_CNTRL_TAGS/D1001VFDStop",
  1: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/VFD_CNTRL_TAGS/D1001VFDStopSpeedSetpoint",
  2: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/PE_Lube_Tags/D2001PELubePumpMtr1Stop",
  3: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Outputs/D1001DriveRunCommandDO",
  4: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Outputs/D1001DriveSpeedReferenceAO_ENG",
  5: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Outputs/D1002ChargePumpDriveSpeedReferenceAO_ENG",
  6: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Outputs/D2001PELubePumpDriveSpeedReferenceAO_ENG",
  7: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Outputs/D1002ChargePumpVFDRunCommandDO",
  8: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Outputs/D2001PELubePumpVFDRunCommandDO",
  9: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/CV1001PositionFeedbackAI_ENG",
  10: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/CV1002PositionFeedbackAI_ENG",
  11: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D1001MotorSpeedAI_ENG",
  12: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D1001MotorTorqueAI_ENG",
  13: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D1002ChargePumpSpeedAI_ENG",
  14: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D1002ChargePumpTorqueAI_ENG",
  15: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D2001PELubePumpDriveSpeedAI_ENG",
  16: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/FT1001MainLoopFlowrateAI_ENG",
  17: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/FT2001PELubeSupplyFlowAI_ENG",
  18: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/FT2001PELubeSupplyFlowSetpoint_ENG",
  19: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/LT1001MainWaterTankLevelAI_ENG",
  20: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT1001MaingPumpChargePressAI_ENG",
  21: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT1002MainPumpDischargePressAI_ENG",
  22: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT1003MainPumpDischargePressAI_ENG",
  23: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT1004ChokeCV1002PressAI_ENG",
  24: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2001PELubeSupplyPressAI_ENG",
  25: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2001PELubeSupplyPressSetpoint_ENG",
  26: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2002PELubeSupplyPressAI_ENG",
  27: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2002PELubeSupplyPressSetpoint_ENG",
  28: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1001PumpTempSensorAI_ENG",
  29: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1002PumpTempSensorAI_ENG",
  30: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1003PumpTempSensorAI_ENG",
  31: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1004PumpTempSensorAI_ENG",
  32: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1005PumpTempSensorAI_ENG",
  33: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1006PumpTempSensorAI_ENG",
  34: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1007PumpTempSensorAI_ENG",
  35: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1008PumpTempSensorAI_ENG",
  36: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1009PumpTempSensorAI_ENG",
  37: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1010PumpTempSensorAI_ENG",
  38: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1011PumpTempSensorAI_ENG",
  39: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TC1012PumpTempSensorAI_ENG",
  40: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TT1001MainWaterTemperatureAI_ENG",
  41: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TT2001PELubeTankTempAI_ENG",
  42: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/TT2002PELubeSupplyTempAI_ENG",
  43: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/CHOKE_TAGS/CV1002ChokeValvePositionSetpoint",
  44: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/CHOKE_TAGS/CV1002ChokeValveStop",
  45: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/CHOKE_TAGS/CV1001ChokeValveStop",
  46: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/CHOKE_TAGS/CV1001ChokeValvePositionSetpoint",
  47: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/CHARGE_PUMP_TAGS/D1002ChargePumpMotorStop",
  48: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/FT2001LL_AlarmSetpoint",
  49: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1001H_AlarmSetpoint",
  50: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1002H_AlarmSetpoint",
  51: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1003H_AlarmSetpoint",
  52: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1004HH_AlarmSetpoint",
  53: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS2001L_AlarmSetpoint",
  54: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LT1001L_AlarmSetpoint",
  55: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LT1001LL_AlarmSetpoint",
  56: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1001L_AlarmSetpoint",
  57: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1001LL_AlarmSetpoint",
  58: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1002HH_AlarmSetpoint",
  59: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1003HH_AlarmSetpoint",
  60: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT2001HH_AlarmSetpoint",
  61: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT2002L_AlarmSetpoint",
  62: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT2002LL_AlarmSetpoint",
  63: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT1001H_AlarmSetpoint",
  64: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT1001HH_AlarmSetpoint",
  65: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT2001H_AlarmSetpoint",
  66: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT2001HH_AlarmSetpoint",
  67: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/FT2001LL_Alarm",
  68: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1001H_Alarm",
  69: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1002H_Alarm",
  70: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1003H_Alarm",
  71: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS1004HH_Alarm",
  72: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LS2001L_Alarm",
  73: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LT1001L_Alarm",
  74: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/LT1001LL_Alarm",
  75: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1001L_Alarm",
  76: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1001LL_Alarm",
  77: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1002HH_Alarm",
  78: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT1003HH_Alarm",
  79: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT2001HH_Alarm",
  80: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT2002L_Alarm",
  81: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/PT2002LL_Alarm",
  82: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT1001H_Alarm",
  83: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT1001HH_Alarm",
  84: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT2001H_Alarm",
  85: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/ALARM_TAGS/TT2001HH_Alarm",
  86: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Outputs/D2002PELubePumpVFDRunCommandDO",
  87: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D2002PELubePumpDriveSpeedAI_ENG",
  88: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2006PELubeSupplyPressSetpointAI_ENG",
  89: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2006PELubeSupplyPressAI_ENG",
  90: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2005PELubeSupplyPressAI_ENG",
  91: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2005PELubeSupplyPressSetpointAI_ENG",
  92: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2004PELubeSupplyPressAI_ENG",
  93: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/PT2003PELubeSupplyPressAI_ENG",
  94: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/FT2002PELubeSupplyFlowAI_ENG",
  95: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/PE_Lube_Tags/D2003PELubeCoolerManualSpeedValue",
  96: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/PE_Lube_Tags/D2002PELubePumpMtr2ManualSpeedValue",
  97: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D1001MotorEff",
  98: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D2001PELubePumpDriveEff",
  99: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/D2002PELubePumpDriveEff",
  100: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/FT2001PELubeDriveCalculatedFlowrate_ENG",
  101: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/FT1001MainLoopCalculatedFlowrateAI_ENG",
  102: "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/Inputs/FT2002PELubeDriveCalculatedFlowrate_ENG"
}

def current_policy(table_format=1):
    """
    We would need this type of policy if / we need to specify a full path
    :sample policies:
    -- this is what we currently have --
    {
        "tag": {
            "path": "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/VFD_CNTRL_TAGS/D1001VFDStop",
            "index": 0,
            "table": "t0"
        }
    }
    --      End     --
    {
        "tag": {
            "path": "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]/DeviceSet/WAGO 750-8210 PFC200 G2 4ETH XTR/Resources/Application/GlobalVars/VFD_CNTRL_TAGS/D1001VFDStop",
            "index": 0,
            "table": "D1001VFDStop"
        }
    }
    """
    tags = []
    for index in VALUES:
        if table_format == 1:
            tags.append({
                "tag": {
                    "path":  VALUES[index],
                    "index": index,
                    "table": f"t{index}"
                }
            })
        else:
            tags.append({
                "tag": {
                    "path": VALUES[index],
                    "index": index,
                    "table": VALUES[index].rsplit("/", 1)[-1]
                }
            })

    return tags


def single_policy():
    """
    breakdown the path into human-readable parts and store in policy.
    we could potentially integrate table name into such policy if needed
    :sample-policy:
    {
        "tag": {
            "server-name": "LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]",
            "device-container": "DeviceSet",
            "device": "WAGO 750-8210 PFC200 G2 4ETH XTR",
            "resource": "Resources",
            "application": "Application",
            "variables-section": "GlobalVars",
            "feeder": "VFD_CNTRL_TAGS",
            "value": "D1001VFDStop" <-- this would also be the table name
        }
    }
    :return:
    """
    tags = []
    for index in VALUES:
        path_parts = VALUES[index].split("/")
        tags.append({
            "tag": {
                "server-name": path_parts[0],
                "device-container": path_parts[1],
                "device": path_parts[2],
                "resource": path_parts[3],
                "application": path_parts[4],
                "variables-section": path_parts[5],
                "feeder": path_parts[6],
                "value": path_parts[7]
            }
        })
    return tags





import uuid

class OPCUATreeParser:
    def __init__(self, values_dict):
        self.values_dict = values_dict
        self.nodes = []
        self.path_to_id = {}  # Maps full path to UUID

    def get_node_type(self, depth, name):
        mapping = {
            0: "server-name",
            1: "device-container",
            2: "device",
            3: "resource",
            4: "application",
            5: "variables",
            6: "feeder",
        }
        return mapping.get(depth, "tag")

    def build_tree(self):
        """
        {'server-name': {'name': 'LSPP_TEST_OPC_UA::[LSPP_Test_OPC_Server]', 'id': '479eb6d3b5274febb937a9a46d4e618a'}}
            {'device-container': {'name': 'DeviceSet', 'id': '52c71aeff3514710b4ee53413b36c7ff' 'parent': '479eb6d3b5274febb937a9a46d4e618a'}}
                {'device': {'name': 'WAGO 750-8210 PFC200 G2 4ETH XTR', 'id': 'b74970221f8544cfa5a031d23be95756', 'parent': '52c71aeff3514710b4ee53413b36c7ff'}}
                    {'resource': {'name': 'Resources', 'id': '010f915623204db58d423a29f5aea703', 'parent': 'b74970221f8544cfa5a031d23be95756'}}
                        {'application': {'name': 'Application', 'id': '85955df7099f49c68445a98e8dbb182a', 'parent': '010f915623204db58d423a29f5aea703'}}
                            {'variables': {'name': 'GlobalVars', 'id': '95fca717ea034819a79e92f5b3a33e77', 'parent': '85955df7099f49c68445a98e8dbb182a'}}
                                 {'feeder': {'name': 'VFD_CNTRL_TAGS', 'id': '3c03613b4d284575b3b2be43d0ad3704', 'parent': '95fca717ea034819a79e92f5b3a33e77'}},
                                    {'tag': {'name': 'D1001VFDStop', 'id': '208030ffba814f65b19069ce3fe6711e', 'parent': '3c03613b4d284575b3b2be43d0ad3704'}}
                                    ...
                                {'feeder': {'name': 'PE_Lube_Tags', 'id': 'abc701c714aa47d5856bcf9829430c82', 'parent': '95fca717ea034819a79e92f5b3a33e77'}},
                                    {'tag': {'name': 'D2001PELubePumpMtr1Stop', 'id': '754762cc97184465bb3305ddcae6fb8a', 'parent': 'abc701c714aa47d5856bcf9829430c82'}}
                                    ...
        """
        for full_path in self.values_dict.values():
            parts = full_path.split("/")
            current_path = ""
            parent_uuid = None

            for depth, part in enumerate(parts):
                current_path = current_path + "/" + part if current_path else part

                if current_path in self.path_to_id:
                    parent_uuid = self.path_to_id[current_path]
                    continue

                node_type = self.get_node_type(depth, part)
                node_uuid = str(uuid.uuid4()).replace('-', '')
                node = {
                    node_type: {
                        "name": part,
                        "id": node_uuid
                    }
                }
                if parent_uuid is not None:
                    node[node_type]["parent"] = parent_uuid

                self.nodes.append(node)
                self.path_to_id[current_path] = node_uuid
                parent_uuid = node_uuid

        return self.nodes





# format1 = current_policy(table_format=1)
# format2 = current_policy(table_format=2)
# tag_policy = single_policy()
#
# print(json.dumps(format1[0], indent=2))
# print(json.dumps(format2[0], indent=2))
# print(json.dumps(tag_policy[0], indent=2))

parser = OPCUATreeParser(VALUES)
result = parser.build_tree()

from pprint import pprint

pprint(result, sort_dicts=False)
