from django.conf import settings


def yandex_decorator(f):
    def wrapper(*args, **kwargs):
        st = f(*args, **kwargs)
        return {
            "response": {
                "text": st,
                "tts": st,
                "endsession": "false",
            },
            "version": settings.VERSION,
        }

    return wrapper


def yandex_data_handler(data: dict):
    return data["request"]["original_utterance"]


@yandex_decorator
def yandex_response_handler(data: dict):
    return data["message"]
