from guardrails.validator_base import FailResult, PassResult
from validator import ContainsString


def test_success_case():
    validator = ContainsString("s")
    result = validator.validate("pass", {})
    assert isinstance(result, PassResult) is True


def test_failure_case():
    validator = ContainsString("s")
    result = validator.validate("fail", {})
    assert isinstance(result, FailResult) is True
    assert result.error_message == "fail doesn't contain s"
