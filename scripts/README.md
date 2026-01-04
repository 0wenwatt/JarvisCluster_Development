# Scripts

This directory contains utility scripts for managing the development tracking repository.

## Available Scripts

### For Tracking Integration

- `setup-tracking.sh` - Initial setup for tracking integration
- `manual-snapshot.sh` - Take a manual snapshot of Jarvis repo
- `generate-report.sh` - Generate reports on demand
- `sync-state.sh` - Sync latest state from Jarvis repo

### For Data Management

- `cleanup-old-snapshots.sh` - Clean up old snapshot data
- `export-metrics.sh` - Export metrics to CSV/JSON
- `validate-data.sh` - Validate snapshot data integrity

### For Analysis

- `compare-milestones.sh` - Compare actual vs. planned milestones
- `coverage-trend.sh` - Show test coverage trends
- `velocity-report.sh` - Calculate development velocity

## Usage

Make scripts executable:
```bash
chmod +x scripts/*.sh
```

Run a script:
```bash
./scripts/manual-snapshot.sh
```

## Creating New Scripts

When adding new scripts:
1. Add a clear description at the top
2. Include usage instructions
3. Make it executable
4. Update this README
5. Follow the project's shell scripting standards
