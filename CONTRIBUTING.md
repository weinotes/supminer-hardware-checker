# Contributing to SupMiner Hardware Checker

Thanks for your interest in contributing! 🎉

## How to Contribute

1. **Fork** the repo on GitHub
2. **Clone** your fork locally
3. Create a **feature branch** (`git checkout -b feature/my-feature`)
4. Make your changes
5. Run `make test` to verify nothing is broken
6. **Commit** with a clear message
7. **Push** to your fork
8. Open a **Pull Request**

## Development Setup

```bash
git clone https://github.com/weinotes/supminer-hardware-checker.git
cd supminer-hardware-checker
pip install -e .[rich]
make test
```

## Guidelines

- Keep it simple — this tool targets users of all skill levels
- Update `data.py` if adding/modifying mining projects
- Add type hints for new functions
- Run `make lint` before committing (if ruff is available)
- Update `CHANGELOG.md` for user-facing changes

## Project Structure

```
src/supminer_hardware_checker/
├── __init__.py    # Package metadata
├── __main__.py    # `python -m` entry point
├── data.py        # Mining project definitions
└── detector.py    # Core detection logic
```

## Questions?

Open an issue or email support@supminer.net
