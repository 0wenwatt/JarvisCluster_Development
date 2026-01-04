# Metrics Directory

This directory stores development metrics tracked over time.

## Metric Files

### `code-metrics.json`
Tracks code evolution over time:
```json
{
  "history": [
    {
      "date": "2026-01-04",
      "total_lines": 0,
      "code_lines": 0,
      "comment_lines": 0,
      "blank_lines": 0,
      "files_by_type": {
        ".go": 0,
        ".py": 0,
        ".md": 4
      }
    }
  ]
}
```

### `test-coverage.json`
Test coverage metrics:
```json
{
  "history": [
    {
      "date": "2026-01-04",
      "overall_coverage": 0,
      "unit_test_coverage": 0,
      "integration_test_coverage": 0,
      "components": {}
    }
  ]
}
```

### `commit-activity.json`
Commit and contributor metrics:
```json
{
  "history": [
    {
      "date": "2026-01-04",
      "commits_today": 0,
      "active_contributors": [],
      "files_changed": 0,
      "lines_added": 0,
      "lines_removed": 0
    }
  ]
}
```

### `issue-metrics.json`
Issue and PR tracking:
```json
{
  "history": [
    {
      "date": "2026-01-04",
      "open_issues": 0,
      "closed_issues": 0,
      "open_prs": 0,
      "merged_prs": 0,
      "avg_time_to_close_issue": 0,
      "avg_time_to_merge_pr": 0
    }
  ]
}
```

## Visualization

These metrics can be used to generate charts and graphs showing:
- Code growth over time
- Test coverage trends
- Development velocity
- Team activity
