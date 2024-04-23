# Overview

| Developed by | Guardrails AI |
| Date of development | Feb 15, 2024 |
| Validator type | Format |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

## Description

### Intended Use
This validator is a template for creating other validators, but for demonstrative purposes it ensures that a generated output is the literal `pass`.

### Requirements

* Dependencies:
	- guardrails-ai>=0.4.0

* Foundation model access keys:
	- OPENAI_API_KEY

## Installation

```bash
$ guardrails hub install hub://guardrails/validator_template
```

## Usage Examples

### Validating string output via Python

In this example, we apply the validator to a string output generated by an LLM.

```python
# Import Guard and Validator
from guardrails.hub import ValidatorTemplate
from guardrails import Guard

# Setup Guard
guard = Guard().use(
    ValidatorTemplate
)

guard.validate("pass")  # Validator passes
guard.validate("fail")  # Validator fails
```

### Validating JSON output via Python

In this example, we apply the validator to a string field of a JSON output generated by an LLM.

```python
# Import Guard and Validator
from pydantic import BaseModel, Field
from guardrails.hub import ValidatorTemplate
from guardrails import Guard

# Initialize Validator
val = ValidatorTemplate()

# Create Pydantic BaseModel
class Process(BaseModel):
		process_name: str
		status: str = Field(validators=[val])

# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=Process)

# Run LLM output generating JSON through guard
guard.parse("""
{
	"process_name": "templating",
	"status": "pass"
}
""")
```

# API Reference

**`__init__(self, on_fail="noop")`**
<ul>
Initializes a new instance of the ValidatorTemplate class.

**Parameters**
- **`arg_1`** *(str)*: A placeholder argument to demonstrate how to use init arguments.
- **`arg_2`** *(str)*: Another placeholder argument to demonstrate how to use init arguments.
- **`on_fail`** *(str, Callable)*: The policy to enact when a validator fails.  If `str`, must be one of `reask`, `fix`, `filter`, `refrain`, `noop`, `exception` or `fix_reask`. Otherwise, must be a function that is called when the validator fails.
</ul>
<br/>

**`validate(self, value, metadata) → ValidationResult`**
<ul>
Validates the given `value` using the rules defined in this validator, relying on the `metadata` provided to customize the validation process. This method is automatically invoked by `guard.parse(...)`, ensuring the validation logic is applied to the input data.

Note:

1. This method should not be called directly by the user. Instead, invoke `guard.parse(...)` where this method will be called internally for each associated Validator.
2. When invoking `guard.parse(...)`, ensure to pass the appropriate `metadata` dictionary that includes keys and values required by this validator. If `guard` is associated with multiple validators, combine all necessary metadata into a single dictionary.

**Parameters**
- **`value`** *(Any):* The input value to validate.
- **`metadata`** *(dict):* A dictionary containing metadata required for validation. Keys and values must match the expectations of this validator.
    
    
    | Key | Type | Description | Default |
    | --- | --- | --- | --- |
    | key1 | String | Description of key1's role. | N/A |
</ul>
