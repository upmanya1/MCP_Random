from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="RandomTools",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8052,  # only used for SSE transport (set this to any port)
)


@mcp.tool()
def extract_dates(text: str) -> list[str]:
    """Takes a string text (source to scan) as input. Find date-like patterns using simple regex"""
    import re
    return re.findall(r'\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4}', text)

@mcp.tool()
def validate_email(email: str) -> bool:
    """Takes a string email (address to verify) as input. Check valid email format"""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

@mcp.tool()
def generate_slug(text: str) -> str:
    """Takes string text (content to convert) as input. Create URL-friendly slug"""
    return text.strip().lower().replace(' ', '-').replace('[^\w-]', '')[:60]

@mcp.tool()
def check_password_strength(password: str) -> bool:
    """Takes string password (text to evaluate) as input. Verify basic security criteria"""
    return (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password)
    )

@mcp.tool()
def capitalize_names(name: str) -> str:
    """Takes string name (full name input) as input. Format personal names properly"""
    return ' '.join([part.capitalize() for part in name.split()])

@mcp.tool()
def extract_hashtags(text: str) -> list[str]:
    """Takes string text (social content) as input. Identify social media hashtags"""
    import re
    return re.findall(r'#\w+', text)

@mcp.tool()
def calculate_reading_time(text: str, wpm: int = 200) -> int:
    """Takes string text (content to measure) and optional wpm (words per minute). Estimate reading duration"""
    word_count = len(text.split())
    return max(1, round(word_count / wpm))

@mcp.tool()
def basic_sentiment(text: str) -> int:
    """Takes string text (content to analyze) as input. Simple positive/negative word score"""
    POSITIVE = ['good', 'great', 'excellent', 'happy']
    NEGATIVE = ['bad', 'poor', 'terrible', 'sad']
    words = text.lower().split()
    return sum(1 for w in words if w in POSITIVE) - sum(1 for w in words if w in NEGATIVE)

# Run the server
if __name__ == "__main__":
    transport = "sse"
    print("Running server with SSE transport")
    mcp.run(transport="sse")