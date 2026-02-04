install:
	uv sync

VD-games:
	uv run vd-game

build:
	uv build

package-install:
	uv tool install dist/*.whl
