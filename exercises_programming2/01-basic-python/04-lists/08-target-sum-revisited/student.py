def target_sum(ns, target):
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            if ns[i] + ns[j] == target:
                return True
    return False

# alle combinaties van een element in de lijst en een element die er na komt
