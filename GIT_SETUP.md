# Git Setup Guide - Breast Cancer Classification Project

## ✅ Git Repository Initialized

The project has been successfully set up as a Git repository.

## Repository Information

- **Location:** `d:\BITS_WILP\Sem 1\ML\Assignment 2`
- **Status:** Initialized and committed
- **Initial Commit:** e4cfcda - Initial commit: Breast Cancer Classification Model Comparison

## Git Configuration

### Local Configuration
```
User Email: sme2@uplevel.academy
User Name: ML Student
Core Format Version: 0
File Mode: false
Bare Repository: false
Log All Ref Updates: true
Symlinks: false
Ignore Case: true
```

## Files and Folders

### Code Files (Tracked)
- ✅ `model_training.py` - ML pipeline
- ✅ `streamlit_app.py` - Web application
- ✅ `requirements.txt` - Dependencies
- ✅ `run_app.bat` - Windows launcher
- ✅ `run_app.ps1` - PowerShell launcher
- ✅ `app.py` - Additional app file

### Model Files (Tracked)
- ✅ `model/logistic_regression_model.pkl`
- ✅ `model/decision_tree_model.pkl`
- ✅ `model/knn_model.pkl`
- ✅ `model/naive_bayes_model.pkl`
- ✅ `model/random_forest_model.pkl`
- ✅ `model/feature_scaler.pkl`

### Documentation (Tracked)
- ✅ README.md
- ✅ DEPLOYMENT_GUIDE.md
- ✅ CHANGES.md
- ✅ And other documentation files

### Ignored Files (.gitignore)
- Python cache files (`__pycache__/`, `*.pyc`)
- Virtual environments (`venv/`, `ENV/`)
- IDE files (`.vscode/`, `.idea/`)
- Temporary files (`*.tmp`, `*.log`)
- Environment files (`.env`, `.env.local`)
- OS files (`Thumbs.db`, `.DS_Store`)

## Common Git Commands

### View commit history
```bash
git log
git log --oneline
git log --graph --all --decorate
```

### Check status
```bash
git status
```

### Make changes
```bash
git add <file>
git commit -m "Your commit message"
```

### Create branches
```bash
git branch <branch-name>
git checkout <branch-name>
```

### Connect to remote repository
```bash
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```

## Typical Workflow

### 1. Make Code Changes
Edit your files in the project directory.

### 2. Stage Changes
```bash
git add model_training.py streamlit_app.py
# or add all changes
git add -A
```

### 3. Commit Changes
```bash
git commit -m "Update model training for better performance"
```

### 4. View History
```bash
git log --oneline
```

### 5. Push to Remote (if configured)
```bash
git push origin main
```

## Initial Commit Details

The initial commit includes:
- Migration from Wine dataset to Breast Cancer dataset
- 569 samples (exceeds 500 minimum requirement)
- 5 classification models implementation
- 6 evaluation metrics
- Streamlit web application
- Deployment scripts
- Comprehensive documentation
- Trained model files
- All dependencies configured

## Setting Up Remote Repository

If you want to push this to GitHub or GitLab:

### GitHub
```bash
# Create repository on GitHub first

# Add remote
git remote add origin https://github.com/username/repo-name.git

# Rename branch to main (if needed)
git branch -M main

# Push
git push -u origin main
```

### GitLab
```bash
git remote add origin https://gitlab.com/username/repo-name.git
git branch -M main
git push -u origin main
```

## Authentication

For GitHub/GitLab authentication, you can use:

### Option 1: HTTPS with Token
```bash
git clone https://username:token@github.com/username/repo.git
```

### Option 2: SSH Keys
```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "sme2@uplevel.academy"

# Add public key to GitHub/GitLab account settings
# Then use SSH URL for cloning/remote
git remote add origin git@github.com:username/repo.git
```

### Option 3: Git Credential Manager
```bash
# Windows with credential manager
# Will prompt for credentials on first push/pull
git push origin main
```

## Useful Git Configurations

### Set default editor
```bash
git config --global core.editor "code"
```

### Set line endings
```bash
git config --global core.autocrlf true
```

### View all config
```bash
git config --local --list
```

## Branching Strategy

Recommended branching pattern:

```
main/master (production-ready)
  ├── develop (development branch)
  │   ├── feature/breast-cancer-models
  │   ├── feature/streamlit-ui
  │   ├── bugfix/model-accuracy
  │   └── docs/deployment-guide
```

### Create a feature branch
```bash
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "Add new feature"
git checkout develop
git merge feature/new-feature
```

## Version Tags

To create releases:

```bash
# Create a tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tags
git push origin --tags

# View tags
git tag -l
```

## Troubleshooting

### Problem: "fatal: Not a git repository"
**Solution:** Run `git init` in the project directory

### Problem: "Please commit or stash your changes"
**Solution:** Either commit your changes or stash them
```bash
git stash
```

### Problem: "Permission denied"
**Solution:** Check SSH keys or use HTTPS with token authentication

### Problem: "Merge conflict"
**Solution:** Resolve conflicts manually in affected files, then:
```bash
git add resolved-file.py
git commit -m "Resolve merge conflict"
```

## Best Practices

✓ Commit frequently with meaningful messages
✓ Use descriptive branch names
✓ Keep commits focused on single changes
✓ Use .gitignore to exclude unnecessary files
✓ Review changes before committing
✓ Use tags for releases
✓ Sync with remote regularly

## Project-Specific Guidelines

### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation update
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Build/dependency updates

### Example
```
feat: Add Breast Cancer dataset migration

- Changed from Wine dataset (178 samples) to Breast Cancer (569 samples)
- Updated model_training.py with new class
- Updated streamlit_app.py with new dataset references
- All metrics calculated correctly

Closes #123
```

## Git Credentials Setup (Windows)

### Using Git Credential Manager
1. Git will prompt for credentials on first push
2. Enter username and personal access token
3. Credentials are cached for future operations

### Using SSH Keys
1. Generate key: `ssh-keygen -t ed25519 -C "sme2@uplevel.academy"`
2. Add public key to GitHub/GitLab
3. Use SSH URLs for repositories

### Using Personal Access Token (GitHub)
1. Create token in GitHub Settings → Developer settings
2. Use as password: `git push https://username:token@github.com/user/repo.git`

---

**Setup Date:** August 13, 2026
**Repository Status:** Active
**Initial Commit Hash:** e4cfcda
**Total Files Tracked:** 28
