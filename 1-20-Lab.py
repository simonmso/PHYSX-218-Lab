import error_rules as er

def dif(nums):
    return nums[1] - nums[0]


al_T = [24.89, 85.89]  # degrees C
unc_T = .3  # degrees C
al_dT = dif(al_T)

al_L = 0.706  # m
unc_L = 0.001  # m
al_dL = 0.00117  # m

al_a = al_dL / (al_L * al_dT)
al_unc_a = er.rule_4(al_a, [al_L, al_dL, al_dT], [unc_L, 0.00001, unc_T], [1, 1, 1])


print("Aluminum a: {:.5} +/- {:.5}".format(al_a, al_unc_a))

cu_T = [25.55, 88.35]  # degrees C
cu_dT = dif(cu_T)

cu_L = 0.703  # m
cu_dL = 0.00082  # m

cu_a = cu_dL / (cu_L * cu_dT)
cu_unc_a = er.rule_4(cu_a,
                     [cu_L, cu_dL, cu_dT],
                     [unc_L, 0.00001, unc_T],
                     [1, 1, 1])

print("Copper a: {:.5} +/- {:.5}".format(cu_a, cu_unc_a))
