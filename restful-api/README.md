## Basics of HTTP and HTTPS

### HTTP vs HTTPS
- **HTTP** sends data in plain text and is not secure.
- **HTTPS** is the secure version of HTTP and uses SSL/TLS encryption.
- HTTPS protects data from being read or modified by attackers.

### HTTP Request Structure
An HTTP request contains:
- Method (GET, POST, etc.)
- URL path
- Headers
- Optional body (for POST/PUT)

### HTTP Response Structure
An HTTP response contains:
- Status code (200, 404, etc.)
- Headers
- Response body

### Common HTTP Methods
- **GET**: Retrieve data
- **POST**: Send data
- **PUT**: Update data
- **DELETE**: Remove data

### Common HTTP Status Codes
- **200 OK**: Request successful
- **201 Created**: Resource created
- **301 Moved Permanently**: Redirect
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

### Common HTTP Methods
- **GET**: Retrieve data
- **POST**: Send data
- **PUT**: Update data
- **DELETE**: Remove data

### Common HTTP Status Codes
- **200 OK**: Request successful
- **201 Created**: Resource created
- **301 Moved Permanently**: Redirect
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

## Consuming an API Using curl

### What is curl?
curl is a command-line tool used to send and receive data from servers using HTTP and HTTPS. It is commonly used to test and interact with APIs.

### Check curl Installation
```bash
curl --version
