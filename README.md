# Books
GraphQL API example.

## Usage

### General
Endpoint: `<server>/books`

Method: `POST`

Headers: `Content-Type`: `application/json`

### Body

Query all books
```graphql
{
    "query": "{ books { title author } }"
}
```

Query one book
```graphql
{
    "query": "{ book(title: \"1984\") { title author } }"
}
```

Add a new book
```graphql
{
    "query": "mutation { addBook(title: \"Dune\", author: \"Frank Herbert\") { success book { title author } } }"
}
```

### Return values
- `200` Success
- `400` `"query"` missing
- `415` Request not JSON

### Testing
The folder `postman` includes a Postman collection and environment to test the API.

## Tools
Flask / Graphene / Python

## Author
ChatGPT 5, prompted by Arturo Mora-Rioja, based on [Kesha Williams' repo](https://github.com/LinkedInLearning/programming-foundations-apis-and-web-services-3811153/tree/main/03_02) from her LinkedIn Learning course [*Programming Foundations: APIs and Web Services*](https://www.linkedin.com/learning/programming-foundations-apis-and-web-services-27993033).