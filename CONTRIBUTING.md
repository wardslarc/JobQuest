# Contributing to Job Quest

Thank you for your interest in contributing to Job Quest! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions. We're building a welcoming community for job seekers and developers alike.

## How to Contribute

### 1. Bug Reports

If you find a bug, please open an issue with:

- Clear title describing the bug
- Detailed description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Your environment (Python version, Django version, OS)

### 2. Feature Requests

Have an idea for a new feature? Open an issue with:

- Clear title describing the feature
- Detailed description of what and why
- Potential implementation approach
- Use cases and benefits
- Examples of similar features in other apps

### 3. Pull Requests

#### Before You Start

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature-name`
3. Set up development environment: `python -m venv env && source env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt && npm install`

#### While Developing

- Follow PEP 8 style guide for Python
- Keep commits atomic and descriptive
- Write clear commit messages
- Test your changes locally
- Update documentation as needed

#### Before Submitting

1. Ensure all tests pass
2. Run Django migrations if needed
3. Rebuild Tailwind CSS: `npm run build`
4. Test in both light and dark modes
5. Verify responsive design on mobile
6. Update README if behavior changed
7. Add/update docstrings for new functions

#### Pull Request Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issue

Closes #(issue number)

## Testing

Describe testing performed

## Screenshots (if applicable)

Add before/after screenshots

## Checklist

- [ ] Code follows style guidelines
- [ ] Migrations created if needed
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] No console errors
```

## Development Workflow

### Setting Up Development Environment

```bash
# Clone and enter directory
git clone https://github.com/yourusername/job-quest.git
cd job-quest/resume

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
npm install

# Run migrations
python manage.py migrate

# Initialize achievements
python manage.py initialize_achievements

# Start development server
python manage.py runserver

# In another terminal, watch Tailwind CSS
npm run dev
```

### Project Structure

```
resume/
├── resumeapp/           # Main Django app
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # URL routing
│   ├── forms.py         # Django forms
│   └── management/      # Management commands
├── leaderboard/         # Leaderboard app
├── templates/           # HTML templates
├── static/              # CSS, JS, images
└── tests/               # Test files
```

## Code Style Guidelines

### Python (PEP 8)

```python
# Good
def get_user_achievements(user):
    """Get all achievements for a user."""
    return Achievement.objects.filter(users=user)

# Avoid
def getAchievements(user):
    achievements = Achievement.objects.filter(users=user)
    return achievements
```

### HTML/Template

- Use 2-space indentation
- Add comments for complex sections
- Use semantic HTML elements
- Include accessibility attributes (alt, aria-label, etc.)

### JavaScript

- Use const/let instead of var
- Use arrow functions where appropriate
- Add comments for complex logic
- Use descriptive variable names

### CSS (Tailwind)

- Use Tailwind utility classes
- Avoid custom CSS when possible
- Keep color scheme consistent
- Test responsive breakpoints

## Testing

### Running Tests

```bash
python manage.py test

# With coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

### Test Structure

```python
from django.test import TestCase
from .models import Application, Achievement

class ApplicationTest(TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_application_creation(self):
        """Test creating a new application."""
        app = Application.objects.create(
            user=self.user,
            company='Tech Corp',
            position='Developer'
        )
        self.assertEqual(app.company, 'Tech Corp')
```

## Documentation

### Code Comments

- Use docstrings for functions/classes
- Add comments for complex logic
- Explain the "why" not the "what"

### Example Docstring

```python
def unlock_achievement(user, criterion):
    """
    Unlock an achievement for a user based on a criterion.

    Args:
        user (User): The user unlocking the achievement
        criterion (str): The achievement criterion identifier

    Returns:
        bool: True if achievement was unlocked, False otherwise

    Raises:
        Achievement.DoesNotExist: If criterion not found
    """
```

## Commit Messages

Use clear, descriptive commit messages:

```
# Good
feat: add achievement notifications
fix: resolve dashboard loading issue
docs: update achievement documentation

# Avoid
update code
fix stuff
changes
```

Format: `<type>: <subject>`

Types:

- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code style
- `refactor` - Code refactoring
- `test` - Tests
- `chore` - Maintenance

## Performance Considerations

- Minimize database queries (use select_related, prefetch_related)
- Cache expensive calculations
- Optimize template rendering
- Lazy load heavy resources
- Test with realistic data volumes

## Security

- Never commit secrets or API keys
- Validate all user input
- Sanitize output
- Use Django's security features (CSRF, XSS protection)
- Keep dependencies updated

## Documentation Standards

When adding features, update:

1. README.md
2. Inline code comments
3. Relevant documentation files
4. This CONTRIBUTING guide if needed

## Release Process

Maintainers handle releases following semantic versioning:

- MAJOR: Breaking changes
- MINOR: New features
- PATCH: Bug fixes

## Getting Help

- Check existing issues and documentation
- Review code comments and docstrings
- Ask in pull request comments
- Start a discussion for ideas

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- GitHub contributors page

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Job Quest! 🎉
