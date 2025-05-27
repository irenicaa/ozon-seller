# ozon-seller

[![lint](https://github.com/irenicaa/ozon-seller/actions/workflows/lint.yaml/badge.svg)](https://github.com/irenicaa/ozon-seller/actions/workflows/lint.yaml)
[![test](https://github.com/irenicaa/ozon-seller/actions/workflows/test.yaml/badge.svg)](https://github.com/irenicaa/ozon-seller/actions/workflows/test.yaml)

A library that implements a client for [Ozon Seller API](https://docs.ozon.ru/api/seller/en/).

## Features

- common features:
  - use [dataclasses](https://docs.python.org/3/library/dataclasses.html) for all the request and responses
  - support for automatic JSON serialization and parsing for all the request and responses, respectively
  - implement iterators for the endpoints with pagination
  - powerful error handling — for each error is available:
    - HTTP status
    - [Ozon Seller API](https://docs.ozon.ru/api/seller/en/) error code and message

## Installation

Clone this repository:

```
$ git clone https://github.com/irenicaa/ozon-seller
$ cd ozon-seller
```

Then install the library:

```
$ make install
```

## License

The MIT License (MIT)

Copyright &copy; 2022 irenica
