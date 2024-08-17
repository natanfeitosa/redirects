# Redirects Server

This repository contains a simple HTTP redirect server built in Python. It can be configured to redirect traffic from one domain to another using a specified status code.

## Features

- Redirects all requests to a new domain.
- Allows configuration of the HTTP status code for the redirect (301, 302, etc.).
- Supports full redirects, including pathnames and query strings, or redirects only to the root of the new domain.

## Requirements

- Python ^3.10
- Poetry

## Configuration

Before starting the server, you need to set the following environment variables:

1. **REDIRECT_STATUS**: Defines the HTTP status code to be used for the redirect (e.g., 301, 302).
2. **NEW_DOMAIN**: Specifies the new domain to which the traffic will be redirected (e.g., `https://newdomain.com`).
3. **FULL_REDIRECT**: A boolean value (`true` or `false`). If `true`, the server will redirect with the full pathname and query string. If `false`, it will redirect only to the root of the new domain.

### Example `.env` file

Create a `.env` file in the project root with the following content:

```env
REDIRECT_STATUS=301
NEW_DOMAIN=https://newdomain.com
FULL_REDIRECT=true
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/natanfeitosa/redirects.git
   cd redirects
   ```

2. Install Poetry, if you don't have it yet:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install the project dependencies:
   ```bash
   poetry install
   ```

## Usage

After setting up the environment variables and installing the dependencies, start the server with:

```bash
poetry run python main.py
```

The server will run on port `8000` by default. You can access it at `http://localhost:8000`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.