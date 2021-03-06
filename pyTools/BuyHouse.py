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
    print("\n----------------------------------------------------------------------------------------------\n")
    print ("-------, 还款，第 %d 月，本月还款总额：%.2f，本月本金：%.2f，本月利息：%.2f" %(monthNow, totalPriceThisMonth, principalPerMonth, interestThisMonth));

    # 已还本金
    principalHasPay = principalHasPay + principalPerMonth;
    # 已还利息
    interestHasPay = interestHasPay + interestThisMonth;
    # 剩余本金
    principalLast = principalLast - principalPerMonth;
    # 剩余利息
    interestLast = interestTotal - interestHasPay;

    print("$$$$$$$, 已还本金：%.2f，已还利息：%.2f，剩余本金：%.2f，剩余利息：%.2f" %(principalHasPay, interestHasPay, principalLast, interestLast));

    # 递归调用
    EquivalentPrincipal(amount, totalMonths, interestMonthRate, monthNow + 1, principalHasPay, interestHasPay, interestTotal, principalPerMonth);
    
# 
# 等额本息
#
def EquivalentInterest(amount, totalMonths, interestMonthRate, monthNow, principalHasPay, interestHasPay, repaymentPerMonth, interestLast):
    # 计算当月还款额，当月还款本金，当月还款利息，剩余本金，剩余利息
    if totalMonths <= 0 or amount <= 0 or interestMonthRate < 0 or 0 > totalMonths:
        return;

    # 月还款额
    if repaymentPerMonth == None:
        repaymentPerMonth = (amount * interestMonthRate * ((1 + interestMonthRate)**totalMonths)) / ((1 + interestMonthRate)**totalMonths - 1);
        # 剩余利息
        interestLast = repaymentPerMonth * totalMonths - amount;
    
    # 剩余本金
    amountOld = amount;
    amount = amount * (1 + interestMonthRate) - repaymentPerMonth;

    # 当月还款本金
    principalThisMonth = amountOld - amount;
    # 当月还款利息
    interestThisMonth = repaymentPerMonth - principalThisMonth;

    # 还款操作
    print("\n----------------------------------------------------------------------------------------------\n")
    print ("-------, 还款，第 %d 月，本月还款总额：%.2f，本月本金：%.2f，本月利息：%.2f" %(monthNow, repaymentPerMonth, principalThisMonth, interestThisMonth));

    # 剩余利息
    interestLast = interestLast - interestThisMonth;
    # 已还本金
    principalHasPay = principalHasPay + principalThisMonth;
    # 已还利息
    interestHasPay = interestHasPay + interestThisMonth;

    print("$$$$$$$, 已还本金：%.2f，已还利息：%.2f，剩余本金：%.2f，剩余利息：%.2f" %(principalHasPay, interestHasPay, amount, interestLast));

    # 递归调用
    EquivalentInterest(amount, totalMonths - 1, interestMonthRate, monthNow + 1, principalHasPay, interestHasPay, repaymentPerMonth, interestLast)


print("\n-------------------------         等额本金还款         ---------------------------------\n")
EquivalentPrincipal(520000, 360, 0.04312 / 12, 1, 0, 0, None, None)
print("\n----------------------------------------------------------------------------------------------\n")


print("\n-------------------------         等额本息还款         ---------------------------------\n")
EquivalentInterest(520000, 360, 0.04312 / 12, 1, 0, 0, None, None)
print("\n----------------------------------------------------------------------------------------------\n")