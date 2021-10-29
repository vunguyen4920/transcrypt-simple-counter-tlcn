from lib.pyreact import consoleLog, alert, useState, render, createElement as el


def App():
    val, setVal = useState("")

    def changeValue(e):
        setVal(e.target.value)

    return [
        el("h3", None, "Hello World"),
        el("h3", None, val),
        el("input", {"onChange": changeValue, "value": val}),
    ]


render(App, None, "root")
