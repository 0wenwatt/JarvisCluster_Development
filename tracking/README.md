# Tracking Directory

This directory contains automated snapshots and tracking data from the actual Jarvis implementation repository.

## Structure

### `/snapshots`
Point-in-time snapshots of the Jarvis repository state.

- `YYYY-MM-DD-snapshot.json` - Daily snapshots
- Contains: file structure, commit info, branch status, etc.

### `/metrics`
Development metrics and statistics over time.

- `code-metrics.json` - Lines of code, file counts, etc.
- `test-coverage.json` - Test coverage over time
- `commit-activity.json` - Commit frequency and contributors
- `issue-metrics.json` - Issue and PR tracking

### `/reports`
Generated reports comparing plan vs. actual implementation.

- `progress-report.md` - Overall progress against roadmap
- `deviation-report.md` - Deviations from the plan
- `component-status.md` - Status of each component

## Automated Injection

This directory is designed to receive automated updates from your tracking program.

Expected update frequency: [Daily/Weekly/On-demand]

## Data Format

### Snapshot Format (JSON)
```json
{
  "timestamp": "2026-01-04T21:17:00Z",
  "repository": {
    "url": "https://github.com/user/jarvis",
    "branch": "main",
    "last_commit": {
      "sha": "abc123",
      "message": "...",
      "author": "...",
      "date": "..."
    }
  },
  "structure": {
    "directories": [],
    "files": []
  },
  "metrics": {
    "total_files": 0,
    "lines_of_code": 0,
    "test_coverage": 0
  }
}
```

## Manual Updates

While this directory is primarily for automated updates, manual updates can be made when:
- Adding context or notes to snapshots
- Creating custom reports
- Documenting anomalies
