def create_list(x):
    """ function to create a list """

    return x.split('.')


def make_comparison(ad_equip, display_equip):
    """ function that checks if one item of a list is in another,
        if it is return True """

    lower_case_ad_equip = [x.lower() for x in ad_equip]
    lower_case_display_equip = [y.lower() for y in display_equip]

    for tool in lower_case_ad_equip:
        if tool in lower_case_display_equip:
            return True
