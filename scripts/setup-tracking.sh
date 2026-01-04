#!/bin/bash
# Setup script for tracking integration
# This script helps configure the tracking integration with the Jarvis repo

set -e

echo "========================================="
echo "Jarvis Development Tracking Setup"
echo "========================================="
echo ""

# Check if config file exists
CONFIG_FILE="config/tracking-config.yaml"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Config file not found at $CONFIG_FILE"
    exit 1
fi

echo "Step 1: Configure Jarvis Repository URL"
echo "----------------------------------------"
read -p "Enter the Jarvis repository URL: " JARVIS_URL

if [ -z "$JARVIS_URL" ]; then
    echo "Error: Repository URL cannot be empty"
    exit 1
fi

# Update config file (basic sed replacement)
echo "Updating configuration..."
sed -i.bak "s|url: \"\"|url: \"$JARVIS_URL\"|g" "$CONFIG_FILE"

echo "✓ Repository URL configured"
echo ""

echo "Step 2: Authentication Setup"
echo "----------------------------"
echo "If the Jarvis repo is private, you'll need authentication."
read -p "Is the repository private? (y/n): " IS_PRIVATE

if [ "$IS_PRIVATE" = "y" ] || [ "$IS_PRIVATE" = "Y" ]; then
    echo ""
    echo "Please set the JARVIS_REPO_TOKEN environment variable:"
    echo "  export JARVIS_REPO_TOKEN='your_github_token_here'"
    echo ""
    echo "Add this to your ~/.bashrc or ~/.zshrc to persist it."
fi

echo ""
echo "Step 3: Install Dependencies"
echo "----------------------------"
echo "This tracking system may need:"
echo "  - git (for cloning and tracking)"
echo "  - jq (for JSON processing)"
echo "  - cloc or tokei (for code metrics)"
echo ""
read -p "Install dependencies now? (requires sudo) (y/n): " INSTALL_DEPS

if [ "$INSTALL_DEPS" = "y" ] || [ "$INSTALL_DEPS" = "Y" ]; then
    echo "Installing dependencies..."
    
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y git jq cloc
    elif command -v brew &> /dev/null; then
        brew install git jq cloc
    else
        echo "Package manager not detected. Please install manually:"
        echo "  - git"
        echo "  - jq"
        echo "  - cloc or tokei"
    fi
    
    echo "✓ Dependencies installed"
fi

echo ""
echo "Step 4: Create Tracking Directories"
echo "------------------------------------"
mkdir -p tracking/snapshots
mkdir -p tracking/metrics
mkdir -p tracking/reports

echo "✓ Directories created"

echo ""
echo "========================================="
echo "Setup Complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Review and customize config/tracking-config.yaml"
echo "2. Run './scripts/manual-snapshot.sh' to test"
echo "3. Set up automated tracking (cron job or CI)"
echo ""
echo "For help, see docs/guides/tracking-setup.md (when created)"
