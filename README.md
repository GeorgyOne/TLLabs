# TLLabs

TLLabs is a simple example project that demonstrates a minimal Python
package with a command line interface.

## Structure

```
TLLabs/
├── src/          # source code for the package
│   └── tllabs/   # package implementation
├── tests/        # unit tests using the standard library
└── README.md     # project documentation
```

## Usage

Run the CLI directly:

```bash
python -m tllabs.cli
```

You can pass a custom greeting message:

```bash
python -m tllabs.cli --greet "Hi"
```

## Development

Tests rely only on the Python standard library and can be executed with:

```bash
python -m unittest discover -s tests
```
