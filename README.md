# API Endpoints

## Payment Types

### Get all Payment Types - GET /api/paymentTypes/

*Response*
Status: **200 OK**
```
[
    {
        "id": 1,
        "name": "Cash",
        "slug": "cash"
    },
    {
        "id": 2,
        "name": "Lease",
        "slug": "lease"
    },
    {
        "id": 3,
        "name": "Financement",
        "slug": "finance"
    }
]
```

### Retrieve Single Payment Type - GET /api/paymentTypes/{id}/

*Response*
Status: **200 OK**
```javascript
{
    "id": 1,
    "name": "Cash",
    "slug": "cash"
}
```