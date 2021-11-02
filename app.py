from lib.pyreact import consoleLog, alert, useState, render, createElement as el


def App():
    count, setCount = useState(0)

    def inc():
        consoleLog(count)
        setCount(lambda count: count + 1)

    def dec():
        alert(count)
        setCount(lambda count: count - 1)

    return el(
        "div",
        {"className": "main"},
        el(
            "div",
            {"className": "count"},
            el("p", None, "Count: "),
            el("p", None, count),
        ),
        el(
            "div",
            {"className": "buttons"},
            el(
                "button",
                {"className": "button", "type": "button", "onClick": inc},
                "+",
            ),
            el(
                "button",
                {"className": "button", "type": "button", "onClick": dec},
                "-",
            ),
        ),
    )


render(App, None, "root")
