# cacao percentage calculator
Lambda API to calculate cacao percentage of a chocolate recipe

## Usage
```
curl --location --request POST 'https://tjeeclmrh0.execute-api.us-west-2.amazonaws.com/' \
--header 'Content-Type: application/json' \
--data-raw '{
        "cacao_butter": 100,
        "cacao": 3900,
        "sugar": 1000,
        "milk_powder": 0,
        "other": 0
    }'
```
