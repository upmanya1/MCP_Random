# MCP Text Processing Tools Demo

A client-server system demonstrating text processing utilities using MCP (Modular Computing Platform) with Server-Sent Events (SSE) transport. The server provides various text manipulation and validation tools.

## Project Overview

- **Server**: FastMCP server offering text analysis, validation, and formatting tools
- **Client**: Demonstrates usage of all server tools with example inputs
- **Port**: 8052 (SSE transport)

## Prerequisites

- Python 3.7+
- `uv` server (install with `pip install uv`)
- Required packages in requirements.txt

## Installation

```bash
pip install -r requirements.txt
```

## Server Tools

| Tool Name                  | Description                                                                 | Parameters                     |
|----------------------------|-----------------------------------------------------------------------------|--------------------------------|
| `extract_dates`            | Finds date patterns in text using regex                                     | `text` (str)                   |
| `validate_email`           | Verifies email format validity                                              | `email` (str)                  |
| `generate_slug`            | Creates URL-friendly slugs from text                                        | `text` (str)                   |
| `check_password_strength`  | Checks if password meets basic security rules                               | `password` (str)               |
| `capitalize_names`         | Properly capitalizes personal names                                         | `name` (str)                   |
| `extract_hashtags`         | Identifies social media hashtags in text                                    | `text` (str)                   |
| `calculate_reading_time`   | Estimates content reading time (default 200 wpm)                            | `text` (str), [wpm] (int)      |
| `basic_sentiment`          | Simple positive/negative word scoring (-neg +pos)                           | `text` (str)                   |

## Running the System

1. **Start Server**:
```bash
uv run server.py
```

2. **Run Client** (in separate terminal):
```bash
python client.py
```

**Sample Client Output**:
```
Available tools:
  - extract_dates: Takes a string text...
  - validate_email: Takes a string email...
  ... (tool list)

Date Extraction: ['2023-12-25', '12/31/2023']
Email Validation: True
Generated Slug: my-awesome-blog-post-2023
Password Strength: True
Capitalized Name: Jane Austin
Hashtags Found: ['#Python', '#MachineLearning']
Reading Time (mins): 1
Sentiment Score: 0
```

## Custom Usage Example

Modify client.py to test different inputs:
```python
# Example: Check different password
pass_result = await session.call_tool(
    "check_password_strength",
    arguments={"password": "weak"}
)
print(f"Password valid: {pass_result.content[0].text}")
```

## Troubleshooting

- **Port Conflicts**: Ensure port 8052 is available
- **Regex Errors**: Some tools use simple regex patterns (may not cover all edge cases)
- **Async Issues**: Keep `nest_asyncio.apply()` for interactive environments
- **Tool Errors**: Verify parameter names match server definitions exactly
