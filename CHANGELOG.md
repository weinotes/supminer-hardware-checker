# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Author:** Davey Wong <wgwcko@gmail.com> | [www.guangweiblog.com](https://www.guangweiblog.com)

## [3.0.0] - 2025-05-10

### Added
- Proper Python package structure (`src/` layout with `pyproject.toml`)
- `__main__.py` — run via `python -m supminer_hardware_checker`
- Type hints throughout the codebase (PEP 484)
- `dataclass`-based `SystemInfo` model for structured data
- `pathlib.Path` for all file operations
- `Makefile` with `install`, `run`, `lint`, `clean` targets
- `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` for community engagement

### Changed
- Refactored `HardwareDetector` to use explicit type annotations
- Improved GPU detection error handling (per-card fallback, timeout robustness)
- Mining project data extracted to `data.py` for easier maintenance
- CLI output uses richer formatting with `rich` (optional; falls back gracefully)
- `.gitignore` — removed overly broad `*.json` exclusion; only blocks `hardware_report.json`
- `requirements.txt` pinned to `psutil>=5.9.0`, added optional `rich>=13.0.0`
- README restructured with clearer sections and modern formatting

### Removed
- Standalone `hardware_checker.py` at repo root (moved into package)

## [2.0.0] - 2024-12-07

### Changed
- Full rewrite for mainstream-only project recommendations
- Removed niche coins (Qubic, Nexa, Nexus, Ore, Gauntlet)
- Added BTC, LTC, DOGE, ETC, RVN, KAS, ERG, XMR
- Detailed pool and exchange information

## [1.0.0] - 2024-12-06

- Initial release
