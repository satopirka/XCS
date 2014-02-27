#!/usr/local/bin python
# -*- coding:utf-8 -*-

class XCSConfig:
    k = 2
    N = 800
    max_iterations = 20000
    max_experiments = 10

    alpha = 0.1
    beta = 0.2
    gamma = 0.71
    delta = 0.1
    myu = 0.04
    nyu = 5
    chi = 0.8

    epsilon_0 = 10

    theta_ga = 25
    theta_del = 20
    theta_sub = 20
    theta_mna = 2

    p_sharp = 0.33
    p_explr = 1.0

    doGASubsumption = True
    doActionSetSubsumtion = True

XCSConfig = XCSConfig()
conf = XCSConfig #To access one of the above constant values from another module, import XCS_Constants * and use "cons.Xconstant"