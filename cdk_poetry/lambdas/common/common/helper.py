import pendulum


def get_answer(s):
    now = pendulum.now("UTC")

    d = now.to_iso8601_string()
    print (f"from helper: {d}")
    return f"answer for {s} is {d}"
