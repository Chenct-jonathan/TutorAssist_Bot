#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for class_arrangement

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_class_arrangement = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"連假":["連假"],"進班":["進班"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_class_arrangement:
        print("[class_arrangement] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[15].[你][方便]嗎":
        # write your code here
        pass

    if utterance == "[15].[你]ok 嗎":
        # write your code here
        pass

    if utterance == "[15].[老師]ok嗎":
        # write your code here
        pass

    if utterance == "[15].好嗎":
        # write your code here
        pass

    if utterance == "[七點]好嗎":
        # write your code here
        pass

    if utterance == "[三點][你]ok嗎":
        # write your code here
        pass

    if utterance == "[三點][老師]ok嗎":
        # write your code here
        pass

    if utterance == "[五點][你][可以]嗎":
        # write your code here
        pass

    if utterance == "[五點][你][方便]嗎":
        # write your code here
        pass

    if utterance == "[五點][老師][可以]嗎":
        # write your code here
        pass

    if utterance == "[五點][老師][方便]嗎":
        # write your code here
        pass

    if utterance == "[可以]改上課時間嗎":
        # write your code here
        pass

    if utterance == "[可以]改時間嗎":
        # write your code here
        pass

    if utterance == "[提早][半][小時]":
        # write your code here
        pass

    if utterance == "[禮拜天][可以]幫[XX]上課嗎":
        # write your code here
        pass

    if utterance == "延[後][半][小時]":
        # write your code here
        pass

    if utterance == "延[後]到[8].":
        # write your code here
        pass

    if utterance == "延[後]到[八點]":
        # write your code here
        pass

    if utterance == "提早到[8].":
        # write your code here
        pass

    if utterance == "提早到[八點]":
        # write your code here
        pass

    if utterance == "改[8].":
        # write your code here
        pass

    if utterance == "改[八點]":
        # write your code here
        pass

    if utterance == "改到[8].":
        # write your code here
        pass

    if utterance == "改到[八點]":
        # write your code here
        pass

    if utterance == "需要調整時間嗎":
        # write your code here
        pass

    return resultDICT