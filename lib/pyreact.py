# Load React and ReactDOM JavaScript libraries into local namespace
React = require("react")
ReactDOM = require("react-dom")

"""
This is `render` function calls the `render` in ReactDOM.
This function literally pass all parameters that the ReactDOM.render wants
"""
def render(root_component, props, container):
    def main():
        ReactDOM.render(
            React.createElement(root_component, props),
            document.getElementById(container),
        )

    document.addEventListener("DOMContentLoaded", main)


# Map React javaScript objects to Python identifiers
createElement = React.createElement
useState = React.useState
useEffect = React.useEffect


def setDocumentTitle(title):
    document.title = title
