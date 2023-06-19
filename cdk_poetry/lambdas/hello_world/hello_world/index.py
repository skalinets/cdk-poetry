from common.helper import get_answer


def handler(event, context):
    f = get_answer("42")
    print(f"from handler: {f}")
    return f"42: {f}"
    # return {"statusCode": 200, "body": "hello"}
