import json


def handler(event, context):
    b = json.loads(event['body'])
    if not validate_body(b):
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': {
                    'mandatory_keys': [
                        'cacao_butter',
                        'cacao',
                        'sugar',
                        'milk_powder',
                        'other'
                    ]
                }
            })
        }
    ingredient_list = [b['cacao_butter'],
                       b['cacao'],
                       b['sugar'],
                       b['milk_powder'],
                       b['other']
    ]
    return {
        'statusCode': 200,
        'body': json.dumps(calculate_percentage(ingredient_list))
    }


def validate_body(bdy: dict):
    keys = ["cacao_butter", "cacao", "sugar", "milk_powder", "other"]
    if all(k in bdy for k in keys):
        return True
    return False


def calculate_percentage(i: list):
    total = sum(i)
    cacao = sum(i[0:2])
    cacao_butter = i[0]
    cp = cacao / total
    cbp = cacao_butter / total
    return {
        'total': total,
        'cacao_percent': cp,
        'cacao_butter_percent': cbp
    }