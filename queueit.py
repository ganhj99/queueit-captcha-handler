from requests import post
from base64 import b64decode


def load_captcha():
    url = "https://footlocker.queue-it.net/challengeapi/queueitcaptcha/challenge/en-us"
    headers = {
        "Host": "footlocker.queue-it.net",
        "sec-ch-ua": '"Chromium";v="129", "Not(A:Brand";v="24", "Google Chrome";v="129"',
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "accept": "*/*",
        "origin": "https://footlocker.queue-it.net",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://footlocker.queue-it.net/",
        "accept-language": "en-US,en;q=0.9,ko;q=0.8,ms;q=0.7",
        "x-queueit-challange-customerid": "footlocker",
        "x-queueit-challange-eventid": "cxcdtest02",
        "x-queueit-challange-hash": "sg7R/eOE9jBw1RMb1iI7d1M8uKgf6sErktuA3Q69hgw=",
        "x-queueit-challange-reason": "1",
    }
    return post(url, headers=headers).json()["imageBase64"]


if __name__ == "__main__":
    b64image = load_captcha()
    result = post(
        "https://ocr.ganhj.dev/queueit",
        json={"image_data": b64image},
    ).json()
    if error := result.get("error"):
        print(error)
        exit(0)
    print(f"Solved! {result.get('answer')}")

    # Save image for debugging
    with open("queueit.png", "wb") as fh:
        fh.write(b64decode(b64image))
