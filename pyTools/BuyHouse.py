#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
#  计算买房相关

###################
# 贷款相关
###################

#
# 等额本金
#
def EquivalentPrincipal(amount, totalMonths, interestMonthRate, monthNow, principalHasPay, interestHasPay, interestTotal, principalPerMonth):
    # 计算当月还款额，当月还款本金，当月还款利息，剩余本金，剩余利息
    if totalMonths <= 0 or amount <= 0 or interestMonthRate < 0 or monthNow > totalMonths:
        return;

    # 总利息
    if interestTotal == None:
        interestTotal = (totalMonths + 1) * amount * interestMonthRate / 2;

    # 每月还款本金
    if principalPerMonth == None:
        principalPerMonth = amount / totalMonths;

    # 剩余本金
    principalLast = amount - principalHasPay;
    if principalLast <= 0:
        return;
    # 当月利息
    interestThisMonth = principalLast * interestMonthRate;
    # 当月还款总额
    totalPriceThisMonth = principalPerMonth + interestThisMonth;

    # 还款操作

    # 已还本金
    principalHasPay = principalHasPay + principalPerMonth;
    # 已还利息
    interestHasPay = interestHasPay + interestThisMonth;
    # 剩余本金
    principalLast = principalLast - principalPerMonth;
    # 剩余利息
    interestLast = interestTotal - interestHasPay;

    print("还款，第 ", monthNow, " 月，本月还款总额：", totalPriceThisMonth, "，本月本金：", principalPerMonth, "，本月利息：", interestThisMonth, "，已还本金：", principalHasPay, "，已还利息：", interestHasPay, "，剩余本金：", principalLast, "，剩余利息：", interestLast);

    EquivalentPrincipal(amount, totalMonths, interestMonthRate, monthNow + 1, principalHasPay, interestHasPay, interestTotal, principalPerMonth);

EquivalentPrincipal(520000, 360, 0.429 / 12, 1, 0, 0, None, None)