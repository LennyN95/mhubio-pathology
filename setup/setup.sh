#!/bin/bash

# create dir for the dummy dependency
mkdir -p /app/src/test_collection

# install a dummy dependency script
cat <<EOF > /app/src/test_collection/dummy_dependency.py
#!/usr/bin/env python3

import sys

def main():
  args = sys.argv[1:]
  print("Input arguments:", args)

if __name__ == "__main__":
  main()
EOF

chmod +x /app/src/test_collection/dummy_dependency.py