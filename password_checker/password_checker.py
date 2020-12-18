import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    print(res)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try')

    return res


def read_res(res):
    print(res.text)


def get_passwords_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1p = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1p[:5], sha1p[5:]
    res = request_api_data(first5_char)
    return get_passwords_leaks_count(res, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was fiund {count} times... change password')
        else:
            print(f'{password} was not found')


if __name__ == '__main__':
    sys.exit(main(['cthutq19962020']))
