import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply()  # Needed to run interactive python

"""
Make sure:
1. The server is running before running this script.
2. The server is configured to use SSE transport.
3. The server is listening on port 8050.

To run the server:
uv run server.py
"""


async def main():
    # Connect to the server using SSE
    async with sse_client("http://localhost:8052/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Example calls for each tool
            print("\nCalling tools...") 
            date_result = await session.call_tool("extract_dates", arguments={"text": "Meeting on 2023-12-25 or 12/31/2023"})
            email_result = await session.call_tool("validate_email", arguments={"email": "user.name@example.com"})
            slug_result = await session.call_tool("generate_slug", arguments={"text": "My Awesome Blog Post 2023!"})
            password_result = await session.call_tool("check_password_strength", arguments={"password": "SecurePass123"})
            name_result = await session.call_tool("capitalize_names", arguments={"name": "jane austin"})
            hashtag_result = await session.call_tool("extract_hashtags", arguments={"text": "Loving #Python and #MachineLearning"})
            reading_result = await session.call_tool("calculate_reading_time", arguments={"text": "This is a sample article. " * 100})
            sentiment_result = await session.call_tool("basic_sentiment", arguments={"text": "Great experience but poor customer service"})

            print(f"""
            Date Extraction: {date_result.content[0].text}
            Email Validation: {email_result.content[0].text}
            Generated Slug: {slug_result.content[0].text}
            Password Strength: {password_result.content[0].text}
            Capitalized Name: {name_result.content[0].text}
            Hashtags Found: {hashtag_result.content[0].text}
            Reading Time (mins): {reading_result.content[0].text}
            Sentiment Score: {sentiment_result.content[0].text}
            """)


if __name__ == "__main__":
    import nest_asyncio
    asyncio.run(main())