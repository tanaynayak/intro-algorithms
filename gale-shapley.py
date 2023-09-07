def preference(woman_pref_list, woman, current_partner, new_partner):
    for pref in woman_pref_list[woman]:
        if pref == new_partner:
            return True
        if pref == current_partner:
            return False
    return False

def gale_shapley(men_pref_list, women_pref_list):
    n = len(men_pref_list)
    woman_partner = [-1] * n
    free_men = [False] * n
    free_men_queue = list(range(n))

    while free_men_queue:
        man = free_men_queue.pop(0)
        for woman in men_pref_list[man]:
            if woman_partner[woman] == -1:
                woman_partner[woman] = man
                free_men[man] = True
                break
            else:
                current_partner = woman_partner[woman]
                if preference(women_pref_list, woman, current_partner, man):
                    free_men[current_partner] = False
                    free_men_queue.append(current_partner)
                    woman_partner[woman] = man
                    free_men[man] = True
                    break

    return [(woman, man) for woman, man in enumerate(woman_partner)]

def main():
    men_pref_list = [
        [1, 0, 2],
        [0, 2, 1],
        [2, 1, 0]
    ]

    women_pref_list = [
        [0, 1, 2],
        [1, 2, 0],
        [2, 0, 1]
    ]

    pairs = gale_shapley(men_pref_list, women_pref_list)
    for woman, man in pairs:
        print(f"Woman {woman} is paired with Man {man}")

if __name__ == "__main__":
    main()
