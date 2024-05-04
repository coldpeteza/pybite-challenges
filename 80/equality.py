from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    ordered_list1 = sorted(list1)
    ordered_list2 = sorted(list2)
    deduped_list1 = set(list1)
    deduped_list2 = set(list2)

    result = Equality.NO_EQUALITY

    if list1 is list2:
        result = Equality.SAME_REFERENCE
    elif len(list1) == len(list2):
        counter = 0
        dupe_counter = 0

        for key, element in enumerate(list1):
            if element == list2[key]:
                counter += 1
            if element in list2:
                dupe_counter += 1

        if counter == len(list2):
            result = Equality.SAME_ORDERED
        elif not set(list1).symmetric_difference(set(list2)):
            if dupe_counter > counter:
                # check ordered
                if dupe_counter == len(deduped_list2) and counter != 0:
                    result = Equality.SAME_ORDERED
            else:
                result = Equality.SAME_UNORDERED
    elif not set(list1).symmetric_difference(set(list2)):
        result = Equality.SAME_UNORDERED_DEDUPED

    if len(list1) == len(list2) and list1[0] < list2[0] and not set(list1).symmetric_difference(set(list2)):
        result = Equality.SAME_UNORDERED

    return result
