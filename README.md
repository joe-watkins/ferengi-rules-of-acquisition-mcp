# Ferengi Rules of Acquisition MCP Server

An MCP (Model Context Protocol) server that provides access to all 286 Ferengi Rules of Acquisition from Star Trek. Built with [FastMCP](https://gofastmcp.com).

## Features

This server provides the following tools:

- **get_rule(rule_number)** - Retrieve a specific rule by its number (1-286)
- **search_rules(keyword)** - Search for rules containing a specific keyword
- **get_random_rule()** - Get a random rule for inspiration
- **list_all_rules()** - Get all 286 rules at once
- **get_rules_count()** - Get the total number of rules
- **get_rules_by_range(start, end)** - Get rules within a specific range

## Installation

### Local Testing

1. Clone this repository:
```bash
git clone <your-repo-url>
cd ferengi-rules-of-acquisition-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python server.py
```

### Deployment to FastMCP Cloud

This server is ready for deployment to [FastMCP Cloud](https://gofastmcp.com/deployment/fastmcp-cloud).

1. Ensure you have:
   - `server.py` - The main server file
   - `requirements.txt` - Python dependencies
   - `data/ferengi-rules-of-acquisition.json` - The rules database

2. Deploy to FastMCP Cloud following the [official documentation](https://gofastmcp.com/deployment/fastmcp-cloud)

## Usage Examples

Once connected to an MCP client (like Claude Desktop), you can:

- Get Rule #1: "Once you have their money, never give it back"
- Search for rules about "profit"
- Get a random rule for daily inspiration
- Browse rules by range (e.g., rules 1-10)

## Data Source

The Ferengi Rules of Acquisition are from the Star Trek universe, specifically from Deep Space Nine and other series. This collection includes all 286 canonical and apocryphal rules.

## License

This is a fan project for educational purposes. Star Trek and all related marks and logos are trademarks of CBS Studios Inc.

## Contributing

Feel free to submit issues and pull requests!
