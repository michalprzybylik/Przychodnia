import re


# True - valid NPWZ, False - invalid NPWZ
def is_valid_npwz(npwz_candidate):
    # https://www.nil.org.pl/rejestry/centralny-rejestr-lekarzy/zasady-weryfikowania-nr-prawa-wykonywania-zawodu
    regexp = r"^[1-9]{1}[0-9]{6}$"
    if not isinstance(npwz_candidate, str):
        return False
    if re.match(regexp, npwz_candidate) is None:
        return False
    weights = [1, 2, 3, 4, 5, 6]
    mod = 11
    candidate_control_digit = int(npwz_candidate[0])
    sum_ = sum(list(map(
        lambda x, y: int(x) * y,
        list(npwz_candidate[1:]),
        weights
    )))
    result_control_digit = sum_ % mod
    return True if result_control_digit == candidate_control_digit else False


# Return birth date in format yyyy-mm-dd form CORRECT PESEL number
def get_birth_date_from_pesel(pesel):
    date = pesel[0:6]
    if date[2] in "89":
        month = int(date[2:4]) - 80
        date = "18" + date
    elif date[2] in "23":
        month = int(date[2:4]) - 20
        date = "20" + date
    elif date[2] in "45":
        month = int(date[2:4]) - 40
        date = "21" + date
    elif date[2] in "67":
        month = int(date[2:4]) - 60
        date = "22" + date
    else:
        month = int(date[2:4])
        date = "19" + date
    date = date[0:4] + "-" + str(month // 10) + \
        str(month % 10) + "-" + date[6:8]
    return date


# True - correct date, False - incorrect date. Date format yyyy-mm-dd
def is_valid_date(date):
    if not re.match("^[0-9]{4}-[01][0-9]-[0-3][0-9]$", date):
        return False
    daysofmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        daysofmonths[1] = 29
    return (1 <= month <= 12 and 1 <= day <= daysofmonths[month - 1])


# True - corrent PESEL, False - incorrenct PESEL.
def is_valid_pesel(pesel):
    if not re.match("^[0-9]{11}$", pesel):
        return False
    if not is_valid_date(get_birth_date_from_pesel(pesel)):
        return False
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    sum = 0
    for i in range(0, 11):
        sum = sum + int(pesel[i]) * weights[i]
    return sum % 10 == 0
