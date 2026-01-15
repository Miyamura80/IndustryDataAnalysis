# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Run Commands

- `make all` - Setup venv and run `main.py`
- `make test` - Run all tests with pytest
- `make fmt` - Format code with Black and JSON files with jq
- `make ci` - Run all CI checks (ruff, vulture, ty)
- `uv run python -m tests.path_to.test_module` - Run a specific test in isolation

## Package Management

This project uses **uv** (not pip) for dependency management. Dependencies are in `pyproject.toml`.

- `uv sync` - Sync dependencies
- `uv run python <file>.py` - Run Python files
- `uv pip install <package>` - Add new dependencies

## Configuration System

The project uses **pydantic-settings** for type-safe configuration with YAML + environment variables:

- `common/global_config.yaml` - Base configuration (hyperparameters, LLM settings, logging)
- `common/config_models.py` - Pydantic models for config validation
- `common/global_config.py` - Config class loading from YAML and `.env`
- `.env` - Secrets (API keys) - git-ignored
- `.global_config.yaml` - Local overrides (git-ignored, highest priority)

Access config:
```python
from common import global_config
print(global_config.example_parent.example_child)  # YAML values
print(global_config.OPENAI_API_KEY)  # Environment variables
```

Add new hyperparameters to `common/global_config.yaml`. For nested configs, define the Pydantic model in `config_models.py` first.

## LLM Inference

Use the DSPYInference wrapper in `utils/llm/dspy_inference.py` for LLM calls with built-in LangFuse observability:

```python
from utils.llm.dspy_inference import DSPYInference
import dspy

class MySignature(dspy.Signature):
    text: str = dspy.InputField()
    result: str = dspy.OutputField()

module = DSPYInference(pred_signature=MySignature)
result = await module.run(text="input")
```

Pass `tools=[...]` for agentic tool-use with dspy.ReAct.

## Logging

Use centralized logging from `src/utils/logging_config.py`:
```python
from loguru import logger as log
from src.utils.logging_config import setup_logging
setup_logging()
log.info("message")
```

Log levels are configured in `common/global_config.yaml` under `logging.levels`.

## Testing

Tests use pytest with a custom `TestTemplate` base class:

```python
from tests.test_template import TestTemplate, slow_test, nondeterministic_test

class TestFeature(TestTemplate):
    @pytest.fixture(autouse=True)
    def setup_shared_variables(self, setup):
        pass

    def test_something(self):
        assert True
```

- Inherit from `TestTemplate` for proper setup
- Use `@slow_test` or `@nondeterministic_test` decorators as appropriate
- Add `__init__.py` to new test directories

## Code Style

- Snake case for functions, files, directories
- CamelCase for classes
- UPPERCASE for constants
- Double quotes for strings
- 4 spaces for indentation
- Use native `list`, `tuple` type hints (Python 3.12+), not `typing.List`

## LangFuse Observability

Use `@observe` decorator for LLM tracing:
```python
from langfuse.decorators import observe, langfuse_context

@observe
def my_function():
    langfuse_context.update_current_observation(name="custom_name")
```

## Long-Running Code Pattern

For long-running operations, structure code as:
- `init()` - Initialize
- `continue(task_id)` - Resume from checkpoint
- `cleanup(task_id)` - Cleanup

Always checkpoint with IDs. Keep data serializable. Handle rate limits, timeouts, and retries at system boundaries.
