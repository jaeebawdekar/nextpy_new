from unittest.mock import mock_open

import pytest

from nextpy import constants
from nextpy.core.config import Config
from nextpy.utils.prerequisites import initialize_requirements_txt, update_next_config


@pytest.mark.parametrize(
    "template_next_config, nextpy_config, expected_next_config",
    [
        (
            """
                module.exports = {
                    basePath: "",
                    compress: true,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
            Config(
                app_name="test",
            ),
            """
                module.exports = {
                    basePath: "",
                    compress: true,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
        ),
        (
            """
                module.exports = {
                    basePath: "",
                    compress: true,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
            Config(
                app_name="test",
                next_compression=False,
            ),
            """
                module.exports = {
                    basePath: "",
                    compress: false,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
        ),
        (
            """
                module.exports = {
                    basePath: "",
                    compress: true,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
            Config(
                app_name="test",
                frontend_path="/test",
            ),
            """
                module.exports = {
                    basePath: "/test",
                    compress: true,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
        ),
        (
            """
                module.exports = {
                    basePath: "",
                    compress: true,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
            Config(
                app_name="test",
                frontend_path="/test",
                next_compression=False,
            ),
            """
                module.exports = {
                    basePath: "/test",
                    compress: false,
                    reactStrictMode: true,
                    trailingSlash: true,
                };
            """,
        ),
    ],
)
def test_update_next_config(template_next_config, nextpy_config, expected_next_config):
    assert (
        update_next_config(template_next_config, nextpy_config) == expected_next_config
    )


def test_initialize_requirements_txt(mocker):
    # File exists, nextpy is included, do nothing
    mocker.patch("os.path.exists", return_value=True)
    open_mock = mock_open(read_data="nextpy==0.1.0b2")
    mocker.patch("builtins.open", open_mock)
    initialize_requirements_txt()
    assert open_mock.call_count == 1
    assert open_mock().write.call_count == 0


def test_initialize_requirements_txt_missing_nextpy(mocker):
    # File exists, nextpy is not included, add nextpy    open_mock = mock_open(read_data="random-package=1.2.3")
    mocker.patch("builtins.open", open_mock)
    initialize_requirements_txt()
    # Currently open for read, then open for append
    assert open_mock.call_count == 2
    assert open_mock().write.call_count == 1
    assert (
        open_mock().write.call_args[0][0]
        == f"\n{constants.RequirementsTxt.DEFAULTS_STUB}{constants.Nextpy.VERSION}\n"
    )


def test_initialize_requirements_txt_not_exist(mocker):
    # File does not exist, create file with nextpy    mocker.patch("os.path.exists", return_value=False)
    open_mock = mock_open()
    mocker.patch("builtins.open", open_mock)
    initialize_requirements_txt()
    assert open_mock.call_count == 2
    assert open_mock().write.call_count == 1
    assert (
        open_mock().write.call_args[0][0]
        == f"\n{constants.RequirementsTxt.DEFAULTS_STUB}{constants.Nextpy.VERSION}\n"
    )
