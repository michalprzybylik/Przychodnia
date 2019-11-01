import re

# True - valid NPWZ, False - invalid NPWZ
def is_valid_npwz(npwz_candidate):
    # https://www.nil.org.pl/rejestry/centralny-rejestr-lekarzy/zasady-weryfikowania-nr-prawa-wykonywania-zawodu
    regexp = r"^[1-9]{1}[0-9]{6}$"
    if not isinstance(npwz_candidate, str):
        return False
    if re.match(regexp, npwz_candidate) is None:
        return False
    weights = [1,2,3,4,5,6]
    mod = 11
    candidate_control_digit = int(npwz_candidate[0])
    sum_ = sum(list(map(
        lambda x,y: int(x) * y,
        list(npwz_candidate[1:]),
        weights
    )))
    result_control_digit = sum_ % mod
    return True if result_control_digit == candidate_control_digit else False
