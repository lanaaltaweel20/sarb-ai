#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on 0.0.0.0:{port}")
    sys.stdout.flush()  # Ensure the print statement is immediately visible
    
    # Import uvicorn here to ensure it's available
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)