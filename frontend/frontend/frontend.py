"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import requests


class State(rx.State):
    math_ops: list[str] = []
    val1: int = 0
    val2: int = 0
    math_op: str
    result: int

    def on_page_load(self):
        # url = 'http://127.0.0.1:8001'
        url = 'http://78.46.49.173:8001'
        response = requests.get(f"{url}/math-operations")
        
        if response.status_code == 200:
            result = response.json()
            self.math_ops = result.get("response")
        else:
            # show error
            ...

    def send_calc_request(self):
        req_data = {
            "args": [self.val1, self.val2],
            "operations": [self.math_op]
        }
        # url = 'http://127.0.0.1:8001'
        url = 'http://78.46.49.173:8001'
        response = requests.post(f"{url}/calculate", json=req_data)
        if response.status_code == 200:
            result = response.json()
            print(result)
            self.result = result.get("response")
        else:
            # show error
            ...
        pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.hstack(
                rx.number_input(on_change=State.set_val1, default_value=0),
                rx.select(
                    State.math_ops,
                    on_change=State.set_math_op,
                    is_required=True,
                    style={"width": "4em"}
                ),
                rx.number_input(on_change=State.set_val2, default_value=0),
                rx.text("="),
                rx.text(State.result),
                rx.button("Count", on_click=State.send_calc_request),
            ),
            spacing="1.5em",
            font_size="1.5em",
            padding_top="10%",
        ),
    )


app = rx.App()
app.add_page(index, on_load=State.on_page_load)
app.compile()
