

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

def gcp(str1, str2):
    if len(str1) < len(str2):
        shorter = str1
        longer = str2
    else:
        shorter = str2
        longer = str1

    len_lon = len(longer)
    len_shr = len(shorter)
    shorter_orig = shorter
    len_shr_orig = len(shorter_orig)

    for idx in range(len_shr, 0, -1):
        shorter = shorter[:idx]
        len_shr = len(shorter)
        # check if prefix fits the exact number of times into larger string
        if len_lon % len_shr == 0 and len_shr_orig % len_shr == 0:
            n = len_lon // len_shr
            n_shr = len_shr_orig // len_shr
            if longer == shorter * n and shorter_orig == shorter * n_shr:
                return shorter
    return ''


print(gcp(str1, str2))
str2