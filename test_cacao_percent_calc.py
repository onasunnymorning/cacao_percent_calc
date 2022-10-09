import json
import pytest

from cacao_percent_calc import handler, calculate_percentage, validate_body


@pytest.fixture
def event_fix_valid():
    body = json.dumps({
        'cacao_butter': 100,
        'cacao': 3900,
        'sugar': 1000,
        'milk_powder': 0,
        'other': 0
    })
    event = {'body': body}
    return event


@pytest.fixture
def event_fix_invalid():
    body = json.dumps({
        'milk_powder': 0,
        'other': 0
    })
    event = {'body': body}
    return event


@pytest.fixture
def context_fix():
    return {}



@pytest.fixture
def list_fix():
    return [100, 3900, 1000, 0, 0]


def test_80(event_fix_valid, context_fix):
    result = handler(event_fix_valid, context_fix)
    body = json.loads(result['body'])
    assert result['statusCode'] == 200
    assert body['total'] == 5000


def test_80_fail(event_fix_invalid, context_fix):
    result = handler(event_fix_invalid, context_fix)
    body = json.loads(result['body'])
    assert result['statusCode'] == 400
    assert body == {
                'message': {
                    'mandatory_keys': [
                        'cacao_butter',
                        'cacao',
                        'sugar',
                        'milk_powder',
                        'other'
                    ]
                }}


def test_calculate_percentage(list_fix):
    result = calculate_percentage(list_fix)
    assert result['total'] == 5000
    assert result['cacao_percent'] == 0.8
    assert result['cacao_butter_percent'] == 0.02


