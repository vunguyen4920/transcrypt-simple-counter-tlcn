from lib.jsutil import NODE_ENV
from lib.pyreact import console, alert, useState, render, createElement as el
from lib.emoji import node_emoji


# TODO: Add styles
def App():
    count, setCount = useState(0)

    console.log(NODE_ENV)

    def inc():
        console.log(count)
        setCount(lambda count: count + 1)

    def dec():
        alert(count)
        setCount(lambda count: count - 1)

    def Thumbs(props):
        return el(
            "div",
            None,
            el("span", None, node_emoji.find("thumbsup").emoji)
            if props.count > 5
            else el("span", None, node_emoji.find("thumbsdown").emoji),
        )

    return el(
        "div",
        {"className": "main"},
        el(
            "div",
            {"className": "count"},
            el("p", None, "Count: "),
            el("p", None, count),
            el(Thumbs, {"count": count}, None),
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
