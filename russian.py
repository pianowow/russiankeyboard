#-------------------------------------------------------------------------------
# Name:        russian.py
# Purpose:     To translate English written without changing the input
#              language from Russian to English.
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     08/27/2012
#-------------------------------------------------------------------------------
#!/usr/bin/env python

english   = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?.,'"
russian   = [1060, 1048, 1057, 1042, 1059, 1040, 1055, 1056, 1064, 1054, #ABCDEFGHIJ
             1051, 1044, 1068, 1058, 1065, 1047, 1049, 1050, 1067, 1045, #KLMNOPQRST
             1043, 1052, 1062, 1063, 1053, 1071, 1092, 1080, 1089, 1074, #UVWXYZabcd
             1091, 1072, 1087, 1088, 1096, 1086, 1083, 1076, 1100, 1090, #efghijklmn
             1097, 1079, 1081, 1082, 1099, 1077, 1075, 1084, 1094, 1095, #opqrstuvwx
             1085, 1103,   46, 1102, 1073, 1101]                         #yz?.,'
russian2  = [212, 200, 209, 194, 211, 192, 207, 208, 216, 206, 203, 196, #ABCDEFGHIJKL
             220, 210, 217, 199, 201, 202, 219, 197, 195, 204, 214, 215, #MNOPQRSTUVWX
             205, 223, 244, 232, 241, 226, 243, 224, 239, 240, 248, 238, #YZabcdefghij
             235, 228, 252, 242, 249, 231, 233, 234, 251, 229, 227, 236, #klmnopqrstuv
             246, 247, 237, 255, 44, 225, 254, 1101] #1101 isn't right   #wxyz?.,'
ukrainian = [1060, 1048, 1057, 1042, 1059, 1040, 1055, 1056, 1064, 1054, #ABCDEFGHIJ
             1051, 1044, 1068, 1058, 1065, 1047, 1049, 1050,  178, 1045, #KLMNOPQRST
             1043, 1052, 1062, 1063, 1053, 1071, 1092, 1080, 1089, 1074, #UVWXYZabcd
             1091, 1072, 1087, 1088, 1096, 1086, 1083, 1076, 1100, 1090, #efghijklmn
             1097, 1079, 1081, 1082,  179, 1077, 1075, 1084, 1094, 1095, #opqrstuvwx
             1085, 1103,   44, 1102, 1073, 1101]                         #yz?.,'

s = 'Copy the Russian/Ukrainian text and press enter'
while s != '':
    if chr(178) in s or chr(179) in s:
        #ukrainian
        for i,r in enumerate(ukrainian):
            s = s.replace(chr(r),english[i])
    else:
        #russian
        for i,r in enumerate(russian):
            s = s.replace(chr(r),english[i])
            s = s.replace(chr(russian2[i]),english[i])
    print (s)
    s = input()