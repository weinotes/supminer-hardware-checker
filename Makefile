.PHONY: install run lint clean test

install:
	pip install -e .[rich]

run:
	python -m supminer_hardware_checker

lint:
	ruff check src/

clean:
	rm -rf src/*.egg-info dist build
	rm -f hardware_report.json
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

test:
	python -c "from supminer_hardware_checker.detector import HardwareDetector; d = HardwareDetector(); d.detect_os(); d.detect_cpu(); d.detect_memory(); print('Import OK')"
