#!/usr/bin/env python3
import os
import sys
from main import app
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on 0.0.0.0:{port}")
    sys.stdout.flush()  # Ensure the print statement is immediately visible
    uvicorn.run(app, host="0.0.0.0", port=port, reload=False)