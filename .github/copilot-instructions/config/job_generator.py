#!/usr/bin/env python3
"""
Job Generator - Creates specific agent jobs from snippets and context.

Usage:
    python job_generator.py --role coder --step 14 --context context_step14.json
    python job_generator.py --role designer --step 14 --title "Clustering Algorithm"
    python job_generator.py --role maintainer --step 14 --context context_step14.json

This script:
1. Reads snippets database (snippets.yml)
2. Reads role definitions (roles.yml)
3. Takes user context input
4. Generates a specific job combining:
   - Always-include snippets for the role
   - Context-dependent snippets (if conditions met)
   - Personalized content based on step and context
"""

import json
import yaml
import argparse
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any


class JobGenerator:
    """Generate specific agent jobs from snippets and context."""
    
    def __init__(self, config_dir: str = "."):
        """Initialize generator with config files."""
        self.config_dir = Path(config_dir)
        self.snippets_config = self._load_yaml("snippets.yml")
        self.roles_config = self._load_yaml("roles.yml")
    
    def _load_yaml(self, filename: str) -> Dict:
        """Load YAML config file."""
        path = self.config_dir / filename
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def generate_job(self, 
                    role: str,
                    step: int,
                    title: str = None,
                    context: Dict = None) -> Dict:
        """
        Generate a specific job for an agent.
        
        Args:
            role: 'designer', 'coder', or 'maintainer'
            step: Step number (1-N)
            title: Step title (e.g., "Implement Clustering Algorithm")
            context: Dictionary with contextual information
            
        Returns:
            Dictionary representing the generated job
        """
        if context is None:
            context = {}
        
        # Get snippets for this role
        role_snippets = self.roles_config['snippets_by_role'].get(role, {})
        snippets_to_include = self._select_snippets(role, role_snippets, context)
        
        # Generate job object
        job = {
            'metadata': {
                'job_id': f"{role}_{step}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'generated_at': datetime.now().isoformat(),
                'role': role,
                'step': step,
                'title': title or f"Step {step}",
                'status': 'created'
            },
            'context': context,
            'snippets': snippets_to_include,
            'includes': self._build_includes(snippets_to_include, context),
            'job_folder': self._get_job_folder(role, step),
            'instructions': self._generate_instructions(role, step, title, context)
        }
        
        return job
    
    def _select_snippets(self, role: str, role_snippets: Dict, 
                        context: Dict) -> List[str]:
        """Select which snippets to include based on role and context."""
        selected = []
        
        # Always include these
        selected.extend(role_snippets.get('always_include', []))
        
        # Conditionally include based on context
        for snippet_name, snippet_config in self.snippets_config.get(role, {}).items():
            if snippet_config.get('context_dependent') and snippet_config.get('context_triggers'):
                # Check if any trigger is in context
                for trigger in snippet_config['context_triggers']:
                    if context.get(trigger) is True:
                        snippet_path = f"{role}/{snippet_name}"
                        if snippet_path not in selected:
                            selected.append(snippet_path)
        
        return selected
    
    def _build_includes(self, snippets: List[str], context: Dict) -> str:
        """Build markdown includes section for job README."""
        includes_md = "## Required Reading\n\n"
        
        # Group snippets by category
        shared = [s for s in snippets if s.startswith('shared/')]
        role_specific = [s for s in snippets if not s.startswith('shared/')]
        
        # Shared standards
        if shared:
            includes_md += "### Shared Standards\n"
            for snippet in shared:
                name = snippet.split('/')[-1].replace('.md', '')
                includes_md += f"- [{name}](../../{snippet})\n"
            includes_md += "\n"
        
        # Role-specific
        if role_specific:
            includes_md += "### Role-Specific Guidance\n"
            for snippet in role_specific:
                name = snippet.split('/')[-1].replace('.md', '')
                includes_md += f"- [{name}](../../{snippet})\n"
            includes_md += "\n"
        
        return includes_md
    
    def _get_job_folder(self, role: str, step: int) -> str:
        """Get job folder path."""
        return f"jobs/{role}-step-{step}"
    
    def _generate_instructions(self, role: str, step: int, 
                              title: str, context: Dict) -> str:
        """Generate job-specific instructions."""
        template = f"""# Job: {role.title()} - Step {step}{f': {title}' if title else ''}

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Your Role

You are the **{role.title()}** for this step.

See your role overview: [../../roles/{role}/COMPLETE_ROLE.md](../../roles/{role}/COMPLETE_ROLE.md)

## Context

### Step Information
- **Step**: {step}
- **Title**: {title or f'Step {step}'}
- **Role**: {role.title()}

### Related Steps
"""
        
        # Add related steps from context
        if 'related_steps' in context:
            for s in context['related_steps']:
                template += f"- Step {s}\n"
        else:
            template += f"- Step {step - 1} (previous)\n- Step {step + 1} (next)\n"
        
        # Add dependencies
        if 'dependencies' in context:
            template += "\n### Dependencies\n"
            for dep in context['dependencies']:
                template += f"- {dep}\n"
        
        # Add designer spec for coders
        if role == 'coder' and 'designer_spec' in context:
            template += f"\n### Designer Specification\n\nSee: {context['designer_spec']}\n"
        
        # Add verification items for maintainers
        if role == 'maintainer':
            template += "\n### What to Verify\n"
            if context.get('file_organization_check'):
                template += "- [ ] File organization matches specification\n"
            if context.get('code_review'):
                template += "- [ ] Code quality and style\n"
            if context.get('test_verification'):
                template += "- [ ] Tests pass and coverage >= 80%\n"
            if context.get('documentation_check'):
                template += "- [ ] Documentation is complete\n"
        
        return template
    
    def save_job(self, job: Dict, output_dir: str = ".") -> Path:
        """Save generated job to disk."""
        output_path = Path(output_dir) / job['job_folder']
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save job metadata
        metadata_file = output_path / "job_metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(job, f, indent=2, default=str)
        
        # Create README with instructions and includes
        readme_file = output_path / "README.md"
        readme_content = job['instructions'] + "\n\n" + job['includes']
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        print(f"✓ Job created: {output_path}")
        print(f"  - README.md (start here)")
        print(f"  - job_metadata.json (configuration)")
        
        return output_path


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate specific agent jobs from snippets and context"
    )
    
    parser.add_argument('--role', 
                       choices=['designer', 'coder', 'maintainer'],
                       required=True,
                       help='Agent role')
    
    parser.add_argument('--step',
                       type=int,
                       required=True,
                       help='Step number')
    
    parser.add_argument('--title',
                       help='Step title')
    
    parser.add_argument('--context',
                       help='JSON file with context')
    
    parser.add_argument('--config-dir',
                       default='.',
                       help='Config directory path')
    
    parser.add_argument('--output-dir',
                       default='.',
                       help='Output directory for job')
    
    args = parser.parse_args()
    
    # Load context if provided
    context = {}
    if args.context:
        with open(args.context, 'r') as f:
            context = json.load(f)
    
    # Generate job
    generator = JobGenerator(args.config_dir)
    job = generator.generate_job(
        role=args.role,
        step=args.step,
        title=args.title,
        context=context
    )
    
    # Save job
    generator.save_job(job, args.output_dir)
    
    print(f"\n✓ Job generated successfully")
    print(f"  Role: {args.role}")
    print(f"  Step: {args.step}")
    print(f"  Snippets included: {len(job['snippets'])}")


if __name__ == '__main__':
    main()
