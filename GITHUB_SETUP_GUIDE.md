# GitHub Setup Guide - Breast Cancer Classification Project

## Remote Repository Configuration

### Current Status
```
Remote: origin
URL: https://github.com/username/repo.git
Status: Configured and ready to push
```

## Step 1: Update Remote URL (if needed)

If you need to change the repository URL:

```bash
# View current remote
git remote -v

# Change remote URL
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Or remove and re-add
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

## Step 2: Create GitHub Repository

1. Go to [https://github.com](https://github.com)
2. Click the **+** icon in the top right
3. Select **New repository**
4. Fill in details:
   - **Repository name:** `breast-cancer-classifier` (or your choice)
   - **Description:** Breast Cancer Classification Model Comparison
   - **Visibility:** Public or Private
   - **Do NOT initialize with README** (leave empty)
5. Click **Create repository**
6. Copy the repository URL (HTTPS or SSH)

## Step 3: Update Your Local Remote

Replace the placeholder URL with your actual repository URL:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/breast-cancer-classifier.git
```

**Example:**
```bash
git remote set-url origin https://github.com/parijat-roy/breast-cancer-classifier.git
```

Verify it was updated:
```bash
git remote -v
```

## Step 4: Push to GitHub

### Option A: Rename branch to main (recommended)
```bash
git branch -M main
git push -u origin main
```

### Option B: Keep as master
```bash
git push -u origin master
```

## Step 5: Authenticate

When you run `git push`, you'll be prompted to authenticate. Choose one method:

### Method 1: HTTPS with Personal Access Token (Recommended)

**Generate Personal Access Token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Click "Generate new token"
3. Give it a name: `Breast Cancer Project`
4. Select scopes:
   - `repo` (full control of private repositories)
   - `workflow` (update GitHub Actions workflows)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again)

**Use the token:**
When Git asks for password:
```
Username: your-github-username
Password: paste-your-personal-access-token
```

Select "Store credentials" to avoid re-entering.

### Method 2: SSH Key (Most Secure)

**Generate SSH Key:**
```bash
ssh-keygen -t ed25519 -C "2025ac05223@wilp.bits-pilani.ac.in"
# Press Enter for default location
# Enter passphrase (optional, for extra security)
```

**Add SSH Key to GitHub:**
1. Open `~/.ssh/id_ed25519.pub` with a text editor
2. Copy the entire contents
3. Go to GitHub → Settings → SSH and GPG keys
4. Click "New SSH key"
5. Paste the key
6. Click "Add SSH key"

**Update your remote URL to SSH:**
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/breast-cancer-classifier.git
```

**Test SSH connection:**
```bash
ssh -T git@github.com
# Should output: Hi username! You've successfully authenticated...
```

### Method 3: Git Credential Manager (Windows Built-in)

1. Windows will prompt you to sign in to GitHub
2. Follow the OAuth flow
3. Credentials are automatically cached
4. Future operations use cached credentials

## Complete Push Workflow

```bash
# 1. Verify your remote
git remote -v

# 2. Create/update personal access token on GitHub (HTTPS) or SSH key

# 3. Update remote URL if needed (HTTPS example)
git remote set-url origin https://github.com/YOUR_USERNAME/breast-cancer-classifier.git

# 4. Rename branch to main (if using master)
git branch -M main

# 5. Push to GitHub
git push -u origin main

# 6. When prompted, enter credentials/token
# GitHub username: your-username
# GitHub password: personal-access-token (or use SSH)

# 7. Verify on GitHub
# Visit https://github.com/YOUR_USERNAME/breast-cancer-classifier
```

## Verification

After successful push, verify:

```bash
# Check remote status
git remote -v

# Check branch tracking
git status

# View commits on GitHub
# Visit: https://github.com/YOUR_USERNAME/breast-cancer-classifier
```

## Troubleshooting

### Problem: "fatal: remote origin already exists"
**Solution:** Remove old remote first
```bash
git remote remove origin
git remote add origin <new-url>
```

### Problem: "Authentication failed"
**Solution:** 
- Check personal access token is correct
- Ensure you have push permissions
- For SSH: verify SSH key is added to GitHub account
- Try re-entering credentials

### Problem: "Repository not found"
**Solution:**
- Verify repository URL is correct
- Ensure repository exists on GitHub
- Check you have permission to push

### Problem: "Could not read Username"
**Solution:** Update Git Credential Manager
```bash
git credential reject https://github.com
git credential approve https://github.com
# Re-enter credentials when prompted
```

## Future Operations

After initial setup, operations become simple:

### Push local commits
```bash
git push
```

### Pull remote changes
```bash
git pull
```

### Create feature branch
```bash
git checkout -b feature/new-feature
# Make changes
git add -A
git commit -m "Add new feature"
git push -u origin feature/new-feature
```

### Push to existing branch
```bash
git push origin feature-branch-name
```

## GitHub Best Practices

### Branch Protection (Optional)
1. Go to repository → Settings → Branches
2. Click "Add rule"
3. Set branch name to `main`
4. Enable:
   - "Require a pull request before merging"
   - "Require status checks to pass"
   - "Require branches to be up to date"
5. Click "Create"

### Add .gitignore on GitHub
If you want GitHub-specific ignores:
1. Create `.gitignore` in repository root
2. We already have this configured locally

### Add README.md
1. Create README.md with project description
2. Stage, commit, and push:
```bash
git add README.md
git commit -m "Add README"
git push
```

### Add GitHub Actions (CI/CD)
1. Create `.github/workflows/` directory
2. Add workflow files for automated testing
3. Push to GitHub

## Commands Summary

```bash
# Setup
git remote add origin <url>
git branch -M main
git push -u origin main

# Daily development
git status
git add -A
git commit -m "description"
git push

# Create feature branch
git checkout -b feature/name
git push -u origin feature/name

# View on GitHub
# https://github.com/USERNAME/REPO_NAME
```

## Next Steps

1. **Create GitHub Repository**
   - Go to github.com
   - Create new empty repository
   - Copy the URL

2. **Update Remote URL**
   ```bash
   git remote set-url origin <your-github-url>
   ```

3. **Generate Authentication**
   - Personal Access Token (HTTPS) OR
   - SSH Key (SSH) OR
   - Windows Credential Manager

4. **Push Code**
   ```bash
   git branch -M main
   git push -u origin main
   ```

5. **Verify**
   - Check GitHub repository
   - View commits and files online
   - Share repository link

## Resources

- [GitHub Documentation](https://docs.github.com/)
- [Personal Access Tokens](https://github.com/settings/tokens)
- [SSH Keys](https://github.com/settings/keys)
- [Git Documentation](https://git-scm.com/doc)

---

**Setup Guide Created:** August 13, 2026  
**Project:** Breast Cancer Classification  
**Author:** Parijat Roy  
**Status:** Ready for GitHub deployment
