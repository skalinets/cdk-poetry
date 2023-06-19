import pendulum


def get_answer(s):
    now = pendulum.now("UTC")

    d = now.to_iso8601_string()
    return f"answer for {s} is {d}"
