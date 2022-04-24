from typing import List


def full_names(first_names: List, last_names: List, min_length=0) -> List:
    """
    The function creates full names from lists of given names and checks that start with a capital letter.
    :param first_names: List of first names.
    :param last_names: List of surnames.
    :param min_length: Minimum length of full name.
    :return: A list of full names whose length is greater than the minimum length requested.
    """
    new_names = [f'{f_name.capitalize()} {l_name.capitalize()}'
                 for f_name in first_names
                 for l_name in last_names]
    return [full_name for full_name in new_names if len(full_name) >= min_length]


if __name__ == '__main__':
    my_first_names = ['avi', 'moshe', 'yaakov']
    my_last_names = ['cohen', 'levi', 'mizrahi']

    # התנאים הבאים צריכים להתקיים
    print(full_names(my_first_names, my_last_names, 10) == ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
                                                            'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
    print(full_names(my_first_names, my_last_names) == ['Avi Cohen', 'Avi Levi', 'Avi Mizrahi', 'Moshe Cohen',
                                                        'Moshe Levi', 'Moshe Mizrahi', 'Yaakov Cohen', 'Yaakov Levi',
                                                        'Yaakov Mizrahi'])
