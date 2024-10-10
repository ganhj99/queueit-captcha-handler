# Image Based Captchas / Queue-it Captchas (BotDetect) Handler API
Some captchas are based on text displayed in a tricky way inside an image. We have a well trained Machine Learning model ready to solve all of them with more than 98% success rate. Here's some examples

## Table of Contents
- [Sponsor](#sponsor)
- [The API (Free to Use)](#the-api-free-to-use)
  - [Implementation (Queue-it)](#implementation-queue-it)
- [Queue IT Captcha (BotDetect)](#queue-it-captcha-botdetect)
- [Having issue with your captcha?](#having-issue-with-your-captcha)

## Sponsor
[<img width="960" alt="CapSolver Ads" src="https://github.com/user-attachments/assets/f321b383-6931-4def-802a-68161cfaec1d">](https://www.capsolver.com/?utm_source=github&utm_medium=repo&utm_campaign=scraping&utm_term=queueit-captcha-handler)

## The API (Free to Use)
We have two endpoints that works for images OCR. By passing an image as base64 string, it will return a JSON containing the extracted text

### API Base URL

**[https://ocr.ganhj.dev](https://ocr.ganhj.dev)**

### Endpoints

**POST ```/ocr```**

Works for all universal images OCR with a success rate of > 75% tested on ~20,000 samples.

**POST ```/queueit```**

Specially crafted for Queue-it image captcha (BotDetect) with a success rate of > 98% tested on ~20,000 samples.

### Implementation (Queue-it)


**Example Request (CURL)**
```bash
curl --request POST \
  --url 'https://ocr.ganhj.dev/queueit' \
  --header 'Content-Type: application/json' \
  --data '{
	"image_data": "/9j/4AAQSkZJRgABAQAA..."
}'
```

**Example Response**
```json
{
    "answer": "1Z42ET"
}
```

## Queue IT Captcha (BotDetect)
Queue IT offers to their clients to use their own Captcha solution, known as **BotDetect** as well.
It is an image based captcha, that you can easily solve with our FREE APIs.

<img src="./media/sample_queueit.png" alt="Queue-IT's Captcha" width="400" /> 

Check out [queueit.py](./queueit.py) for an example script

## Having issue with your captcha?
We can fine tune our ML model in order to quickly work for you as well. Contact me [hj@ganhj.dev](mailto:hj@ganhj.dev)
