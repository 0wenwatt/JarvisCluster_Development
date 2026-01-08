# Assets Directory

This directory stores visual assets, diagrams, images, and other media files for the JarvisCluster_Development repository.

## Purpose

Store visual materials such as:
- Architecture diagrams
- Workflow visualizations
- UI mockups and wireframes
- Screenshots
- Logos and branding materials
- Exported graphs and charts
- Presentation slides

## Organization

Consider organizing assets by type or purpose:

```
assets/
├── diagrams/           # Architecture and system diagrams
├── images/             # General images and screenshots
├── logos/              # Branding and logo files
├── charts/             # Exported charts and graphs
└── presentations/      # Slide decks and presentation materials
```

## File Formats

Recommended formats:
- **Diagrams**: PNG, SVG, PDF
- **Photos/Screenshots**: PNG, JPG
- **Vector Graphics**: SVG, PDF
- **Documents**: PDF
- **Editable Sources**: Keep original files (e.g., .drawio, .sketch, .psd)

## Best Practices

1. Use descriptive filenames: `jarvis-architecture-overview.png`
2. Include dates for versioned assets: `jarvis-workflow-2026-01-08.svg`
3. Keep source files alongside exports
4. Document complex diagrams with accompanying markdown files
5. Optimize image sizes for web viewing

## Usage in Documentation

Reference assets in markdown documents using relative paths:

```markdown
![Architecture Overview](../assets/diagrams/architecture-overview.png)
```

## Version Control

- **DO commit**: Final diagrams, images, logos
- **CONSIDER excluding**: Very large files (>5MB) - use Git LFS
- **AVOID committing**: Temporary files, cache files, build artifacts
