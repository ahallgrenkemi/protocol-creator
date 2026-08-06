# Aurora Method Builder

A desktop editor for creating aurora unicycler based cycling protocols and exporting them as PalmSens MethodSCRIPT.

## How it works

1. Create a protocol with the visual builder or JSON editor.
2. Aurora Unicycler validates the input and converts it to a common `CyclingProtocol` model.
3. Save the editable source and normalized protocol in a `.psmethod` package.
4. Export PalmSens-compatible protocols as `.mscr` MethodSCRIPT files.

For more documentation and step specifications see the aurora unicycler library. Temperature steps can be saved in a package but cannot be exported to MethodSCRIPT because they require an external temperature controller implementation.

## Features

- Drag-and-drop visual editor with copying, reordering, unit conversion, imports, and loops.
- JSON protocol editing.
- Tag, open-circuit voltage, temperature, constant-current, constant-voltage, voltage-scan, impedance-spectroscopy, and loop steps.
- Open, import, and save `.psmethod` packages.
- Configure the PalmSens target, sample capacity, EIS values, and additional measurements during export.

## `.psmethod` format

A `.psmethod` file is custom file format used by the application. It stores both the original editable input and the normalized Aurora protocol, so the method can be reopened in its original editor mode while other consumers use a consistent protocol representation.

Every package written by the application has these top-level fields:

| Field | Type | Description |
| --- | --- | --- |
| `format` | string | Package identifier. It must be `palmsens_aurora_method_package`. |
| `name` | string | Human-readable method name shown by the editor. |
| `source_mode` | string | Editor used to create the method: `aurora_visual` or `aurora_json`. |
| `source_payload` | object or string | Original editable content. Its structure depends on `source_mode`, as described below. |
| `protocol_json` | object | Validated, normalized output from `CyclingProtocol.to_dict()`. This is used for MethodSCRIPT generation and by other package consumers. |

### `source_payload`

- `aurora_visual`: an object containing `globals`, `record`, `safety`, and the ordered `method` steps. It also preserves visual-editor details such as selected display units, current input mode, and loop target mode.
- `aurora_json`: the Aurora protocol JSON exactly as text in the JSON editor.

## Code structure

- `app.py` contains the main window and file workflows.
- `builder.py` contains the visual editor and converts its form data to protocols.
- `methods.py` handles protocol parsing, packages, loops, and MethodSCRIPT generation.
- `export_dialog.py` collects and validates export settings.
- `style.py` and `widgets.py` contain the small shared UI pieces.

## Aurora Unicycler

[Aurora Unicycler](https://github.com/EmpaEConversion/aurora-unicycler) provides the protocol models, validation, JSON conversion, and PalmSens MethodSCRIPT generation used by this application.

This project currently depends on a pinned revision of the library that includes temperature steps. The dependency is installed automatically from the URL in `pyproject.toml`.

## Run

Python 3.10 or newer is required. From the repository root, the shortest setup is with [uv](https://docs.astral.sh/uv/):

```sh
uv run aurora-method-builder
```

`uv` creates the environment and installs the dependencies automatically on the first run.

Alternatively, install it with `pip`:

```sh
python -m venv .venv
```

Activate the environment:

```sh
# Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Then install and run the application:

```sh
python -m pip install -e .
aurora-method-builder
```
