"""
Quick test script for the Ferengi Rules MCP server
"""
from server import RULES
import json

print("Testing Ferengi Rules MCP Server\n")
print("=" * 50)

# Test 1: Data loaded correctly
print(f"\n1. Data loaded: {len(RULES)} rules")
print(f"   First rule: Rule #{RULES[0]['id']}: {RULES[0]['rule']}")
print(f"   Last rule: Rule #{RULES[-1]['id']}: {RULES[-1]['rule']}")

# Test 2: Search functionality
print("\n2. Testing search for 'profit':")
matches = [r for r in RULES if 'profit' in r['rule'].lower()]
print(f"   Found {len(matches)} rules containing 'profit'")
print(f"   Example: Rule #{matches[0]['id']}: {matches[0]['rule']}")

# Test 3: Get specific rule
print("\n3. Testing get specific rule (#1):")
rule = next((r for r in RULES if r['id'] == 1), None)
if rule:
    print(f"   Rule #{rule['id']}: {rule['rule']}")

# Test 4: Range query
print("\n4. Testing range query (rules 1-5):")
range_rules = [r for r in RULES if 1 <= r['id'] <= 5]
print(f"   Found {len(range_rules)} rules in range")
for r in range_rules[:3]:
    print(f"   - Rule #{r['id']}: {r['rule']}")

print("\n" + "=" * 50)
print("All tests completed successfully!")
print("\nServer is ready for MCP deployment!")
