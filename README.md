# Trashify-AI-Mircoservice Documentation

## Overview

**Trashify-AI-Mirco** is a gRPC-based microservice designed for use with a Next.js project. Its primary function is to find the nearest coordinates using the Ball Tree algorithm, leveraging the Scikit-learn library.

## Features

- **gRPC Server:** The service uses gRPC for efficient communication between services.
- **Nearest Neighbor Search:** Implements nearest neighbor search through the Ball Tree algorithm provided by Scikit-learn.
- **Microservice Architecture:** Designed as a microservice to be easily integrated into larger projects, such as a Next.js application.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- `scikit-learn` library
- `grpcio` and `grpcio-tools` for gRPC support

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd trashify-ai-mirco
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that your `requirements.txt` includes the following:

   ```text
   grpcio
   grpcio-tools
   scikit-learn
   ```

### Running the Server

To start the gRPC server:

```bash
python server.py
```

Ensure the server is running on the appropriate port configured in your Next.js project. This server is on 50051 by default!

## Usage

### gRPC Methods

The service exposes a set of gRPC methods to interact with the Ball Tree model. Below is a general outline of the key methods:

1. **GetNearestCoor**: Find the nearest coordinates to a given point.

   - **Request**: coordinates which must be an array (nested with arrays that includes **lat** and **long**, query_location which must be a single array of **lat** and **long**
   - **Response**: The nearest coordinate(s) found.

### Integration with Next.js

To use this microservice in your Next.js project:

1. Import the gRPC client in your Next.js API routes.
2. Make calls to the gRPC methods to retrieve nearest coordinates.
3. Handle responses as needed within your Next.js application.

## Development

### Generating gRPC Code (into Python so it can be used by my other class, inheritance OOP prinicpal)

If you make changes to the `.proto` file, regenerate the gRPC code:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. your_proto_file.proto
```

