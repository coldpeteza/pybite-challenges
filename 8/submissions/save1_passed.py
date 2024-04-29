def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    pre_text = string[:n]
    post_text = string[n:]
    result = f"{post_text}{pre_text}"
    if n < 0:
        pre_text = string[n:]
        post_text = string[:n]
        result = f"{pre_text}{post_text}"

    return result