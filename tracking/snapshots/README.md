# Snapshot Directory

This directory stores point-in-time snapshots of the Jarvis implementation repository.

## File Naming Convention

- Format: `YYYY-MM-DD-HHmm-snapshot.json`
- Example: `2026-01-04-2117-snapshot.json`

## Snapshot Contents

Each snapshot should include:
1. **Repository metadata** - URL, branch, latest commit
2. **File structure** - Directory tree and file list
3. **Code metrics** - Line counts, file counts by type
4. **Git information** - Recent commits, active branches
5. **Dependencies** - Package versions
6. **Build status** - Latest build/test results
7. **Issues/PRs** - Open issues and pull requests

## Usage

Your automated tracking program should:
1. Pull latest state from Jarvis repo
2. Generate snapshot JSON
3. Save to this directory with timestamp
4. Update `latest.json` symlink or file

## Retention Policy

- Keep daily snapshots for 30 days
- Keep weekly snapshots for 1 year
- Keep monthly snapshots indefinitely
- Or adjust based on your needs
