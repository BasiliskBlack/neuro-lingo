#!/bin/bash

# Initialize Git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: NeuroLingo v0.1.0"

echo "✅ Repository initialized with initial commit!"
echo "Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Add the remote: git remote add origin <your-repo-url>"
echo "3. Push your code: git push -u origin main"
