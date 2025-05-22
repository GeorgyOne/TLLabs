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

### ASCII Visualization

You can generate a simple ASCII chart for returns stored in the `DIFF1`
file using:

```bash
python -m tllabs.viz --column diff_return_trend_team
```

This command prints an ASCII line chart for the reconstructed close price
and its RSI indicator.

## Development

Tests rely only on the Python standard library and can be executed with:

```bash
python -m unittest discover -s tests
```
