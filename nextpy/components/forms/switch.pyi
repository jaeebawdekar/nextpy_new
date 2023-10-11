"""Stub file for switch.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Optional, Union, overload
from nextpy.components.libs.chakra import ChakraComponent
from nextpy.components.component import Component
from nextpy.core.vars import Var, BaseVar, ComputedVar
from nextpy.event import EventHandler, EventChain, EventSpec

class Switch(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, is_checked: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_focusable: Optional[Union[Var[bool], bool]] = None, is_invalid: Optional[Union[Var[bool], bool]] = None, is_read_only: Optional[Union[Var[bool], bool]] = None, is_required: Optional[Union[Var[bool], bool]] = None, name: Optional[Union[Var[str], str]] = None, spacing: Optional[Union[Var[str], str]] = None, placeholder: Optional[Union[Var[str], str]] = None, color_scheme: Optional[Union[Var[str], str]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_change: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Switch":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            is_checked: If true, the switch will be checked. You'll need to set an on_change event handler to update its value (since it is now controlled)
            is_disabled: If true, the switch will be disabled
            is_focusable: If true and is_disabled prop is set, the switch will remain tabbable but not interactive.
            is_invalid: If true, the switch is marked as invalid. Changes style of unchecked state.
            is_read_only: If true, the switch will be readonly
            is_required: If true, the switch will be required
            name: The name of the input field in a switch (Useful for form submission).
            spacing: The spacing between the switch and its label text (0.5rem)
            placeholder: The placeholder text.
            color_scheme: The color scheme of the switch (e.g. "blue", "green", "red", etc.)
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
