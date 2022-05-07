import json


def handler(event, context):
    b = json.loads(event['body'])
    print(b)
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


def calculate_percentage(i: list):
    total = sum(i)
    cacao = sum(i[0:2])
    p = cacao / total
    return {
        'total': total,
        'percentage': p
    }