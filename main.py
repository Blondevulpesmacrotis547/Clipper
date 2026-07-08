#!/usr/bin/env python3
# Clipper_Builder - main entry point

import os
from builder import Builder

def main():
    print("[*] Clipper_Builder v1.0.0")
    print("[*] Educational project. Check Releases for the archive.")
    b = Builder()
    b.run()

if __name__ == "__main__":
    main()