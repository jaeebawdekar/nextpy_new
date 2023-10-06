"""Stub file for code.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, Optional, Union, overload
from dotserve.components.libs.chakra import ChakraComponent
from dotserve.components.component import Component
from dotserve.vars import Var, BaseVar, ComputedVar
from dotserve.event import EventHandler, EventChain, EventSpec

PRISM_STYLES_PATH: str

class CodeBlock(Component):
    @overload
    @classmethod
    def create(cls, *children, can_copy: Optional[bool] = None, copy_button: Optional[Union[bool, Component]] = None, theme: Optional[Union[Var[str], str]] = None, language: Optional[Union[Var[str], str]] = None, show_line_numbers: Optional[Union[Var[bool], bool]] = None, starting_line_number: Optional[Union[Var[int], int]] = None, wrap_long_lines: Optional[Union[Var[bool], bool]] = None, custom_style: Optional[Union[Var[Dict[str, str]], Dict[str, str]]] = None, code_tag_props: Optional[Union[Var[Dict[str, str]], Dict[str, str]]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "CodeBlock":  # type: ignore
        """Create a text component.

        Args:
            *children: The children of the component.
            theme: The theme to use ("light" or "dark").
            language: The language to use.
            show_line_numbers: If this is enabled line numbers will be shown next to the code block.
            starting_line_number: The starting line number to use.
            wrap_long_lines: Whether to wrap long lines.
            custom_style: A custom style for the code block.
            code_tag_props: Props passed down to the code tag.
            can_copy: Whether a copy button should appears.
            copy_button: A custom copy button to override the default one.
            **props: The props to pass to the component.

        Returns:
            The text component.
        """
        ...

class Code(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Code":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...